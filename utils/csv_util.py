import csv
import os


# 用于读取csv格式的数据文件，返回数组列表，数组的元素是字典格式
class CsvUtil:

    def read_csv(self, filename, video_name, video_length):
        """
        用于读取csv格式的数据文件，返回数组列表，数组的元素是字典格式
        1、路径，如果是执行run文件，filename路径为os.getcwd() + "/data/" + filename
        2、如果是单独执行某个test.py文件，路径为"../../data/" + filename
        :param args: 表头名，目前仅能支持2个参数
        :param filename: 文件名
        """
        # print(os.getcwd())
        vedio_list = []  # 定义空数组
        with open(os.getcwd() + "/data/" + filename, 'r', encoding='utf-8') as f:
            data = csv.DictReader(f)  # 以字典格式读取，第一行作为key
            for row in data:
                vedio_list.append([row[video_name], row[video_length]])   # 追加数组元素
            return vedio_list
        # print('list:', vedio_list)
        #
        # vedio_list1 = []
        # with open(os.getcwd() + "../../data/" + filename, 'r', encoding='utf-8') as f:
        #     data = csv.DictReader(f)
        #     for row in data:
        #         # vedio_list1.append([row[args[0]], row[args[1]]])
        #         for arg in args:
        #             vedio_list1.append([row[arg]],)
        # print('list1:', vedio_list1)



# if __name__ == '__main__':
#     # ReadCsv().get_object_path()
#     CsvUtil().read_csv('demo.csv', 'vedio_name', 'vedio_length')
