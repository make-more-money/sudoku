import openpyxl
print("Please input the same number in the same site", end=' ')
print("When the sites is unknown then input 0")
sudokus = [[0] * 9 for _ in range(9)]  # 每个为  sudokus[row][lis]

# 打开工作薄
wb = openpyxl.load_workbook('E://python//edit//program//mmp.xlsx')
# 选择表单
sh = wb['Sheet1']
# 便利列表寻找未能按要求输入的值并报错
for i in range(0, 9):
    for j in range(0, 9):
        sudokus[i][j] = sh.cell((i + 1), (j + 1)).value
        if (int(sudokus[i][j]) >= 0 and int(sudokus[i][j]) <= 9):
            pass
        else:  # 报错
            print("The cell in " + str(i+1)+","+str(j+1)+" error.", end=' ')
            print("Please input number bigger than 0 and less than 9")
wb.close()
