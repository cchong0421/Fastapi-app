from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 建立 FastAPI 實例
app = FastAPI()

# 資料庫連線設定
SQLALCHEMY_DATABASE_URL = "sqlite:///./demo.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 建立資料表映射模型
Base = declarative_base()

class Menulist(Base):
    __tablename__ = "Menulist2"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    isenable = Column(Integer)
    parentid = Column(Integer)


# 定義 Pydantic 模型用於接收和回傳資料
class MenuCreate(BaseModel):
    name: str
    description: str
    isenable: int
    parentid: int

class MenuUpdate(BaseModel):
    name: str = None
    description: str = None
    isenable: int = None
    parentid: int = None

class Menu(BaseModel):
    id: int
    name: str
    description: str
    isenable: int
    parentid: int

class MenuList(BaseModel):
    items: List[Menu]


# 建立資料庫表格
Base.metadata.create_all(bind=engine)

# 路由定義
@app.get("/menu/{menu_id}", response_model=Menu)
def read_menu(menu_id: int):
    db = SessionLocal()
    menu = db.query(Menulist).filter(Menulist.id == menu_id).first()
    db.close()
    if menu is None:
        return {"error": "Menu not found"}
    
    return Menu(
        id=menu.id,
        name=menu.name,
        description=menu.description,
        isenable=menu.isenable,
        parentid=menu.parentid
    )

@app.get("/menu", response_model=MenuList)
def read_menu_list():
    db = SessionLocal()
    menus = db.query(Menulist).all()
    db.close()
    menu_list = [Menu(
        id=menu.id,
        name=menu.name,
        description=menu.description,
        isenable=menu.isenable,
        parentid=menu.parentid
    ) for menu in menus]
    return {"items": menu_list}

@app.post("/menu", response_model=Menu)
def create_menu(menu: MenuCreate):
    db = SessionLocal()
    menu_data = Menulist(**menu.dict())
    db.add(menu_data)
    db.commit()
    db.refresh(menu_data)
    db.close()
    return Menu(
        id=menu_data.id,
        name=menu_data.name,
        description=menu_data.description,
        isenable=menu_data.isenable,
        parentid=menu_data.parentid
    )

@app.put("/menu/{menu_id}", response_model=Menu)
def update_menu(menu_id: int, menu: MenuUpdate):
    db = SessionLocal()
    menu_data = db.query(Menulist).filter(Menulist.id == menu_id).first()
    if menu_data is None:
        return {"error": "Menu not found"}
    for field, value in menu.dict(exclude_unset=True).items():
        setattr(menu_data, field, value)
    db.commit()
    db.refresh(menu_data)
    db.close()
    return Menu(
        id=menu_data.id,
        name=menu_data.name,
        description=menu_data.description,
        isenable=menu_data.isenable,
        parentid=menu_data.parentid
    )

@app.delete("/menu/{menu_id}")
def delete_menu(menu_id: int):
    db = SessionLocal()
    menu_data = db.query(Menulist).filter(Menulist.id == menu_id).first()
    if menu_data is None:
        return {"error": "Menu not found"}
    db.delete(menu_data)
    db.commit()
    db.close()
    return {"message": "Menu deleted"}


# 啟動 FastAPI 服務
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)