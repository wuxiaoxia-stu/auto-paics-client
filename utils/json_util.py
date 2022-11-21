import json
import pytest
import os


class JsonUtil:
    """
    读取json数据
    写入json数据
    """
    path = os.getcwd() + "/data/"

    def write_json(self, filename, data):
        """
        写入json文件
        """
        # filename_path = self.path + filename
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)
            # print(data)

    def read_json(self, filename):
        """
        读取json文件
        """
        filename_path = self.path + filename
        with open(filename_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # print(data)
        return data

    def get_data_json(self, filename, modify_data, key_name):
        """
        值为列表格式的json数据，修改后返回新数据，使用字典保存
        :param filename:
        :param data:
        :return:
        https://blog.csdn.net/buside/article/details/81323871
        """
        dicts = {}
        dicts.setdefault(key_name, [])
        # filename_path = self.path + filename
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f) # 加载json文件中的内容给data
            # data[key_name] = modify_data  #  将key_name的值修改为modify_data
            # print(data)
            # dicts = data  # 将修改后的内容保存在dict中
            dicts.setdefault(key_name, []).append(modify_data)
            # print(dicts)
        f.close() # 关闭文件
        return dicts  # 返回dicts字典内容

    def modify_json(self, filename, modify_data, key_name):
        """
        修改json文件的数据后，写入新数据
        :param filename: 待修改的文件名
        :param modify_data: 修改后的数据
        :param key_name: 修改的字段名
        :return:
        """
        data = self.get_data_json(filename, modify_data, key_name)
        self.write_json(filename, data)
# #
# if __name__ == '__main__':
#         # pytest.main(['-vs'])
#         WriteReadJson().test_modify_json("VideoPathList.json", "连体双胎.flv", "video_path_list")
#


