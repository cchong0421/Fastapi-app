from fastapi import FastAPI
import uvicorn
import config

app = FastAPI()

@app.get("/")
def root_index():
    return {'Hello': f"world --- {config.ServerName}"}
