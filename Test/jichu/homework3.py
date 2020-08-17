from jichu.homework2 import server

class serverzi(server):

    def __init__(self,cpu,mem,disk,system):
        super(serverzi, self).__init__(cpu,mem,disk,system)

    def price(self):
        p = (self.cpu)*1527.679+(self.mem)*100.21+(self.disk)*50.789
        return '最终价格为：{}'.format(round(p,2))


if __name__ == '__main__':
    sz = serverzi(8,40,150,'Linux')
    print(sz.price())