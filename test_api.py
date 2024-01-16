import pytest
# import allure
import requests

URL = "https://reqres.in/api"


def test_get_list_users_request():
    response = requests.get(URL + "/users?page=2")
    assert response.status_code == 200


def test_list_users_data(list_users_fields):
    body = list_users_fields.json()
    response = requests.get(URL + "/users?page=2")
    obj = response.json()
    assert obj == body


def test_get_single_users_request():
    response = requests.get(URL + "/users/page/2")
    assert response.status_code == 200


def test_user_data(user_fields):
    body = user_fields.json()
    response = requests.get(URL + "/users?page=2", "data")
    obj = response.json()
    assert obj == body


@pytest.mark.parametrize(
    {
    "name": "morpheus",
    "job": "leader"
    }
)
def test_post_request():
    response = requests.post(URL + "/users")
    assert response.status_code == 201


@pytest.mark.parametrize(
    {
    "name": "morpheus",
    "job": "leader"
    }
)
def test_post_request_create(post_response_fields):
    body = post_response_fields.json()
    response = requests.post(URL + "/users")
    obj = response.json()
    assert obj == body


@pytest.mark.parametrize(
    {
    "name": "morpheus",
    "job": "zion resident"
    }
)
def test_put_request():
    response = requests.put(URL + "/users/2")
    assert response.status_code == 200


@pytest.mark.parametrize(
    {
    "name": "morpheus",
    "job": "zion resident"
}
)
def test_put_request_update(put_patch_del_response_fields):
    body = put_patch_del_response_fields
    response = requests.put(URL + "/users/2")
    obj = response.json()
    assert obj == body


@pytest.mark.parametrize(
    {
    "name": "morpheus",
    "job": "zion resident"
}
)
def test_patch_request():
    response = requests.patch(URL + "/users/2")
    assert response.status_code == 200


@pytest.mark.parametrize(
    {
    "name": "morpheus",
    "job": "zion resident"
}
)
def test_patch_request_update(put_patch_del_response_fields):
    body = put_patch_del_response_fields
    response = requests.put(URL + "/users/2")
    obj = response.json()
    assert obj == body


def test_delete_request():
    response = requests.delete(URL + "/users/2")
    assert response.status_code == 204


def test_delete_request_update(put_patch_del_response_fields):
    body = put_patch_del_response_fields
    response = requests.put(URL + "/users/2")
    obj = response.json()
    assert obj == body

