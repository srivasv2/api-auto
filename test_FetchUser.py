import requests
import json
import pytest

'''
Test to validate get request for user data
Assertions: 
1. Validate status code for user details fetch API call
2. Validate response time is below 200ms
3. Response page attribute is equal to 2
'''
@pytest.mark.smoke
def test_fetch_user_data():
    url = "https://reqres.in/api/users?page=2"
    res = requests.get(url)
    print("Value of elapsed time:", res.elapsed)
    # Validate Status code
    assert res.status_code == 200
    print(res.headers)
    assert res.elapsed.seconds < 0.2
    json_res = json.loads(res.text)
    assert json_res['page'] == 2
