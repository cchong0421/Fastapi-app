from fastapi import FastAPI, Header, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
import uvicorn
import config
import json

app = FastAPI()


class ErrorModel(BaseModel):
    code: str
    message: str


@app.middleware("http")
async def check_CustHeader(request, call_next):
    custHead = request.headers.get("custhead1")

    response = await call_next(request)
    if not custHead:
        # response.status_code = status.HTTP_401_UNAUTHORIZED
        m = ErrorModel(code="401", message="UnAuthorized")
        print()
        # return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,
        #                     content={"Error": "UnAuthorized"})
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,
                            content=json.dumps(m.__dict__),
                            headers={'Content-type': 'application/json'})
    return response


@app.get("/")
async def root_index():
    return {'Hello': f"world --- {config.ServerName}"}
