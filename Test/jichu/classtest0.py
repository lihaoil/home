class Person(object):
    total_person = 0
    def __init__(self,name,sex,province):
        print('init the class')
        self.name = name
        self.sex = sex
        self.province = province
        Person.total_person += 1

    def get_name(self):
        return self.name

    def get_sex(self):
        return self.sex

    @staticmethod
    def get_new_name(new_name):
        return '静态方法'+new_name

    @classmethod
    def get_new_sex(cls,aa,bb,cc):
        return '类方法'+aa+bb+cc

    @property
    def get_new_province(self):
        return '属性方法'+self.name

if __name__ == '__main__':
    person1 = Person('weishihao','nan','beijing')
    print(person1.name)
    print(person1.sex)
    print(person1.province)
    print(person1.get_name())
    print(person1.get_sex())
    print(person1.total_person)
    print('1' * 100)

    person2 = Person('张三','nan','haerbin')
    print(person2.sex)
    print(person2.total_person)
    print('2' * 100)

    person3 = Person('李四', 'nv', 'haerbin')
    print(Person.get_new_name('测试'))
    print(person3.get_new_name('test'))
    print('3' * 100)

    person4 = Person('王五', 'nv', 'haerbin')
    print(Person.get_new_sex('l','ll','lll'))
    print(person4.get_new_sex('k','kk','kkk'))
    print('4' * 100)

    person5 = Person('老六', 'nv', 'haerbin')
    print(Person.get_new_province)
    print(person5.get_new_province)