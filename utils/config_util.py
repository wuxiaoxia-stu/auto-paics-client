from configparser import ConfigParser   # Python2中是from ConfigParser import ConfigParser


class ConfigUtil:

    def __init__(self):
        self.conf = ConfigParser()  # 需要实例化一个ConfigParser对象

    def modify_config(self, filename, section_name, key_name, value):
        """
        读取并修改ini文件
        :return:
        """
        self.conf.read(filename, encoding='utf-8')  # 需要添加上config.ini的路径，不需要open打开，直接给文件路径就读取，也可以指定encoding='utf-8'
        print(self.conf[section_name][key_name])  # 读取DEBUG段的video_path变量的值，字符串格式
        self.conf.set(section_name, key_name, value)  # 可以设置DEBUG段的值
    # 保存ini
        with open(filename, 'w', encoding='utf-8') as f:
            self.conf.write(f)
