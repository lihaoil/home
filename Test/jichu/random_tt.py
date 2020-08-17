import random

# 随机整数
print(random.randint(1,20))
# 随机浮点数
print(random.uniform(1,20))

list = ['physics', 'chemistry', 1997, 2000]
# 随机获得元素
print(random.choice(list))
# 随机获得几个元素，组成list
print(random.sample(list,2))
# 打乱list元素顺序
random.shuffle(list)
print(list)