from fastapi import FastAPI, Header, HTTPException, status, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
import config
import json

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class ErrorModel(BaseModel):
    code: str
    message: str


@app.middleware("http")
async def check_CustHeader(request, call_next):
    custHead = request.headers.get("custhead1")

    response = await call_next(request)
    if not custHead:
        response.headers["custhead1"] = "Steven"
        # # response.status_code = status.HTTP_401_UNAUTHORIZED
        # m = ErrorModel(code="401", message="UnAuthorized")
        # print()
        # # return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,
        # #                     content={"Error": "UnAuthorized"})
        # return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,
        #                     content=json.dumps(m.__dict__),
        #                     headers={'Content-type': 'application/json'})
    else:
        response.headers["custhead1"] = custHead
    return response


@app.get("/")
async def root_index(request: Request):
    return templates.TemplateResponse("index.html", { "request": request})
