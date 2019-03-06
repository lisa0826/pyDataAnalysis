# -*- coding: utf-8 -*-


# print "Hello, Python!"; #报错：SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Hello, Python!")? 原因：我们用的python3.X,这是以前旧版本的写法，所以会报错，正确如下
# print('Hello, Python!')

#行和缩进
# if True:
# 	print('True')
# else:
# 	print('False')


#多行语句
item_one = 1
item_two = 2
item_three = 3
total = item_one + \
		item_two + \
		item_three
# print(total)

days = ['Monday','Tuesday','Wednesday','Thursday','Friday']
# print(days)

#引号
word = 'word'
sentence = '这是一个句子'
paragraph = """这是一个段落，
包含了多个语句"""
# print(word)
# print(sentence)
# print(paragraph)

#空行
# input('\n\nPress the enter key to exit.') # For Python 3.x, use input(). For Python 2.x, use raw_input().

import sys;
x = 'foo';
# sys.stdout.write(x + '\n')

#帮助
# help(sys.stdout.write)

#变量赋值
counter = 100 #赋值整型变量
miles = 1000.0 #浮点型
name = 'John' #字符串

# print(counter)
# print(miles)
# print(name)

a = b = c = 1
# print(a,b,c)
a,b,c = 1,2,'John'
# print(a,b,c)

#del var1[,var2[,var3[....,varN]]]]
var=5896419821
var_a=0.22
var_b=3e2
# print(var,var_a,var_b)
del var
del var_a, var_b
# print(var) # 报错：NameError: name 'var' is not defined 原因：数据已经被删除，所以会找不到报错

#字符串
#s="a1a2•••an"(n>=0)
s = 'ilovepython'
# print(s[1:5])
# print(s[5:-1])

str = 'Hello World!'
# print(str) # 输出完整字符串
# print(str[0]) # 输出字符串中的第一个字符
# print(str[2:5]) # 输出字符串中第三个至第五个之间的字符串
# print(str[2:]) # 输出从第三个字符开始的字符串
# print(str * 2) # 输出字符串两次
# print(str + "TEST") # 输出连接的字符串


#列表
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

# print(list) # 输出完整元组
# print(list[0]) # 输出元组的第一个元素
# print(list[1:3]) # 输出第二个至第三个的元素
# print(list[2:]) # 输出从第三个开始至列表末尾的所有元素
# print(tinylist * 2) # 输出元组两次
# print(list + tinylist) # 打印组合的元组

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
# tuple[2] = 1000 # 报错：TypeError: 'tuple' object does not support item assignment 原因：元组中是非法应用,元组中的数据不可改变
# list[2] = 1000 # 列表中是合法应用，列表可以更改
# print(tuple)
# print(list)


#元字典
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print(dict['one']) # 输出键为'one' 的值
print(dict[2]) # 输出键为 2 的值
print(tinydict) # 输出完整的字典
print(tinydict.keys()) # 输出所有键
print(tinydict.values()) # 输出所有值
