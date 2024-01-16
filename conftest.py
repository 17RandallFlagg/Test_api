import pytest


@pytest.fixture(scope="function")
def list_users_fields():
    field = {
        "page": int,
        "per_page": int,
        "total": int,
        "total_pages": int,
        "data": list
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
def put_patch_del_response_fields():
    field = {
        "name": "morpheus",
        "job": "zion resident",
        "updatedAt": str
    }
    yield field
