# -*- coding: utf-8 -*-
# @Date    : 2019/3/30
# @Time    : 20:09
# @Author  : Daishijun
# @File    : calculator.py
# Software : PyCharm
# import re
# import sys
#
# # 将输入的字符串格式统一转换成列表,将数字、符号、括号都成一个独立元素，
# # 如: 12+3*(14+5)  ----> ["12","+","3","*","(","14","+","5",")"]
# def format_input(input_re_value):
#     input_re_value = input_re_value.replace(" ", "")     #去掉输入的空格
#     input_re_value = re.split(r'(\D)', input_re_value)
#     while True:
#         if "" in input_re_value:
#           input_re_value.remove("")     #将列表中""去掉
#         else:
#             break
#
#     return input_re_value
#
#
# # 计算没有括号的列表的值。加减乘除
# def comput(re_value):
#     while "*" in re_value or "/" in re_value:
#         for i, j in enumerate(re_value):
#             if j == "*":
#                 re_cheng = int(re_value[i - 1]) * int(re_value[i + 1])
#                 re_value.pop(i - 1)
#                 re_value.pop(i - 1)
#                 re_value.pop(i - 1)
#                 re_value.insert(i - 1, re_cheng)
#                 break
#
#             if j == "/":
#                 re_chu = int(re_value[i - 1]) / int(re_value[i + 1])
#                 re_chu = int(re_chu)
#                 re_value.pop(i - 1)
#                 re_value.pop(i - 1)
#                 re_value.pop(i - 1)
#                 re_value.insert(i - 1, re_chu)
#                 break
#     while "+" in re_value or "-" in re_value:
#         for i, j in enumerate(re_value):
#             if j == "+":
#                 re_jia = int(re_value[i - 1]) + int(re_value[i + 1])
#                 re_value.pop(i - 1)
#                 re_value.pop(i - 1)
#                 re_value.pop(i - 1)
#                 re_value.insert(i - 1, re_jia)
#                 break
#
#             if j == "-":
#                 re_jian = int(re_value[i - 1]) - int(re_value[i + 1])
#                 re_value.pop(i - 1)
#                 re_value.pop(i - 1)
#                 re_value.pop(i - 1)
#                 re_value.insert(i - 1, re_jian)
#                 break
#     return re_value[0]
#
#
# def bracket(input_str):
#     if not re.search(r'\(([^()]+)\)', input_str):    #若没有括号
#         s = format_input(input_str)
#         return comput(s)
#     else:      #有括号
#         li = re.split(r'\(([^()]+)\)', input_str)
#         data = re.search(r'\(([^()]+)\)', input_str).group()
#         data_strip = data.strip("()")
#         inde = li.index(data_strip)  #取得其下标
#
#         ret = comput(format_input(data_strip))   #参数为列表形式
#         li.pop(inde)
#         li.insert(inde, str(ret))
#         re_str = "".join(li)
#
#         if "+" not in re_str and "-" not in re_str and "*" not in re_str \
#                               and "/" not in re_str and "(" not in re_str and ")" not in re_str:
#             return re_str    #为什么没有return
#         else:
#             return bracket(re_str)   #迭代
#
#
# if __name__ == '__main__':
#     while True:
#         input_str = input("please input(q=quit):")
#         if input_str.strip() == "":
#             continue
#         elif input_str == 'q' or input_str == 'quit':
#             sys.exit()
#         else:
#             bracket_reture = bracket(input_str)
#             print("result:",bracket_reture)

import re


# 格式化字符串函数(消除一些错误的格式)
def format_string(string):
    # 一系列的替换语句
    string = string.replace("--", "-")
    string = string.replace("-+", "-")
    string = string.replace("++", "+")
    string = string.replace("*+", "*")
    string = string.replace("/+", "/")
    string = string.replace(" ", "-")

    return string


# 检查函数（检查输入的表达式是否合法）
def chek_expression(string):
    check_result = True   # 标志位

    if not string.count("(") == string.count(")"):   # 检查括号是否完整
        print("输入错误，未匹配到完整括号!")
        check_result = False

    if re.findall('[a-pr-z]+', string.lower()):   # 检查是否包含字母
        print("输入错误，包含非法字符!")
        check_result = False

    return check_result


