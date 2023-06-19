import json
import app.config as config
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Header, HTTPException, status, Request
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Optional
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi import FastAPI, Request, Header, HTTPException, status

app = FastAPI()

app.mount("/static", StaticFiles(directory="./app/static"), name="static")
templates = Jinja2Templates(directory="./app/templates")


class ErrorModel(BaseModel):
    code: str
    message: str


@app.middleware("http")
async def check_CustHeader(request, call_next):
    custHead = request.headers.get("custhead1")

    response = await call_next(request)
    # if not custHead:
    #     # response.status_code = status.HTTP_401_UNAUTHORIZED
    #     m = ErrorModel(code="401", message="UnAuthorized")
    #     print()
    #     # return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,
    #     #                     content={"Error": "UnAuthorized"})
    #     return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,
    #                         content=json.dumps(m.__dict__),
    #                         headers={'Content-type': 'application/json'})
    return response


class Test(BaseModel):
    username: str
    password: str
    email: str
    today: str


@app.get("/")
async def root_index():
    return {'Hello': f"world --- {config.ServerName}"}


@app.post("/data", tags=["data"])
async def post_data(request: Request, test: Test):
    print(test)
    return {"result": "Success", "data": test}


@app.get("/formfetch", response_class=HTMLResponse)
async def read_formfetch(request: Request):
    return templates.TemplateResponse("formfetch.html", {"request": request})

@app.get("/jinja2/index", tags=["tutorial"])
async def webpage_index(request: Request):
    return templates.TemplateResponse("tutorial-jinja2.html", { "request": request})