import requests


class LoginApi:

    @classmethod
    def login(cls,login_data):
        login_url = "https://admin-api.macrozheng.com/admin/login"
        res = requests.post(login_url,json=login_data)
        return res