# 加减法函数
def add_minus(string):

    add_regular = r'[\-]?\d+\.?\d*\+[\-]?\d+\.?\d*'       # 定义一个匹配的规则
    sub_regular = r'[\-]?\d+\.?\d*\-[\-]?\d+\.?\d*'       # 同上
# 注解：[\-]? 如果有负号，匹配负号； \d+ 匹配最少一个数字； \.? 是否有小数点，有就匹配；\d* 是否有数字有就匹配
# \+ 匹配一个加号；  [\-]?\d+\.?\d*  这几个同上

    # 加法
    while re.findall(add_regular, string):    # 按照regular规则获取一个表达式,用while循环，把所有加法都算完

        add_list = re.findall(add_regular, string)
        for add_stars in add_list:
            x, y = add_stars.split('+')      # 获取两个做加法的数(以+号作为分割对象)，分别赋给x和y
            add_result = '+' + str(float(x) + float(y))
            string = string.replace(add_stars, add_result)   # 替换
        string = format_string(string)

    # 减法
    while re.findall(sub_regular, string):    # 用while循环，把所有减法都算完

        sub_list = re.findall(sub_regular, string)
        for sub_stars in sub_list:
            x, y = sub_stars.split('-')  # 获取两个做减法的数(以-号作为分割对象)，分别赋给x和y
            sub_result = '+' + str(float(x) + float(y))
            string = string.replace(sub_stars, sub_result)   # 替换
        string = format_string(string)

    return string


# 乘、除法函数
def multiply_divide(string):
    regular = r'[\-]?\d+\.?\d*[*/][\-]?\d+\.?\d*'  # 定义一个匹配的规则regular

    while re.findall(regular, string):
        expression = re.search(regular, string).group()    # 按照regular规则获取一个表达式

        # 如果是乘法
        if expression.count('*') == 1:
            x, y = expression.spilt('*')
            mul_result = str(float(x) * float(y))
            string = string.replace(expression, mul_result)  # 计算结果替换原表达式
            string = format_string(string)  # 格式化

        # 如果是除法
        # if expression.count('/') == 1:
        #     x, y = expression.spilt('/')
        #     div_result = str(float(x) / float(y))
        #     string = string.replace(expression, div_result)
        #     string = format_string(string)  # 格式化

        # 如果是阶乘
        # if expression.count('**') == 1:
        #     x, y = expression.spilt('**')
        #     pow_result = 1
        #     for i in range(int(y)):
        #         pow_result *= int(x)
        #     string = string.replace(expression, str(pow_result))
        #     string = format_string(string)  # 格式化

    return string


