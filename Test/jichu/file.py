import time

def open_file_all(in_file):
    '''
    打开全部文件
    :param in_file:
    :return:
    '''
    of = open(in_file,'r',encoding='utf-8')
    all_file = of.read()
    of.close()
    print(all_file)

def open_file_hang(in_file):
    '''
    打开一行文件
    :param in_file:
    :return:
    '''
    of = open(in_file,'r',encoding='utf-8')
    file_line = of.readline()
    of.close()
    print(file_line)

def open_file_list_hang(in_file):
    '''
    打开全部文件，并把内容按照每行存入list
    :param in_file:
    :return:
    '''
    of = open(in_file,'r',encoding='utf-8')
    file_list = of.readlines()
    of.close()
    print(file_list)

def write_file(in_file):
    '''
    a为补充文件，w为重写文件
    write为写入内容，writelines将list按行写入文件
    :param in_file:
    :return:
    '''
    of = open(in_file,'a',encoding='utf-8')
    of.write('\n'+'test1')
    of.writelines(['\n'+'test2','\n'+'tes3'])
    print(1)
    # 将缓冲区的数据立刻写入文件，不用等待关闭时写入
    of.flush()
    time.sleep(10)
    of.close()

if __name__ == '__main__':
    open_file_all('filexample.txt')
    print('1'*100)
    open_file_hang('filexample.txt')
    print('2'*100)
    open_file_list_hang('filexample.txt')
    print('3'*100)
    write_file('filexample.txt')