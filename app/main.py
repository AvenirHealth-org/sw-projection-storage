from fastapi import Depends, FastAPI
from typing_extensions import Annotated
from azure.cosmos import ContainerProxy
from azure.storage.blob import ContainerClient

from . import cosmos
from . import blob


app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.post('/write')
async def write_cosmos(
    container: Annotated[ContainerProxy, Depends(dependency=cosmos.get_cosmos_container)],
):
    _res = container.upsert_item({'id': 'my item 123'})
    return {'message': 'success'}


@app.post('/blob')
async def write_blob(
    container: Annotated[ContainerClient, Depends(dependency=blob.get_blob_container)],
):
    blobs = [blob for blob in container.list_blob_names()]
    if "myblob" not in blobs:
        _res = container.upload_blob("myblob", "my data 123")
    return {'message': 'success'}
