from app import create_app

app = create_app()

from app.db.models import User
import pytest


@pytest.fixture(scope='module')
def new_user():
    user = User('tajwar', 'patkennedy79@gmail.com', 'FlaskIsAwesome')
    return user


@pytest.fixture(scope='module')
def test_client():
    # Create a test client using the Flask application configured for testing
    with app.test_client() as testing_client:
        # Establish an application context
        with app.app_context():
            yield testing_client  # this is where the testing happens!
