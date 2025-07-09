import urllib3
from azure.cosmos.container import ContainerProxy
from azure.cosmos import CosmosClient, PartitionKey
from functools import lru_cache

from . import config


def _setup_cosmos(client: CosmosClient, db_id: str, container_id: str):
    db = client.create_database_if_not_exists(id=db_id)
    return db.create_container_if_not_exists(
        partition_key=PartitionKey(path='/id'), id=container_id
    )


@lru_cache
def get_cosmos_client():
    settings = config.get_settings()
    if settings.cosmos_use_emulator == 'True':
        # We expect this to raise warnings as we're going to
        # accept an unverified connection to cosmosDB emulator
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    return CosmosClient(
        url=settings.cosmos_url,
        credential=settings.cosmos_key,
        connection_verify=(settings.cosmos_use_emulator != 'True'),
    )


@lru_cache
def get_cosmos_container() -> ContainerProxy:
    client = get_cosmos_client()
    return _setup_cosmos(client, db_id='mydb', container_id='default')
