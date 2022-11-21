import shutil
import os

# 用于替换指定路径的文件

def copy_file(filename_src, filename_dst):

    if os.path.exists(filename_dst):  # 判断文件是否存在
        os.remove(filename_dst)  # 删除目标文件
    shutil.copyfile(os.getcwd()+'/data/' + filename_src, filename_dst)  # 将文件复制到指定路径



# if __name__ == '__main__':
#     filename_dst = ReadYaml().read_yaml('config.yaml')[0]['paics_path'] + 'appconfig.ini'
#     CopyFile().copy_file('appconfig.ini', filename_dst)
