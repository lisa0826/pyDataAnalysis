# -*- coding: utf-8 -*-
#1. 编写函数，要求输入x与y，返回x和y的平方差
def squarefeet( arg1, arg2 ):
   # 返回2个参数的和."
   res = arg1 ** 2 - arg2 ** 2
   return res;
 
# 调用平方差函数
res = squarefeet( 5, 8 );
print("平方差 : ", res)


#2. 计算1到100的平方的和
i = 1
sumVal = 0
while (i<=100):
	sumVal += i ** 2
	i += 1
print(sumVal)


#3. 编写函数，若输入为小于100的数，返回TRUE，大于100的数，返回FALSE
def numJudge():
	str = input("please enter number:");#2.X用raw_input,3.X用input
	i = int(str)
	if(i<100):
		return True
	return False;

print(numJudge())


#4. 某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下： 每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。编写加密的函数与解密的函数。