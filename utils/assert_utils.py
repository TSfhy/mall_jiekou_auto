class AssertUtils:
    @staticmethod
    def assert_result(res,status_code=None,code=None,msg=None):
        if status_code is not None:
            assert res.status_code == status_code
        if code is not None:
            assert res.json().get("code") == code
        if msg is not None:
            assert msg in res.json().get("message")