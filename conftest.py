import pytest
import json

# Pytest fixture that runs once before each test in this module
@pytest.fixture(scope='module')
def start_exec():
    file = open("Test Data/test.json")
    req_json = json.loads(file.read())
    file.close()
    return req_json
