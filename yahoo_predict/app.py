from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from .routes.predict import router as predict_router
from .routes.stock import router as stock_router
from alembic.config import Config
from alembic import command
from .config import Settings

settings = Settings()

app = FastAPI()

app.include_router(predict_router)
app.include_router(stock_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# print("Starting Alembic migration")
# alembic_cfg = Config("alembic.ini")
# command.upgrade(alembic_cfg, "head")
# print("Alembic migration completed")

@app.on_event("startup")
async def startup_event():  
    try:
        print("Starting Alembic migration")
        alembic_cfg = Config("alembic.ini")
        command.upgrade(alembic_cfg, "head")
        print("Alembic migration completed")
    except Exception as e:
        print(f"Error during Alembic migration: {e}")

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
