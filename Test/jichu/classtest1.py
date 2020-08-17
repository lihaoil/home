class Per(object):

    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name

if __name__ == '__main__':
    Per1 = Per()
    Per1.set_name('wei')
    print(Per1.get_name())