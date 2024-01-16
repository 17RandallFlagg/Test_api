import pytest
import test_api


@pytest.fixture(scope="function")
def list_users_fields():
    field = {
        "page": None,
        "per_page": None,
        "total": None,
        "total_pages": None,
        "data": None
    }
    yield field


@pytest.fixture(scope="function")
def user_fields():
    data = {
        "id": None,
        "email": None,
        "first_name": None,
        "last_name": None,
        "avatar": None
    }
    yield data


@pytest.fixture(scope="function")
def post_response_fields():
    field = {
        "name": None,
        "job": None,
        "id": None,
        "createdAt": None
    }
    yield field


@pytest.fixture(scope="function")
def put_response_fields():
    field = {
        "name": "morpheus",
        "job": "zion resident",
        "updatedAt": None
    }
    yield field
