# 输入模块

def inputs(a,zuobiao):
    print("When you want to quit please input quit")
    while (1):
        # input读入数据的类型是str不是int
        rang = input("The rang is:(form 0 to 8)")
        if(rang == 'quit'):
            break
        line = input("The line is:(form 0 to 8)")
        if(line == 'quit'):
            break
        num = input("The number is:(form 1 to 9)")
        if(num == 'quit'):
            break
        rang = int(rang)
        line = int(line)
        num = int(num)


        if (rang >= 0 and rang <= 8 and line >= 0 and line <= 8):
            a[rang][line] = num
            zuobiao +=[[rang,line]]#使用列表记录坐标信息
        else:
            print('error')
