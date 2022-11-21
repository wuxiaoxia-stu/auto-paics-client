from utils.config_util import ConfigUtil
from utils.csv_util import CsvUtil
from utils.log_util import LogUtil
from utils.yaml_util import YamlUtil
from utils.json_util import JsonUtil
from utils.keys_util import KeysUtil


#基类
class Base:

    log_util = LogUtil()   # 实例化LogUtil()类
    yaml_util = YamlUtil()  # 实例化ReadYaml()类
    config_util = ConfigUtil()  # 实例化ConfigIni()类
    json_util = JsonUtil()  # 实例化WriteReadJson()类
    csv_util = CsvUtil()   # 实例化ReadCsv()类
    keys_util = KeysUtil()  # 实例化ReadCsv()类
    paics_path = yaml_util.read_yaml('config.yaml')[0]['paics_path']  # paics客户端所在路径
    project_path = yaml_util.read_yaml('config.yaml')[0]['project_path']  # 项目所在路径
    video_path = yaml_util.read_yaml('config.yaml')[0]['video_path']  # 测试视频所在路径
    video_json_path = yaml_util.read_yaml('config.yaml')[0]['videoJsonList_path']  # 测试视频json文件所在路径
    video_name = yaml_util.read_yaml('config.yaml')[0]['col1_name']  # 测试csv文件的第一个表头名
    video_length = yaml_util.read_yaml('config.yaml')[0]['col2_name']  # 测试csv文件的第2个表头名

    def base_modify_json(self, filename, data, key_name):
        """
        修改json数据
        :param filename: 文件名
        :param data: 数据
        :param key_name: 字段名
        :return:
        """
        self.json_util.modify_json(filename, data, key_name)

    def base_config(self, filename, section_name, key_name, value):
        """
        修改ini文件对应key的值
        :param section_name: 需要修改的section名
        :param key_name: 需要修改的字段名
        :param filename: ini文件名
        :param value: 修改后的值
        :return:
        """
        self.config_util.modify_config(filename, section_name, key_name, value)  # 修改配置文件的video_json_path的值，避免乱码

    def base_write_log(self, message, level):
        """输出日志
        :param message: 日志信息
        :param level: info，debug，info，warning，error，critical
        """
        self.log_util.write_log(message, level)

