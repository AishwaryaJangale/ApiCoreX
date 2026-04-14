import pytest
import logging
from core.api_client import APIClient
from utils.config import BASE_URL

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    logging.basicConfig(level=logging.INFO)

@pytest.fixture(scope="session")
def api_client():
    """Returns an instance of APIClient pointing to BASE_URL."""
    client = APIClient(base_url=BASE_URL)
    yield client
    # Any teardown logic (e.g. closing session) can go here
    client.session.close()
