import os

# 打印当前目录下全部文件
a = os.listdir('/Project/Test/jichu/')

# 打印当前python进程的工作目录
b = os.getcwd()

# 获得文件各种属性
c = os.stat('filexample.txt')

# 删除多个目录
# d = os.removedirs()

# 执行shell命令
e = os.system('help')

# 拼接路径
# f = os.path.join()

# 创建目录
# g = os.mkdir('test3')

# 返回文件名
h = os.path.basename('/Project/Test/jichu/if.py')


if __name__ == '__main__':
    print(a)
    print(b)
    print(c)
    print(e)
    print(h)