set1 = {0,1,2,3,4,5}
b=set()
print(type(b))
print(set1)

set2 = {9,8,7,6,5,4}
# set合并后进行去重排序
print(set1.union(set2))

# set取交集
print(set1.intersection(set2))

# set取set1比set2多的差集
print(set1.difference(set2))
# set取set2比set1多的差集
print(set2.difference(set1))

# set取对称差集
print(set1.symmetric_difference(set2))
print(set1.symmetric_difference(set2))