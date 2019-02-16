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
NUMDATA = 0
def numinput():
    global NUMDATA
    str = input("please enter number:");
    NUMDATA = int(str)
    v1 = encode(NUMDATA)
    print(v1)
     
    v2 = decode(v1)
    print(v2)

def encode(numData):   
    numStr = str(numData)
    i1 = numStr[0]
    i2 = numStr[1]
    i3 = numStr[2]
    i4 = numStr[3]
    
    str1 = divmod((int(i4) + 5),10)[1]
    str2 = divmod((int(i3) + 5),10)[1]
    str3 = divmod((int(i2) + 5),10)[1]
    str4 = divmod((int(i1) + 5),10)[1]
 
    res = str(str1)+str(str2)+str(str3)+str(str4)
    return int(res)
    
def decode(numData):
    numStr = str(numData)
    i1 = numStr[0]
    i2 = numStr[1]
    i3 = numStr[2]
    i4 = numStr[3]
    
    str1 = trans(i4)
    str2 = trans(i3)
    str3 = trans(i2)
    str4 = trans(i1)
    
    res = str(str1)+str(str2)+str(str3)+str(str4)
    return int(res)
    
def trans(i):
    num = int(i)
    if (num >= 5):
       return num - 5
    if (num < 5):
       return num + 10 - 5

numinput()


