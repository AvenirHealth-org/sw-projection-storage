from functools import lru_cache
from fastapi import Depends, FastAPI
from typing_extensions import Annotated
from azure.cosmos import ContainerProxy, CosmosClient

from . import config
from . import cosmos


app = FastAPI()


@lru_cache
def get_settings():
    return config.Settings()


@lru_cache
def get_cosmos_client():
    settings = get_settings()
    return CosmosClient(
        url=settings.cosmos_url,
        credential=settings.cosmos_key
    )


@lru_cache
def get_container() -> ContainerProxy:
    client = get_cosmos_client()
    return cosmos.setup_cosmos(client, db_id="mydb", container_id="default")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/write")
async def write_cosmos(container: Annotated[ContainerProxy, Depends(dependency=get_container)]):
    _res = container.upsert_item({"key": "my item 123"})
    return {"message": "success"}
