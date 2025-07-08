from azure.cosmos.container import ContainerProxy
from azure.cosmos import CosmosClient, PartitionKey, ContainerProxy

def setup_cosmos(client: CosmosClient, db_id: str, container_id: str):
    db = client.create_database_if_not_exists(id=db_id)
    return db.create_container_if_not_exists(partition_key=PartitionKey(
                path="/id"
            ), id=container_id)


def insert(container: ContainerProxy, item: dict[str, str]):
    _res = container.upsert_item(body=item)
