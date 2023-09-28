# 封装断言
import json
class Assertutil():
    # 初始化参数
    def __init__(self):
        pass

    # 验证返回的状态码
    def assert_code(self, code, expected_code):
        """
        try except：异常捕获，用于检测try语句中的错误
        Python从 try 子句开始执行，若一切正常，则跳过 except 子句；若发生异常，则跳出 try 子句，执行 except 子句
        """
        try:
            assert int(code) == int(expected_code)
            return True
        except:
            raise

    # 验证返回结果内容相同
    # def assert_body(self, body, expected_body):
    #     try:
    #         assert body == expected_body
    #         return True
    #     except:
    #         self.log.error("body error,body is %s,expected_body is %s" % (body, expected_body))
    #         raise

    # 验证返回结果是否包含期望结果
    def assert_in_body(self, body, expected_body):
        try:
            body = json.dumps(body)
            expected_body = json.dumps(expected_body)
            print(body)
            assert expected_body in body
            return True
        except:
            raise

