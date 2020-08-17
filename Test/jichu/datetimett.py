import time
from datetime import datetime
from datetime import timedelta

def time_format():
    print(time.time())
    print(time.localtime())
    print(time.gmtime())
    print(time.strftime('%Y/%m/%d : %H %M %S',time.localtime()))
    print(time.strftime('%c'))
    print(time.strptime('1 Jan 2018 1:30pm', '%d %b %Y %I:%M%p'))
    print(time.strptime('2020 07 01','%Y %m %d'))


def datetime_format():
    print(datetime.now())
    print(datetime.utcnow())
    print(datetime.now().strftime('%Y/%m/%d : %H %M %S'))
    print(datetime.strptime('1 Jan 2018 1:30pm', '%d %b %Y %I:%M%p'))


def time_delta():
    d1 = datetime.strptime('2020/08/02 : 15 22 39','%Y/%m/%d : %H %M %S')
    d2 = datetime.strptime('1 Jan 2018 1:30pm', '%d %b %Y %I:%M%p')
    print(d2-d1)

    now = datetime.now()
    after_time = timedelta(days=1)
    print(now)
    print(now+after_time)

    before_time = timedelta(hours=1)
    print(now-before_time)


if __name__ == '__main__':
    time_format()
    print('1'*200)
    datetime_format()
    print('2'*200)
    time_delta()