# 主程序
while True:


    source = input("请输入表达式：")   # 输入要计算的式子

    source ="(9-(10-(10-0-(3+(8+(0+(8-(10-8-(7-(2+(5+(6+(10+(3+(8+(3-(9+(1+(10+(1-(1+(6-2+0+(10-(9-(3-(3-9-(1-(7+(4-(2+(2-(10+(3+(7-(1-(4+(1+(1-(10-(5-(9+(9-4-(5-(1+8-(2-(1+(1-10-(4-(1+(4-(7)-(3-(8)+(5+5-(5-(9-(8+(8-4-1+(0-(1+(1+(10-(7+(2-(5-(4-(6+(2+(1-(2-(9+8+(2+(9-(9-(7+(10+1+(5)))-(2-(8+3+(5-(7-(3+(9)+(10+(0+(8-(1-(9)-(0+10-(3+(9-(0-(5-(7-(4-4+1+(7)-(10+(5+(9-(3+(5+(6-(0-(7-(1-(4+(6+(4-2-(4+(9-(6+9-8+1+(5+(7-9+3)+(10-(10+(2+(0-(5-(2+(10-(4-5-(7-(4-(7+(4)+6+10+(2-(7+(2))+(1)+(5-(7)-(10-(5+(7-(6-(2+(1-4)+(10-(5)+(4+(10+(4+(0+(10+(8-(8+(6+5-(1-(6-(1-(2+(4+(9-(3+(1+(10+(4)+(0+(3-(2-(9-(2-(3-(4-(2+(7-(6-(5+(7+(5+(5-(4+(0-(7+(2-(7+(9)-(6-(10)+(7+(2-(9-(9)+(4+(1-(8+(2-0-(2+(2+10)-(7-9-(9+(8-(5-8-(5)+(6+(10-(3-(2-(2+(7-2+(9+(3+(9+(2-(8+(5-(4+(4-(1-(9+(0+(6-(4-(3+(5-(2-(4-(6+(0+(4+3)-(8-(6+(9+(1+(2)-(8-(1+1+(5+(4-(3-(1-(7-4+(6+(9+(1+(4)+(6+(4+(2+(7-(1+(4-(8+(6+(8-(9-(2)-3-(0-(0)+(5+(7-(8)+(8-(2+(1)+1+(3+(6-(10-(2-4-(2-(2)+(8)+(3-(1-(1)+(6+(1+(9+(9+(5)-(4+(9+(10)+(0-(3+(3+0)+(6)-(6+(6)+(4-(8-1-5-(6)-(0))-(3)+(3-(3-(8-(10-(0-(4+(7)+(6-4))+1-(2-(1-(0-(0+(1-(0)-0+(5+(10-(2-(9-(9-10)+(3+(5-(6-(6-9-(5+5))+(7+(0)-(2-(7+2+(7-(2+(7+(4-(10+(4+(10-(3-(0-2+(9+(4-4-(3-(2)+(8+(5)+(1+1-(7+(3+(10+5-(0+(10-(9+(8-(0-(0+(8-(1+(0)+(6+(5+(5+(9)))+(4-(1-(3+(7+(9+(8-(1-8-(8+(0+(1+(1-(1)+(7+(6-(7-(8+(10)+1+(0-(10)+(8+(7+(10+(6+(10+(6)-(2+(2+(10-(8)-(5)))+(9-(1)+(4)+(5)-(6-(9)-(1+(6-(9+(10)+2-(4+(9-(4+1)-(0-(9)-(3)+(0)+(10)))+9)+(6+4+(6))+(5-(9))-(9-(2-(6+(7))-(6-(3+(5+(5-(0)-(5+(6-(5+(9-(2+(9+(1+(0+2+(7)-(3-(5+(2)+(4)+(6+(7-(3-(4)+(10+(4))+(3))-(3-(2)-(2+(2+(10+(3)+(3+(5)-(3-(0+(1)+(6+(4-(4)-(7-(9-(9)+(1)+(4)+(7))-(9))))-(3-(1+5-7-(7))-(4+(3+(7-(9+(8)-(9+(8-(3)+(10-(1)+(5)-(2-(4)+(0-(10-(7-(10+(1)+(1)-(4)-(10)))+(7)+(4-4)+0+9-(6))-(6+(5)))))-(8-(6)-(10+(5-(8)-(10+(3+(0+(6-(9)-(1)))-(0)-(9+(0+(1+(8+2-(4-(9-(4+(3+4)-(10+(1-(5)+(10-(4-(6-(4-(2+(4)-(9)-(4))))-3))))+(9)+(9+(0-(1+(5-(5+(7)-6-(8-(3-(3+(1)-(9-(7-(6)))-(2+(1))-(1+(2+(10))))+(6)+(0+(9-(1)-(10)))+(10-(1-(1)))-(0+(0-(2-(4-(6+(1))+(0)+(5)-(5+(5)-(4+(6)-(5)+(1-(7))))+(8)-(7))-3))-(7+(7+(9+(0+(10)-(7-(0-(2)-(6))-(2+(10)))+(7)+(3))+(8-(8+(10)-(8)+(0+(6-(2)-(1))+(3+(10+(10-(4+(7-(2)-(9-(2+(8))))+(7)-(7+10+(9-(2)+(0))-(6+(1)))+(10)+(2)-(7)-(4)-(10+(3-(6))))+(8-(1))-(10)))+(5+(3-(0-(1-(2+(3-(6-(4)-(1)+(4+(7+(3)-(7)+(4-(9))+(0-(4)+(9+(3-(9)+(4-(10+(6+(4)))+(4))+(10+(0-3-(8+(0-(6))-(5))-(9))-(6))))+2))+6+(6)+(1-(6))-(7-(1))-(8)+(9-(8))+(4)))-(0+7-(1)))-(2))+(0)))+(4-(7))-(5)-(8)-4+(1-(3-(8+(2+0)+(7)))))))-(4-(2))+(9))))+(7)-(2-(10+(4)-(8+(7)+(5-(4)-(6+6))-(2+(6)-(2+(4-(2-(8-(4)-(7+(5)-(10-(7)))))-(10+(9+(8)-(10)+(3-(7+(4+(2+(5)-(10+7+(2-(10)-(10+(3))+(0-(10+(8+(4+(7-(2)+(3+9))))+(7-(6+(2)-(2)+7+(5+(7+(10+(5-(4)-2+(5)+(1))+(0))))-(9))-5-(8)-(9-(4)-(10))-(8-(5)-(10)-7)+(5))-(4)))))+6+3+(3+(6+(9)))-10+(6)+(0)))))+(7)))+(1-(5)+(3-(3+6))+(5)+(7)-(9-(1))+(4+(1))+(2)))-(3))-(10)+(1)))))))))+(3)+2+(8-(4)))-(1))+(6-(8-(0)-(8-(0))-(2-(4+2)))-(9+1)))-(8-(8+(1-8-(7))))+7-(5+(5+(6+(10)+(8)))))))-(4))))-(4)-(6)+(10)-(5)))+(0+(2+(4))-(4-(2)+(0-(10-(4))))))+3-(10)))-(9+(9-(8-(7)-4))))+(6))-(4-(9))))-(1))+(10))))-(0+(9+7-(1)))))-(7)-(4)))-(9))))-7))))+(9))+(10))-(8-(9)))+(8))-(6)-(4)-(8)))))))))))))-(7)))))+(2-(6)-(0))))-(0)-(5+(9)+(9))+(3-(9))))+(8))))))))-(0-(0))+(7-(2))))))))-(6))-(8+(9))-(9+(2))-(2)+(9))-(4))+(7)-(1)-(6))-(2-0)))))))-(0)))))-(8+(0-(5))))+(9)-(1-(0)-(3)))-(3)-(0)))+(4)+(6))))-(5)+(1-(5)))))+(10))))-(5)+(0))))))-(6)))))))+(1))))))))-(5)))))))))+(8))))))))))))))))))-(7)+(10)))))))))))))-(4))))))-(10)-(4))+(1)+(3))-(1))))+(9))))))))+(2-(7-(4-(3+(0))))-(10)))))+0))))+(10)))))+(4)))))))))))+(3)))))))-(5)))))+(3)))))))))))))-(7)-(5-(2+(9))-(0))+(4)))+(10)))))-(1)))-(0))+(1))-(8+(10))))))-(10)-(10+(9)+(2))))-(1)))-(2))))+(4+(5))))))+(8))))))))))))))))))))))-(7)))-(3)))))))+(1))))-(7)-(3)+(4))))))-(6)))))))-(9-(3)))))))))))+(8))))))))))+(6))))))))))))))))))))))))))))))))))+(5))+(7))))))))))))))))))))))))-(10))))))+9)))))))"

    print("eval result: ", eval(source))




    if source == "Q":    # 该判断语句只能写在前面，写后面会报错
        exit()   # 如果输入是Q，退出

    elif chek_expression(source):
        print("eval result: ", eval(source))   # eval() 是把其他类型转换为字符串
        sourse = format_string(source)

        if source.count("(") > 0:
            stars = re.search(r'\([^()]*\)', source).group()   # 去括号，得到括号里的字符串
            replace_stars = multiply_divide(stars)   # 将括号的表达式进行乘除运算
            replace_stars = add_minus(stars)         # 将乘除的结果进行加减运算
            source = format_string(source.replace(stars, replace_stars))  # 用计算结果替换括号字符串
            print('shit!!!')
            print(source)

        # 没有括号直接进行运算
        else:
            replace_stars = multiply_divide(source)   # 乘除运算
            replace_stars = add_minus(source)    # 加减运算
            source = source.replace(source, replace_stars)