import pytest

from apis.loginapi import LoginApi
from utils.log_util import LogUtil


@pytest.fixture(scope="function")
def login():
    data = {"username": "admin", "password": "macro123"}
    res = LoginApi().login(data)
    yield res.json().get("data").get("token")

@pytest.fixture(scope="class")
def get_log():
    logger = LogUtil.get_logger()
    yield logger

