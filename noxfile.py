# noxfile.py
import nox


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
