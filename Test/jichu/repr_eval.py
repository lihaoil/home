from collections import Counter

a = {'name':'wsh','age':18}
# 将对象转化为字符串
str_b = repr(a)
print(str_b[0:3])


b = '[1,2,3,4]'
# 将字符串转化为python对象
str_b = eval(b)
print(str_b[1])


# list(reversed)用于对象反转
seqTuple = ('H', 'e', 'l', 'l', 'o') # 元组
print(list(reversed(seqTuple)))
seqList = [7, 8, 4, 5, 6]  # 列表
print(list(reversed(seqList)))
seqString = 'HelloWorld' # 字符串
print(list(reversed(seqString)))
seqRange = range(1, 8)    # range
print(list(reversed(seqRange)))

# 拆分字符串，返回list
print(sorted('123456'))
# 重新排序list
print(sorted([1,4,5,2,3,6]))
# 重新排序list，并倒序展示
print(sorted([1,4,5,2,3,6],reverse=True))
# 对字典排序，只取key值排序
print(sorted({1:'q',3:'c',2:'g'}))
# 对字典排序，只取value值排序
print(sorted({1:'q',3:'c',2:'g'}.values()))
# 对字典排序，返回元组嵌套list内
print(sorted({1:'q',3:'c',2:'g'}.items()))

# 按照元素的某一部重新进行排序，key用来自定义排序关键字
s = ['Chr1-10.txt','Chr1-1.txt','Chr1-2.txt','Chr1-14.txt','Chr1-3.txt','Chr1-20.txt','Chr1-5.txt']
print(sorted(s, key=lambda d : int(d.split('-')[-1].split('.')[0]),reverse=True))

# list.sort()只能用于list，并且只会针对原有list排序，不会产生新的list
ss = ['Chr1-10.txt','Chr1-1.txt','Chr1-2.txt','Chr1-14.txt','Chr1-3.txt','Chr1-20.txt','Chr1-5.txt']
list.sort(ss)
print(ss)

list_count = [1,2,3,4,5,6,7,8,34,5,6,7,23,2]
# 统计list每个元素出现的次数，并整理成字典展示
counter = Counter(list_count)
print(counter)
# 将整理后的字典转为list套元组
print(counter.most_common())

# 移除list最后一位，返回该值
print(list_count.pop())
print(list_count)