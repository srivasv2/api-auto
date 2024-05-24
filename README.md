This Readme document describes setup and execution of Pytest driven API tests for https://reqres.in/ , which is a hosted site to test API requests. 

Setup:
1. You need to download and install latest version of Python on your system. Please visit https://www.python.org/downloads/ to get executables for your respective platforms. 
2. Set path to your Python executable in PATH environment variable, so you can execute it from anywhere on your command line.
3. Run following commands to install required python modules for running the tests.
  pip install pytest
  pip install requests
  pip install jsonpath

Execution:
1. Clone test repository using https://github.com/srivasv2/api-auto.git in your local machine.
2. From your direcotry run your tests from command line or IDE like PyCharm/Visual Studio Code using following command.
   pytest -s -v -k test 

Note: If tests don't run saying pytest package is not present. You can alternatively try to run using following command.

python -m pytest -s -v -k test
