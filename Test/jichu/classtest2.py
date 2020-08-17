from jichu.classtest0 import Person

class Student(Person):

    def __init__(self,name,sex,province,grade):
        super(Student, self).__init__(name,sex,province)
        self.grade = grade

    def get_grade(self):
        return self.grade

    def get_name(self):
        return '1111'

    def get_little_name(self):
        name = Person.get_name(self)
        if name.startswith('q'):
            return 'samll_'+name
        else:
            return name

if __name__ == '__main__':
    student1 = Student('qirui','nv','qingdao',2)
    print(student1.grade)
    print(student1.total_person)
    print(student1.get_name())
    print(student1.get_little_name())