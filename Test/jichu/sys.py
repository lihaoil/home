import sys

# 返回当前pythonpath列表
a = sys.path

# 获取命令行参数
b = sys.argv

# 退出当前pathon进程
# c = sys.exit()

# 获取当前系统
d = sys.platform

# 标准输入流，标准输出流，标准错误流
e = sys.stdin
f = sys.stdout
g = sys.stderr



if __name__ == '__main__':
    print(a)
    print(b)
    print(d)
    print(e)
    print(f)
    print(g)