# -*- coding: utf-8 -*-

# flag = False
# name = 'python'
# if name == 'python':
# 	flag = True
# 	print('welcome boss')
# else:
# 	print(name)


# num = 2     
# if num == 3:            # 判断num的值
#     print('boss')        
# elif num == 2:
#     print('user')
# elif num == 1:
#     print('worker')
# elif num < 0:           # 值小于零时输出
#     print('error')
# else:
#     print('roadman')    # 条件均不成立时输出

# num = 9
# if num >= 0 and num <= 10:    # 判断值是否在0~10之间
#     print('hello')

# num = 10
# if num < 0 or num > 10:    # 判断值是否在小于0或大于10
#     print('hello')
# else:
# 	print('undefine')

# num = 8
# #判断值是否在0~5或者10~15之间
# if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
# 	print('hello')
# else:
# 	print('undefine')

# var = 100
# if (var == 100):print('变量var的值为100')
# print('Good bye!')


#while语句
'''
while 判断条件：
    执行语句……
'''
# count = 0
# while (count < 9):
#    print('The count is:', count)
#    count = count + 1

# print("Good bye!")


# continue 和 break 用法
# i = 1
# while i < 10:   
#     i += 1
#     if i%2 > 0:     # 非双数时跳过输出
#         continue
#     print(i)       # 输出双数2、4、6、8、10

# i = 1
# while 1:            # 循环条件为1必定成立
#     print(i)         # 输出1~10
#     i += 1
#     if i > 10:     # 当i大于10时跳出循环
#         break

#while … else 
# count = 0
# while count < 5:
#    print(count, " is  less than 5")
#    count = count + 1
# else:
#    print(count, " is not less than 5")

#简单语句组
# flag = 1
# while (flag): print('Given flag is really true!'); #无限循环
# flag=0;
# print("Good bye!")

# for letter in 'Python':     
#    print('当前字母 :', letter)

# fruits = ['banana', 'apple',  'mango']
# for fruit in fruits:        
#    print('当前水果 :', fruit)

# print("Good bye!")

#序列索引迭代
# fruits = ['banana', 'apple',  'mango']
# for index in range(len(fruits)):
#    print('当前水果 :', fruits[index], index)

# print("Good bye!")

#for...else
# for num in range(10,20):  # 迭代 10 到 20 之间的数字
#    for i in range(2,num): # 根据因子迭代
#       if num%i == 0:      # 确定第一个因子
#          j=num/i          # 计算第二个因子
#          print('%d 等于 %d * %d' % (num,i,j))
#          break            # 跳出当前循环
#    else:                  # 循环的 else 部分
#       print(num, '是一个质数')

#嵌套
# i = 2
# while(i < 100): #循环，判断100以内的素数
#    j = 2
#    while(j <= (i/j)):
#       if not(i%j): break
#       j = j + 1
#    if (j > i/j) : print(i, " 是素数")
#    i = i + 1

# print("Good bye!")

#break语句
# for letter in 'Python':   # for循环的break语句
#    if letter == 'h':
#       break
#    print('Current Letter :', letter)

# var = 10                    
# while var > 0:            # while循环的break语句
#    print('Current variable value :', var)
#    var = var -1
#    if var == 5:
#       break

# print("Good bye!")

#continue语句
# for letter in 'Python':     # 对应break的第一个例子
#    if letter == 'h':
#       continue
#    print('当前字母 :', letter)

# var = 10                    # 对应break的第二个例子
# while var > 0:              
#    var = var -1
#    if var == 5:
#       continue
#    print('当前变量值 :', var)
# print("Good bye!")

#pass语句
# 输出 Python 的每个字母
# for letter in 'Python':
#    if letter == 'h':
#       pass
#       print('这是 pass 块')
#    print('当前字母 :', letter)

# print("Good bye!")

#时间与日期
# import time;  # This is required to include time module.

# ticks = time.time()
# print("Number of ticks since 12:00am, January 1, 1970:", ticks)

# localtime = time.localtime(time.time())
# print("Local current time :", localtime)

# localtime = time.asctime( time.localtime(time.time()) )
# print("Local current time :", localtime)

# import calendar

# cal = calendar.month(2008, 1)
# print("Here is the calendar:")
# print(cal);

#函数调用
# def printme( str ):
#    "打印传入的字符串到标准显示设备上"
#    print(str)
#    return

# #函数调用
# printme("我要调用用户自定义函数!");
# printme("再次调用同一函数");

# 可写函数说明
# def changeme(mylist):
# 	"修改传入的列表"
# 	mylist.append([1,2,3,4]);
# 	print("函数内取值：",mylist)
# 	return

# mylist = [10,20,30];
# changeme(mylist);
# print("函数外取值：",mylist)

#定义函数
# def printinfo( name, age ):
#    "打印任何传入的字符串"
#    print("Name: ", name)
#    print("Age ", age)
#    return;
 
# #调用函数
# printinfo( age=50, name="miki" ); #python内函数参数的位置可以不用对应

# def printinfo( arg1, *vartuple ):
#    "打印任何传入的参数"
#    print("输出: ")
#    print(arg1)
#    for var in vartuple:
#       print(var)
#    return;
 
# # 调用printinfo 函数
# printinfo( 10 );
# printinfo( 70, 60, 50 );

#匿名函数
'''
lambda [arg1 [,arg2,.....argn]]:expression
'''

# sum = lambda arg1, arg2: arg1 + arg2;
# # 调用sum函数
# print("相加后的值为 : ", sum( 10, 20 ))
# print("相加后的值为 : ", sum( 20, 20 ))


# return语句
# def sum( arg1, arg2 ):
#    total = arg1 + arg2
#    print("函数内 : ", total)
#    return total;
 
# 调用sum函数
# total = sum( 10, 20 );
# print("函数外 : ", total)


#变量的作用范围
# total = 0; # 这是一个全局变量
# # 可写函数说明
# def sum( arg1, arg2 ):
#    #返回2个参数的和."
#    total = arg1 + arg2; # total在这里是局部变量.
#    print("函数内是局部变量 : ", total)
#    return total;
 
# #调用sum函数
# sum( 10, 20 );
# print("函数外是全局变量 : ", total)








