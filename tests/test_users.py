import pytest
import pymongo

from main import app
from db import get_database
from httpx import AsyncClient


BACKEND = "http://127.0.0.1:8000"


@pytest.fixture(scope="function")
def get_db():
    myclient = pymongo.MongoClient("mongodb+srv://ivand1988:Mongopass88@cluster0.fwymo.mongodb.net/?retryWrites=true&w=majority")
    mydb = myclient["test_habits"]
    yield mydb
    mydb.users.delete_many({"email": "test_user@yahoo.com"})


@pytest.fixture
def user_bad_email():
    payload = {
        "username": "test_user",
        "email": "tester_user@yahoo.com",
        "password": "test_Pa5s"
    }
    return payload


@pytest.fixture
def user_bad_password():
    payload = {
        "username": "test_user",
        "email": "test_user@yahoo.com",
        "password": "test4_Pass"
    }
    return payload


@pytest.fixture
def user():
    payload = {
        "username": "test_user",
        "email": "test_user@yahoo.com",
        "password": "test_Pa5s"
    }
    return payload


@pytest.mark.asyncio
async def test_create_user(user):
    """
    GIVEN registration a new user
    WHEN  POST "/user/registrtion" requested
    THEN check status_code, email, username
    """
    async with AsyncClient() as client:
        response = await client.post(f"{BACKEND}/user/registration", json=user)
    response_body = response.json()
    assert response.status_code == 201
    assert response_body["email"] == user["email"]
    assert response_body["username"] == user["username"]

    """
    GIVEN registration a new user with existsing email
    """
    async with AsyncClient() as client:
        response = await client.post(f"{BACKEND}/user/registration", json=user)
    assert response.status_code == 409


@pytest.mark.asyncio
async def test_user_login(user, user_bad_email, user_bad_password, get_db):
    """
    GIVEN user login with wrong email
    WHEN POST "user/login" requested
    THEN check status_code
    """
    async with AsyncClient() as client:
        r = await client.post(f"{BACKEND}/user/login", json=user_bad_email)
    assert r.status_code == 404

    """
    GIVEN user login with wrong password
    """
    async with AsyncClient() as client:
        r_1 = await client.post(f"{BACKEND}/user/login", json=user_bad_password)
    assert r_1.status_code == 401

    """
    GIVEN user with relevant creds
    """
    async with AsyncClient() as client:
        r_2 = await client.post(f"{BACKEND}/user/login", json=user)
        r_2_body = r_2.json()
    assert r_2.status_code == 200
    assert r_2_body == "token"

