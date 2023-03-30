from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models import crud_db
from app.configuration.database.databaseconfiguration import engine
from app.controllers.crudtest import ServerCrudTestController
import uvicorn

app = FastAPI()
origins = [
    "http://localhost:9000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

crud_db.Base.metadata.create_all(engine)

app.include_router(ServerCrudTestController.router,tags=["DMS_General_Master"],prefix="/api/general")

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.0",port=9000)