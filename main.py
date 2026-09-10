from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.api.v1.api import api_router
from app.core.exceptions import AppException
from app.db.session import Base, engine
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Stock & Portfolio Tracker API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origin=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.exception_handler(AppException)
async def app_exceptions_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "succes": False,
            "error" : {
                "code": exc.status_code,
            },
        },
    )

app.include_router(api_router, prefix="/api/v1")