import yaml
class YamlUtil:
    # 获取登录token/cookies
    def read_testcase(self, yaml_path, part):
        # os.getcwd()获取当前文件所在目录
        with open(yaml_path, mode="r", encoding="utf-8") as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            new_value = value[part]  # 每个接口选择对应的用例
            return new_value

    # 写入获取到的token值
    def write_token(self, yaml_path, data):
        # os.getcwd()获取当前文件所在目录
        with open(yaml_path, mode="w", encoding="utf-8") as f:
            yaml.dump(data, stream=f, allow_unicode=True)

    # 读取写入的token值
    def read_token(self, yaml_path):
        with open(yaml_path, mode="r", encoding="utf-8") as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value

class Weather:
    # 获取天气信息
    # 需要将yaml文件的名字作为参数进行传递
    def get_weather(self, yaml_path):
        with open(yaml_path, mode="r", encoding="utf-8") as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value

class Usetoken:
    def use_token(self, yaml_path):
        with open(yaml_path, mode="r", encoding="utf-8") as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value

