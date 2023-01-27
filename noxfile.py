# noxfile.py
import nox
import tempfile

# default locations to run with nox sessions
locations = "src", "tests", "noxfile.py"
# default sessions to exclude black
nox.options.sessions = "lint", "safety", "tests"


@nox.session(python=["3.10", "3.11"])
def tests(session):
    """Basic nox test.

    Exclude end-to-end tests by passing:
        -m 'not e2e'
        to pytest.
    """
    args = session.posargs or ["--cov", "-m", "not e2e"]
    session.run("poetry", "install", external=True)
    session.run("poetry", "run", "pytest", *args, external=True)


@nox.session(python=["3.10", "3.11"])
def lint(session):
    args = session.posargs or locations
    session.install(
        "flake8",
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        "flake8-import-order",
    )
    session.run("flake8", *args)


@nox.session(python="3.11")
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


@nox.session(python="3.11")
def safety(session):
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        session.install("safety")
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")
