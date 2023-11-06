# run_tests.py
import pytest

if __name__ == '__main__':
    pytest.main(["-v", "test_petstore.py", "--alluredir=allure-results"])
