from azure.storage.blob import BlobServiceClient, ContainerClient
from functools import lru_cache

from . import config


@lru_cache
def get_blob_client():
    settings = config.get_settings()
    return BlobServiceClient.from_connection_string(
        settings.blob_connection_string,
        verify=(settings.blob_use_azurite != 'True'))


@lru_cache
def get_blob_container() -> ContainerClient:
    client = get_blob_client()
    return client.get_container_client("my-container")

