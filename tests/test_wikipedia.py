# tests/test_wikipedia.py
from hypmod_py import wikipedia


def test_random_page_uses_given_language(mock_requests_get):
    """Tests CLI argument for different language."""
    wikipedia.random_page(language="de")
    args, _ = mock_requests_get.call_args
    assert "de.wikipedia.org" in args[0]
