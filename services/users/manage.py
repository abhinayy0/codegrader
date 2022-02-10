from flask.cli import FlaskGroup
from project import create_app
from project import db
from project.api.models import User
import pytest
import sys

app =create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command()
def test():
    retcode = pytest.main(["-x","project/tests", "-v", "-s","--capture","no"])
    return retcode


if __name__ == "__main__":
    cli()