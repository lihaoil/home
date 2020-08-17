from jichu.logger_tt import log

def exception_example(x,y):
    try:
        result = x/y
    except Exception as e:
        print(e)
    else:
        print(result)
    finally:
        print('计算结束')
exception_example(10,2)


def read_file(in_file):
    try:
        fe = open(in_file, 'r')
    except Exception as e:
        print(e)
        # 返回错误日志到jichu.logger_test的log方法
        return log(e)
read_file('../user_info1.txt')


def student(name,sex,age=7):
    '''
    传参练习
    :return:
    '''
    return name+sex+str(age)
print(student('张三','男'))
print(student(name='李四',sex='女',age=18))

def test(test1,test2,*test3,**test4):
    print(test3)
    print(test4)
test(1,2,3,4,haha=1,aia=2)

def add(x,**dicts):
    diyi = x
    print(dicts)
    for key,value in dicts.items():
        print(key)
        x += value
    return x

print(add(1,qq=2,ww=3,tt=4))

lama = lambda x,y : x+y
print(lama(2,3))