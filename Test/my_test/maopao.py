import pytest


# 冒泡排序
def maopao(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

print(maopao(list = [1,5,22,34,67,189]))