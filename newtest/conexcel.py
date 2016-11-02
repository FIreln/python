import os
import xlrd

currentdir=os.path.split(os.path.realpath(__file__))[0]#获取当前工作文件夹
print(currentdir+'\case.xlsx')
data = xlrd.open_workbook(currentdir+'\case.xlsx')#打开文档
#获取工作表
table1 = data.sheets()[0] #通过索引顺序获取表
table2 = data.sheet_by_index(0)#通过索引顺序获取表
table3 = data.sheet_by_name(u'Sheet1')#通过名称获取表
#获取整行或整列的值
table2.row_values(0)
table2.col_values(1)
#获取行数和列数
nrow = table2.nrows
ncol = table2.ncols
print(nrow,ncol,table2.row_values(0))
#读取单元格的值
row1 = table2.row(0)[1].value
print(row1)
