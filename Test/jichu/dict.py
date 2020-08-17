zidian = {"name":"weishihao","age":"18","nannv":"boy"}
a={}
print(type(a))
print(zidian["name"])
print(zidian.keys())
print(zidian.values())
print(zidian.items())

zidian["age"] = "20"
print(zidian)

del zidian["nannv"]
print(zidian)

print(zidian.get("name"))
print('*'*100)



dict_test = {"name":"weishihao","age":"18","nannv":"boy"}
# 遍历字典
for key,value in dict_test.items():
    print(key,':',value)
    assert dict_test[key] == value