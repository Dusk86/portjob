# 封装request
import json
import requests

"""
session与cookie的区别

（1）Cookie以文本文件格式存储在浏览器中，而session存储在服务端它存储了限制数据量。它只允许4kb它没有在cookie中保存多个变量。

（2）cookie的存储限制了数据量，只允许4KB，而session是无限量的

（3）我们可以轻松访问cookie值但是我们无法轻松访问会话值，因此它更安全

（4）设置cookie时间可以使cookie过期。但是使用session-destory（），我们将会销毁会话。

总结：如果我们需要经常登录一个站点时，最好用cookie来保存信息，要不然每次登陆都特别麻烦，
     如果对于需要安全性高的站点以及控制数据的能力时需要用会话效果更佳，当然我们也可以结合两者，使网站按照我们的想法进行运行
"""

class RequestUtil:
    """
    __init__私有函数，只能在该类的内部使用
    init 的本意就是初始化的意思，一般出现在程序创建类中的第一个函数
    使用__init__函数，可以声明一个可以动态变化的参数
    __init__函数在创建类的开始，初始化一些参数，给后续的一些函数调用，而不是规定一个固定的值，使之更加灵活
    构造方法__init__用于创建实例对象时使用，每当创建一个类的实例对象时，Python 解释器都会自动调用它，用来初始化对象的某些属性。
    """
    def __init__(self):
        """
        requests中的session对象能够让我们跨http请求保持某些参数，即让同一个session对象发送的请求头携带某个指定的参数。
        当然，最常见的应用是它可以让cookie保持在后续的一串请求中。
        """
        self.session = requests.session()

    def request(self, url, method, data=None, is_json=False, **kwargs):
        #将请求方式全部大写
        method = method.upper()
        #判断data类型
        if type(data) == str:
            data = eval(data)  # str转成字典
        if method == "GET":
            response = self.session.request(method=method, url=url, params=data, **kwargs)
        elif method == "POST":
            if is_json:  # 请求参数是json格式 application/json
                response = self.session.request(method=method, url=url, json=data, **kwargs)
            else:
                response = self.session.request(method=method, url=url, data=data, **kwargs)
        else:
            response = None
        return response

    # 关闭session会话
    def close_session(self):
        self.session.close()


