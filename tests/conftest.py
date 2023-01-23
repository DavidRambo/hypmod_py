# tests/conftest.py
import pytest


@pytest.fixture
def mock_requests_get(mocker):
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Mock Title",
        "extract": "Mock extract text",
    }
    return mock
