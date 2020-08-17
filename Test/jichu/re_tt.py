import re

# 正则表达式对象
pattern = re.compile('asd')
# 在整个字符串中进行匹配
search = pattern.search('asdfghjhkasdfghjhk')
print(search)
if search:
    print('result:',search.group())
# 从字符串头开始匹配
match = pattern.match('asdfghjhkasdfghjhk')
print(match)
if match:
    print('result:',match.group())

all = re.compile('\d')
# 匹配全部返回列表
findall = all.findall('23gadsy324h546h6l')
print(findall)