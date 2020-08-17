from shutil import make_archive

def yasuobao():
    # 压缩包名称
    yaosuobao_name = 'jichu'
    # 需要进行压缩的地址或者文件
    address = '../lianxi'
    # 进行压缩，gztar为压缩格式
    make_archive(yaosuobao_name,'gztar',address)


if __name__ == '__main__':
    yasuobao()