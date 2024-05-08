import requests
import json
import pytest

'''
Test to validate get request for user data
'''


@pytest.mark.smoke
def test_fetch_user_data():
    url = "https://reqres.in/api/users?page=2"
    res = requests.get(url)
    print("Body of response:", res.content)
    print("Headers of response:", res.headers)
    print("Value for Date Header:", res.headers.get("Date"))
    print("Value of Cookies:", res.cookies)
    print("Value of encoding:", res.encoding)
    print("Value of elapsed time:", res.elapsed)
    # Validate Status code
    print(res.status_code)
    assert res.status_code == 200
    json_res = json.loads(res.text)
    print(json_res)
    # Validate value of page field
    assert json_res['page'] == 2
