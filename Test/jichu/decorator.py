import time

def display_time(func):
    def wrapper(*args):
        t1 = time.time()
        # result为prime_nums的count返回值
        result = func(*args)
        t2 = time.time()
        print('time is {:.3} s'.format(t2-t1))
        return result
    return wrapper

def is_prime(num):
    if num%2 == 0:
        return num
    else:
        pass


@display_time
def prime_nums(maxnum):
    count = 0
    for i in range(1,maxnum):
        if is_prime(i):
            count = count + 1
    return count

print(prime_nums(10000))