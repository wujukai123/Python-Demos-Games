import re

def mul_div(front,after,symbol):
    #计算带入的值进行计算*和/
    if symbol == "*":
        result = float(front) * float(after)
    else:
        result = float(front) / float(after)
    return result

def add_sub(front,after,symbol):
    # 计算带入的值进行计算+和-
    if symbol == "+":
        result = float(front) + float(after)
    else:
        result = float(front) - float(after)
    return result

def process(value,one,two,functions,itmes):
    #通过判断列表是否有四则运算，调取加减乘除的运算函数，不断进行计算
    for symbol_list_number,symbol_list_forin in enumerate(value):
        if one in symbol_list_forin:
            result = functions(itmes[symbol_list_number],itmes[symbol_list_number+1], one)
            itmes[symbol_list_number] = str(result)
            itmes[symbol_list_number+1] = str(result)
        elif two in symbol_list_forin:
            result = functions(itmes[symbol_list_number], itmes[symbol_list_number+1], two)
            itmes[symbol_list_number] = str(result)
            itmes[symbol_list_number+1] = str(result)

def main(number):
    digit_list = []
    symbol_list = []
    number_list = re.findall("^[0-9]+|..[0-9]+[.][0-9]+|..[0-9]+|.[0-9]+[.][0-9]+|"
                             ".[0-9]+",number)#将要计算的数值进行分开
    for n in number_list:
        #将加减乘除和数值分开，以便于后面计算
        if "*" in n or "/" in n or "+" in n or "-" in n:
            digit_list.append(n[1:])
            symbol_list.append(n[0])
        else:
            digit_list.append(n[:])
    if "-" in number_list[0]:
        #判断第一个输入的值是否为负数，是负数则将dict_list列表的第一个值进行替换
        # 并删除symbol_list的第一个符号
        digit_list[0] = number_list[0]
        del symbol_list[0]

    process(symbol_list,"*","/",mul_div,digit_list)


    while  "*" in symbol_list or "/" in symbol_list:
        #将已经计算过才*和/进行删除
        if "*" in symbol_list:
            del digit_list[symbol_list.index("*")]
            symbol_list.remove("*")
        if "/" in symbol_list:
            del digit_list[symbol_list.index("/")]
            symbol_list.remove("/")
    process(symbol_list,"+","-",add_sub,digit_list)
    return digit_list[-1]


number = input("输入你要计算的\033[31;1m公式\033[0m")

while True:
    #判断是否有括号，有括号则先进行括号内的运算
    if "(" in number:
        left = number.find(")")
        right = number[:left].rfind("(")
        number_small = number[right+1:left]
        replace = main(number_small)
        number = number[:right] + replace + number[left+1:]
    else:
        print("===>"+main(number))
        break
