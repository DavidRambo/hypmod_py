# src/hypmod_py/console.py
import textwrap  # stdlib module for wrapping console text

import click
import requests

from . import __version__

# REST API of Wikipedia's /page/random/sammary
API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"


@click.command()
@click.version_option(version=__version__)
def main():
    """The hypermodern Python project."""
    with requests.get(API_URL) as response:
        response.raise_for_status()  # check HTTP status code
        data = response.json()  # retrieved data in json format

        title = data["title"]
        extract = data["extract"]

        click.secho(title, fg="green")
        click.echo(textwrap.fill(extract))
