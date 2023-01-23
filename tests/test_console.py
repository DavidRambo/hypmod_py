# tests/test_console.py
import click.testing
import pytest
import requests

from hypmod_py import console


@pytest.fixture
def runner():
    return click.testing.CliRunner()


@pytest.fixture
def mock_requests_get(mocker):
    """Uses unittest.mock via pytest-mock to replace requests.get."""
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Mock Title",
        "extract": "Mock text extract",
    }
    return mock


def test_main_succeeds(runner, mock_requests_get):
    """Tests the main function in console.py"""
    result = runner.invoke(console.main)
    assert result.exit_code == 0


def test_main_prints_title(runner, mock_requests_get):
    """Tests whether main() prints the title of the retrieved data."""
    result = runner.invoke(console.main)
    assert "Mock Title" in result.output


def test_main_invokes_requests_get(runner, mock_requests_get):
    """Tests whether requests.get was invoked by checking whether the associated mock was
    called."""
    runner.invoke(console.main)
    assert mock_requests_get.called


def test_main_uses_en_wikipedia_org(runner, mock_requests_get):
    """Ensures that the first argument passed to the mock requests object."""
    runner.invoke(console.main)
    args, _ = mock_requests_get.call_args
    assert "en.wikipedia.org" in args[0]


def test_main_fails_on_request_error(runner, mock_requests_get):
    """Tests failure case using the side_effect attribute of the mock."""
    mock_requests_get.side_effect = Exception("Request failed")
    result = runner.invoke(console.main)
    assert result.exit_code == 1


def test_main_prints_message_on_request_error(runner, mock_requests_get):
    """Tests exception in the event of no internet connection."""
    mock_requests_get.side_effect = requests.RequestException
    result = runner.invoke(console.main)
    assert "Error" in result.output
