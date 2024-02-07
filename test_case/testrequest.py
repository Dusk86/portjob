import json
import re
import requests
import pytest
import allure
import logging
from common.api_requests import RequestUtil
from common.yaml_util import YamlUtil
from common.yaml_util import Weather
from common.my_excel import MyExcel
from common.assert_util import Assertutil

"""
一般实际项目开发中都会使用requirements.txt文件保存插件名
通过：pip install -r requirements.txt 安装所有插件
"""

# log日志打印
logger = logging.getLogger()


# format()/f-string格式化字符串
# @allure.feature("获取鉴权码") 功能名称，放在类名前面。 二级目录
@allure.feature("接口测试用例")
@allure.testcase("LoginTest/test_case/testrequest.py", "测试用例地址")
@allure.issue("", "bug地址")
@allure.link("", "链接地址")
class TestSendRequest:
    logger.debug("获取token值")
    @pytest.mark.parametrize("casein", YamlUtil().read_testcase('E:/LoginTest/data/get_token.yml', 'gettoken'))
    # @allure.story("") 子功能名称，放在用例前面。 三级目录
    @allure.story("获取token")
    @allure.title("获取token值")
    @allure.description("用来描述test_gettoken这条case")
    @allure.step("测试步骤，在函数外部使用")
    def test_gettoken(self, casein):
        # with allure.step("获取路径"):  测试过程中的每个步骤,可以放在测试用例方法里面。在函数内部使用
        with allure.step("请求地址：{}".format(casein['request']['url'])):
            url = casein['request']['url']
            logger.debug(f"请求地址=====》{url}")
        with allure.step("请求方式：{}".format(casein['request']['method'])):
            method = casein['request']['method']
            logger.debug(f"请求方式=====》{method}")
        # data 里面是参数，字典类型，键值对
        with allure.step("获取具体数据：{}".format(casein['request']['data'])):
            data = casein['request']['data']
            logger.debug(f"请求参数=====》{data}")
        with allure.step("返回的token值：{}".format(RequestUtil().request(url, method, data).json()['access_token'])):
            # 请求返回的断言
            assert_info = RequestUtil().request(url, method, data).json()['expires_in']
            token = RequestUtil().request(url, method, data).json()['access_token']
            logger.debug(f"返回token值=====》{token}")
        # 期望的断言
        assert_expected =casein['validate']['eq']['expires_in']
        # # 断言判断
        Assertutil().assert_in_body(assert_info, assert_expected)
        # 将token写入yaml
        YamlUtil().write_token('E:/LoginTest/data/save_token.yml', token)

    # 使用获取的token
    logger.debug("使用获取的token值")
    @pytest.mark.parametrize("usetoken", YamlUtil().read_testcase('E:/LoginTest/data/get_token.yml', 'usetoken'))
    @allure.story("使用取到的token")
    @allure.title("使用获取到的token值")
    def test_usetoken(self, usetoken):
        print(usetoken)
        # 读取token
        logger.debug("读取存入的token")
        read_token = YamlUtil().read_token('E:/LoginTest/data/save_token.yml')
        logger.debug(read_token)
        logger.debug("获取请求地址")
        with allure.step('请求地址：{}'.format(usetoken['request']['url'] + 'read_token')):
            url = usetoken['request']['url'] + read_token
            logger.debug(url)
        logger.debug("请求方法")
        with allure.step(f"请求方法：{usetoken['request']['method']}"):
            method = usetoken['request']['method']
            logger.debug(method)
        logger.debug("请求数据")
        data = usetoken['request']['data']['tag']
        logger.debug(data)
        logger.debug("获取返回值")
        with allure.step(f'返回值：{RequestUtil().request(url, method, data)}'):
            rsp = RequestUtil().request(url, method, data)
            logger.debug(rsp)

    # 获取天气信息
    logger.debug("查询城市天气")
    @pytest.mark.parametrize("weatherinfo", Weather().get_weather('E:/LoginTest/data/weather.yml'))
    @allure.story("查询天气信息")
    @allure.title("获取城市的天气预报")
    def test_getweather(self, weatherinfo):
        logger.debug("请求地址")
        with allure.step('请求地址：{}'.format(weatherinfo['request']['url'])):
            url = weatherinfo['request']['url']
            logger.debug(url)
        logger.debug("请求方式")
        with allure.step('请求方式：{}'.format(weatherinfo['request']['method'])):
            method = weatherinfo['request']['method']
            logger.debug(method)
        with allure.step('查询城市：{}'.format(weatherinfo['request']['data']['city'])):
            logger.debug(f"查询 {weatherinfo['request']['data']['city']} 天气预报")
        logger.debug("获取 id/密钥/城市")
        data = weatherinfo['request']['data']
        logger.debug(data)
        with allure.step('查询结果：{}'.format(RequestUtil().request(url, method, data).json())):
            logger.debug(f"{weatherinfo['request']['data']['city']}'天气预报'：{RequestUtil().request(url, method, data).json()}")

    # 获取cookies
    logger.debug("获取cookies值")
    @pytest.mark.parametrize("cookiesinfo", YamlUtil().read_testcase('E:/LoginTest/data/get_token.yml', 'getcookie'))
    @allure.story("获取cookies值")
    @allure.title("获取cookies值")
    def test_getcookies(self, cookiesinfo):
        # print(cookiesinfo)
        logger.debug("请求地址")
        with allure.step(f"请求地址：{cookiesinfo['request']['url']}"):
            url = cookiesinfo['request']['url']
            logger.debug(url)
        logger.debug("请求方式")
        with allure.step(f"请求方法：{cookiesinfo['request']['method']}"):
            method = cookiesinfo['request']['method']
            logger.debug(method)
        res = RequestUtil().request(url, method).text
        # print(res)
        logger.debug("获取 csrf_token 值")
        # 正则表达式获取csrf_token
        # re.search()：匹配整个字符串，并返回第一个成功的匹配。如果匹配失败，则返回None
        value = re.search('name="csrf_token" value="(.+?)"', res).group(1)
        logger.debug(value)
        with allure.step(f"获取csrf_token值：{value}"):
            pass

    # 读取excel表格数据
    @pytest.mark.parametrize('readinfo', MyExcel().read_excel_sheet('E:/LoginTest/data/test_api.xls', 'Sheet1'))
    @allure.story("读取excel表格数据")
    @allure.title("读取excel表格数据")
    def test_getexcel(self, readinfo):
        print(readinfo)
        logger.debug("请求地址")
        with allure.step(f"请求地址：{readinfo[3]}"):
            url = readinfo[3]
            logger.debug(url)
        logger.debug("请求方式")
        with allure.step(f"请求方式：{readinfo[2]}"):
            method = readinfo[2]
            logger.debug(method)
        logger.debug("请求头")
        with allure.step(f"请求头：{readinfo[4]}"):
            headers = readinfo[4]
            logger.debug(headers)
        logger.debug("请求参数")
        # eval()函数就是实现list、dict、tuple、与str之间的转化
        # 用eval（）函数可以去掉外面的双引号，直接用内部的值
        data = readinfo[5]
        logger.debug(data)
        logger.debug("获取access_token")
        with allure.step(f"access_token：{RequestUtil().request(url, method, data).json()}"):
            access_token = RequestUtil().request(url, method, data).json()
        logger.debug(access_token)



















