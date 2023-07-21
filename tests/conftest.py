import pytest
from fastapi.testclient import TestClient

import main


@pytest.fixture
@pytest.mark.asyncio
def client():
    with TestClient(main.app) as c:
        yield c
