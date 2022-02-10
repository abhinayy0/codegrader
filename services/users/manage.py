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
def seed_db():
    db.session.add(User(useername="a1", email="a1@gmail.com"))
    db.session.add(User(useername="a2", email="a2@gmail.com"))
    db.session.commit()

@cli.command()
def test():
    retcode = pytest.main(["-x","project/tests", "-v", "-s","--capture","no"])
    return retcode


if __name__ == "__main__":
    cli()