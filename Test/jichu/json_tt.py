import json

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
# 将Python对象编码成JSON字符串
print(json.dumps(data))
print(type(json.dumps(data)))

jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
# 将已编码的JSON字符串解码为Python对象
print(json.loads(jsonData))
print(type(json.loads(jsonData)))