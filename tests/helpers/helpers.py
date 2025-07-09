import pytest
from app.cosmos import get_cosmos_client
from app.blob import get_blob_client


def is_emulator_running():
    try:
        _client = get_cosmos_client()
        return True
    except:
        return False


emulator_running = pytest.mark.skipif(
    not is_emulator_running(), reason='CosmosDB emulator not running'
)


def is_blob_store_running():
    try:
        _client = get_blob_client()
        return True
    except:
        return False


azurite_running = pytest.mark.skipif(
    not is_blob_store_running(), reason='Azurite blob store emulator not running'
)
