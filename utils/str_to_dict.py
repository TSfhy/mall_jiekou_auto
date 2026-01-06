import json


class StrToDict:
    @staticmethod
    def str_to_dict(s):

        dict_data = json.loads(s)
        return dict_data