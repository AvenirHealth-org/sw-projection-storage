import pytest
from app.main import get_cosmos_client


def is_emulator_running():
    try:
        _client = get_cosmos_client()
        return True
    except:
        return False


emulator_running = pytest.mark.skipif(
    not is_emulator_running(), reason="CosmosDB emulator not running"
)
