class server(object):

    def __init__(self,cpu,mem,disk,system):
        self.cpu = cpu
        self.mem = mem
        self.disk = disk
        self.__system = system

    def geshi(self):
        return '%s核CPU，%sG内存，%sG磁盘空间，%s' % (self.cpu,self.mem,self.disk,self.__system)


if __name__ == '__main__':
    sv = server(8,40,150,'Linux')
    print(sv.geshi())