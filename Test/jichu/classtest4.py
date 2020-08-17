class ren(object):

    def __init__(self,name,sex,height):
        self.name = name
        self._sex = sex
        self.__height = height

    def get_name(self):
        return self.name

    def get_sex(self):
        return self._sex

    def get_height(self):
        return self.__height


if __name__ == '__main__':
    ren1 = ren('laji','nan',180)
    print(ren1.name)
    print(ren1._sex)
    print(ren1.__height)#获取不到私有属性
    print('*'*100)

    print(ren1.get_name())
    print(ren1.get_sex())
    print(ren1.get_height())
