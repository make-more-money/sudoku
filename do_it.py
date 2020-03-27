'''
测试成功
but have a limition: must open the .xlsx when running the .py
another error: every cells must have a value ''!= None"
'''
import openpyxl
book = openpyxl.load_workbook('mmp.xlsx')
sheet = book.active
cells = sheet['A1': 'I9']
for c1, c2, c3, c4, c5, c6, c7, c8, c9 in cells:
    # format to have a nice and net output
    print("{0:10} {1:10} {2:10} {3:10} {4:10} {5:10} {6:10} {7:10} {8:10}".format(
        c1.value, c2.value, c3.value, c4.value, c5.value, c6.value, c7.value, c8.value, c9.value))
