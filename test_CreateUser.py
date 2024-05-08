import requests
import json
import jsonpath
import pytest

url = "https://reqres.in/api/users/"


@pytest.fixture(scope="module")
def start_exec():
    global req_json
    file = open("./Fixtures/test.json")
    req_json = json.loads(file.read())
    yield
    file.close()


@pytest.mark.smoke
@pytest.mark.regression
def test_create_user(start_exec):
    response = requests.post(url, req_json)
    assert response.status_code == 201
    print(response.text)
    user_id = jsonpath.jsonpath(response.json(), 'id')
    user_name = jsonpath.jsonpath(response.json(), 'name')
    assert user_id is not None
    assert user_name[0] == "morpheus"
