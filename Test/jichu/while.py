age = 4
while (age < 7):
    print('小于')
    age = age + 1
print('大于等于')

agess = [1,2,3]

for ages in agess:
    print(ages)
    if ages == 1:
        print('一岁')
    elif ages == 2:
        print('两岁')
    else:
        print('三岁')

for i in range(10):
    print(i)

agess = ['魏','世','豪']
for index in range(len(agess)):
    print(agess[index])
    if index == 0:
        print('第一个是'+agess[index])
    elif index == 1:
        print('第二个是'+agess[index])
    else:
        print('第三个是'+agess[index])

for x in range(1,10):
    for y in range(1,x+1):
        print(x,'*',y,'=',x*y,end='|')
    print('')

a=1
while a <= 5:
    b=1
    while b <= a:
        print('*',end='')
        b+=1
    print('')
    a+=1

age = 0
while age < 7:
    if age > 2:
        print(age,'上学啦')
        break
    print(age,'不上学')
    age+=1

age = 0
while age < 7:
    if age > 2:
        print(age,'上学啦')
        continue
    print(age,'不上学')
    age+=1