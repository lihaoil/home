import pytest
import xlrd


def open_file(in_file):
    '''
    打开文件获取数据
    :param in_file:
    :return:
    '''
    data = xlrd.open_workbook(in_file)
    table = data.sheet_by_name('Sheet1')
    name = table.name
    rowNum = table.nrows
    colNum = table.ncols
    print(rowNum)
    print(colNum)

    # 遍历excel数据，存进list
    list = []
    d = {}
    keyName = table.row_values(



    )
    valueName = table.cell(0, 1).value
    for i in range(1,rowNum):
        for j in range(0,colNum):
            d[keyName[i]] = valueName[j]
            print(i,j)
            list.append(table.cell(i,j).value)
    print(list)

if __name__ == '__main__':
    open_file('../first_pytest/data/data1.xlsx')