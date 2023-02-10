# tests/conftest.py
# from unittest import Mock
import pytest
from pytest_mock import MockFixture


@pytest.fixture
def mock_requests_get(mocker: MockFixture) -> None:
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Mock Title",
        "extract": "Mock extract text",
    }
    return mock


def pytest_configure(config):
    config.addinivalue_line("markers", "e2e: mark as end-to-end test.")
