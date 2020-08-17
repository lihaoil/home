import paramiko
import re
import time

class GetLinuxLog():
    '''获取Linux服务器日志'''
    def __init__(self,hostname,port,username,password,cmds):
        '''
        :param hostname: linux服务器主机IP
        :param port: linux服务器端口
        :param username: linux服务器用户名
        :param password: linux服务器密码
        :param cmds: linux服务器命令
        '''
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.cmds = cmds
        try:
            # 实例化客户端
            self.client = paramiko.SSHClient()
            # 保存服务器的主机名和密钥信息
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # 连接服务端，进行身份验证
            self.client.connect(self.hostname, self.port, self.username, self.password, timeout=10)
            print('连接成功。。。')
        except Exception as e:
            print('连接失败，错误是{}'.format(e))


    def excute_command(self):
        '''执行命令'''
        try:
            # todo stdin是标准输入文件，stdout是标准输出文件，stderr标准出错文件，应用在输出的重新定位上。
            self.stdin, self.stdout, self.stderr = self.client.exec_command(self.cmds,get_pty=True)
            # 执行命令的全部结果
            self.all_log = self.stdout.read().decode()
            # 根据正则进行信息匹配
            # content = re.compile(r'((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}')
            # self.result = content.search(all).group()
            return self.all_log
        except Exception as e:
            print('返回命令发生异常，内容为{}'.format(e))
        # finally:
        #     # 关闭
        #     self.client.close()


    def write_log(self,in_file):
        '''存入log'''
        try:
            file_log = open(in_file,'a',encoding='utf-8')
            file_log.write('\n'+self.all_log)
        except Exception as e:
            print('写入文件失败，原因为{}'.format(e))
        finally:
            file_log.flush()
            time.sleep(5)
            file_log.close()


    def __del__(self):
        self.client.close()
        print('关闭连接。。。')


if __name__ == '__main__':
    linux = GetLinuxLog('10.220.20.205',22,'root','1q2w3e4r','ifconfig')
    print(linux.excute_command())
    linux.write_log('linux_log.txt')