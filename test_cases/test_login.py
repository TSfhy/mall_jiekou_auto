import os

import allure
import pytest
import requests

from apis.loginapi import LoginApi
from config import project_url, datas_path
from utils.assert_utils import AssertUtils
from utils.read_utils import ReadUtil
from utils.str_to_dict import StrToDict

file_path = os.path.join(datas_path, "login_datas.xlsx")
sheet_name = "login_data"
datas = ReadUtil.read_excel(file_path, sheet_name)

@allure.feature("登录模块")
@allure.story("登录")
class TestLogin:

    @pytest.mark.parametrize("title,data,status_code,code,msg",datas)
    @allure.title("title")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login(self, title,data,status_code,code,msg,get_log):
        with allure.step("登录操作"):
            data = StrToDict.str_to_dict(data)
            response = LoginApi().login(data)
        with allure.step("断言结果"):
            AssertUtils.assert_result(response,status_code,code,msg)
            print(response.text)
        with allure.step("打印日志"):
            get_log.info(response.text)
