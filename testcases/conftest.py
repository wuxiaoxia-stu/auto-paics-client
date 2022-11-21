from utils.config_util import ConfigUtil
# from utils.log_util import LogUtil
from utils.yaml_util import YamlUtil
from utils.json_util import JsonUtil

#基类
class Base:

    @classmethod
    def setup_class(cls):
        cls.paics_path = YamlUtil().read_yaml('config.yaml')[0]['paics_path']  # paics客户端所在路径
        print(cls.paics_path)
        cls.project_path = YamlUtil().read_yaml('config.yaml')[0]['project_path']  # 项目所在路径
        cls.vedio_path = YamlUtil().read_yaml('config.yaml')[0]['vedio_path']  # 测试视频所在路径
        cls.vedio_json_path = YamlUtil().read_yaml('config.yaml')[0]['VideoJsonList_path']  # 测试视频json文件所在路径
        # cls.logger = LogUtil()  # 实例化Log且获取Logger，为了作用于整个项目，所以在此实例化
        cls.my_json = JsonUtil()  # 实例化WriteReadJson类
        cls.my_config = ConfigUtil()  # 实例化ConfigIni()类
    #
    # def base_write_log(self, message, level="info"):
    #     """输出日志"""
    #     self.logger.get_logger()  # 获取Logger日志器
    #     self.logger.write_log(message, level)  # 写日志

    def base_modify_json(self, filename, data, key_name):
        """
        修改json数据
        :return:
        """
        self.my_json.modify_json(filename, data, key_name)

    def base_config(self):
        """
        修改ini文件对应key的值
        :param filename:
        :param value:
        :return:
        """
        self.my_config.modify_config(self.paics_path + 'appconfig.ini', 'DEBUG', 'video_path', self.vedio_json_path)  # 修改配置文件的vedio_json_path的值，避免乱码
        # ConfigIni().config_ini(filename, section_name, key_name, value)  # 修改配置文件的vedio_json_path的值，避免乱码


