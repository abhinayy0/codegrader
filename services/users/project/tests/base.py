from project import create_app
from project import db

import os
import tempfile
import pytest

@pytest.fixture
def client():
    app = create_app()
    app.config.from_object('project.config.TestingConfig')

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            db.session.commit()
        print("****before yield")
        yield client
        print("****after yield")
        db.session.remove()
        db.drop_all()
