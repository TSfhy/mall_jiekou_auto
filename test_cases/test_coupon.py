import os

import allure
import pytest

from apis.coupon_api import CouponApi
from config import datas_path
from utils.assert_utils import AssertUtils
from utils.read_utils import ReadUtil
from utils.str_to_dict import StrToDict

file_path = os.path.join(datas_path, "login_datas.xlsx")
sheet_name = "coupon_data"
datas = ReadUtil.read_excel(file_path, sheet_name)


@allure.feature("营销工具")
@allure.story("优惠卷列表")
class TestCoupon:


    @pytest.mark.parametrize("title,data,status_code,code,msg",datas)
    @allure.title("{title}")
    @allure.severity(allure.severity_level.NORMAL)
    def test_coupon(self,title,data,status_code,code,msg,login,get_log):
        with allure.step("优惠卷查询"):
            data = StrToDict.str_to_dict(data)
            res = CouponApi().select_coupon(login,data)
        with allure.step("断言结果"):
            AssertUtils.assert_result(res,status_code,code,msg)
            print(res.text)
        with allure.step("打印日志"):
            get_log.info(res.text)
