import requests


class CouponApi:

    @classmethod
    def select_coupon(cls,token,coupon_data):
        url = "https://admin-api.macrozheng.com/coupon/list"
        res = requests.get(url,coupon_data,headers={"Authorization": "Bearer "+token})
        return res