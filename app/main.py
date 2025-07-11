import urllib3
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
    if settings.cosmos_use_emulator == "True":
        # We expect this to raise warnings as we're going to
        # accept an unverified connection to cosmosDB emulator
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    return CosmosClient(
        url=settings.cosmos_url,
        credential=settings.cosmos_key,
        connection_verify=(settings.cosmos_use_emulator != "True"),
    )


@lru_cache
def get_container() -> ContainerProxy:
    client = get_cosmos_client()
    return cosmos.setup_cosmos(client, db_id="mydb", container_id="default")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/write")
async def write_cosmos(
    container: Annotated[ContainerProxy, Depends(dependency=get_container)],
):
    _res = container.upsert_item({"id": "my item 123"})
    return {"message": "success"}
