from jichu.classtest2 import Student,Person

class SeniorStudent(Student):

    def __init__(self,name,sex,province,grade):
        super(SeniorStudent, self).__init__(name,sex,province,grade)
        # Student.__init__(self,name,sex,province,grade)

    def get_grade(self):
        return self.grade

    def over_time(self):
        if self.grade == 3:
            return '补课'
        else:
            return '不补课'

    def get_little_name(self):
        name = Person.get_name(self)
        if name.startswith('y'):
            return 'samll_'+name
        else:
            return name

if __name__ == '__main__':
    ss = SeniorStudent('yanghongtao','nan','shanghai',3)
    print(ss.get_name())
    print(ss.get_grade())
    print(ss.over_time())
    print(ss.get_little_name())