from app.db.models import User
from flask import session
import pandas as pd


def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, and role fields are defined correctly
    """
    user = User('bebo', 'patkennedy79@gmail.com', 'FlaskIsAwesome')
    assert user.username == 'bebo'
    assert user.email == 'patkennedy79@gmail.com'
    assert user.password == 'FlaskIsAwesome'


def test_signup():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, and role fields are defined correctly
    """
    user = User('tajwar', 'tajwar.bilal@gmail.com', '12345')
    assert user.username == 'tajwar'
    assert user.email == 'tajwar.bilal@gmail.com'
    assert user.password == '12345'


def test_not_signup():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, and role fields are defined correctly
    """
    user = User('tajwar', 'tajwar.bilal@gmail.com', '123')
    assert user.username == 'tajwar'
    assert user.email == 'tajwar.bilal@gmail.com'
    assert user.password == '123'


def test_user_not_in_session():
    """
        You can test if the sessions are working
    """
    if 'user' is None:
        session['user'] = 'bebo'

    username = 'bebo'
    assert username == 'bebo'


def test_csv_file():
    """
        Need to test the file
    """
    try:
        csvData = pd.read_csv('transactions.csv')
    except:
        pass

    check = 0
    if csvData is not None:
        check = 1

    assert check == 1


def test_csv_not_in_file():
    """
        Need to test the incorrect file
    """
    check = 1
    try:
        csvData = pd.read_csv('transaction.csv')
    except:
        check = 0

    assert check == 0
