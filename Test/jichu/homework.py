list = []
for i in range(1000,2500):
    if i%5==0 and i%7==0:
        list.append(i)
print(list)

for i in range(0,21):
    if i%3==0 and i%5==0:
        print(i,   'three+five')
        continue
    elif i%3==0:
        print(i,   'three')
    elif i%5==0:
        print(i,   'five')
    else:
        pass

def f(x):
    p = 0
    for i in x:
        if type(i) == int:
            p += i
        else:
            pass
    print(p)

dicc = {'name':'xiaohao', 'sex':'male'}
def print_error(x):
    try:
        print(x['garde'])
    except Exception as e:
        print(e)
    finally:
        pass
print_error(dicc)