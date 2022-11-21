#!usr/bin.env/ python3

import os
import yaml


class YamlUtil:

    def read_yaml(self, filename):
        """
        读取yaml文件
        """
        with open(os.getcwd()+'/data/'+ filename, 'r', encoding='utf-8') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            # print(data)
        return data

# if __name__ == '__main__':
#     data = ReadYaml().read_yaml('config.yaml')[0]['paics_path']
#     print(data)
