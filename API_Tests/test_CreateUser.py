import requests
import jsonpath
import pytest

url = "https://reqres.in/api/users/"

'''
Test creation of a new user
Assertions: 
1. Validate status code for user creation API call
2. Validate user id value in the response in not None
3. Validate user name of newly created user
'''
@pytest.mark.api
def test_create_user(start_exec):
    response = requests.post(url, start_exec)
    assert response.status_code == 201
    print(response.text)
    user_id = jsonpath.jsonpath(response.json(), 'id')
    user_name = jsonpath.jsonpath(response.json(), 'name')
    assert user_id is not None
    assert user_name[0] == "morpheus"
