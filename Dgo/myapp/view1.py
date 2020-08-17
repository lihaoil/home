from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
import xlrd
import time
import os
import sys

# filename = "data.xlsx"
# filePath = os.path.join(os.getcwd(), filename)
#
# print(filePath)
#
# x1 = xlrd.open_workbook("data.xlsx")
#
# # 获取所有sheet名字
# print('sheet_names:', x1.sheet_names())
# # 获取所有sheet名字
# print('sheet_number:', x1.nsheets)
# # 获取所有sheet对象
# print('sheet_object:', x1.sheets())
# # 通过sheet名查找
# print('By_name:', x1.sheet_by_name("第一页"))
# # 通过索引查找
# print('By_index:', x1.sheet_by_index(2))
