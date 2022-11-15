#import uvicorn
from fastapi import FastAPI, APIRouter
from app.config import db
from typing import Any

def init_app():
    #db.init()

    app = FastAPI(title = "FARM stack")

    #@app.on_event("startup")
    #async def startup():
    #    await db.create_all()

    #@app.on_event("shutdown")
    #async def shutdown():
    #    await db.close()

    return app

app = init_app()

"""def start():
    uvicorn.run(    "app.main:app", 
                    host="localhost", 
                    port=9999, 
                    reload=True
                    )
"""