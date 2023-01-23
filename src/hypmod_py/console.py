# src/hypmod_py/console.py
import textwrap  # stdlib module for wrapping console text

import click
import requests

from . import __version__, wikipedia

# REST API of Wikipedia's /page/random/sammary
API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"


@click.command()
@click.version_option(version=__version__)
def main():
    """The hypermodern Python project."""
    data = wikipedia.random_page()

    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
