import re
def atom_cal(exp):
    if '*' in exp:       #计算单个的乘法
        a,b = exp.split('*')
        return str(float(a) * float(b))
    elif '/' in exp:  #计算单个的除法
        a, b = exp.split('/')
        return str(float(a) / float(b))

def format_exp(exp):  #处理符号的问题
    exp = exp.replace('--','+')
    exp = exp.replace('+-','-')
    exp = exp.replace('-+','-')
    exp = exp.replace('++','+')
    return exp

def mul_div(exp):    #计算乘除法
    while True:
        ret = re.search('\d+(\.\d+)?[*/]-?\d+(\.\d+)?',exp)  #利用正则表达式匹配乘或除法
        if ret:   #如果匹配到的话
            atom_exp = ret.group()  #将这个值拿出来
            res = atom_cal(atom_exp) #调用上面个的atom_cal计算
            exp = exp.replace(atom_exp,res) #将计算的结果把原来的算是替换掉
        else:return exp   #如果匹配不到的话说明乘除法计算完毕,返回计算结果

def add_sub(exp):  #计算加减法
    ret = re.findall('[+-]?\d+(?:\.\d+)?', exp)  #利用正则表达式匹配算式中的带符号的每项数字,返回一个列表
    exp_sum = 0
    for i in ret:
        exp_sum += float(i)   #将列表中的每一项求和
    return exp_sum

def cal(exp):    #计算加减乘除混合运算
    exp = mul_div(exp)  #调用mul_div函数先计算乘除法
    exp = format_exp(exp)  #调用format_exp处理计算时候的符号
    exp_sum =  add_sub(exp)  #调用add_sub计算加减法
    return exp_sum   # float  #返回计算结果

def main(exp):
    exp = exp.replace(' ','')   #删除字符串中的空格
    while True:
        ret = re.search('\([^()]+\)',exp)  #匹配括号
        if ret :    #如果匹配到的话
            inner_bracket = ret.group() #用group()将匹配到的括号内容取出来
            res = str(cal(inner_bracket))  #调用cal()计算括号中的内容,将返回的结果转换成字符串
            exp = exp.replace(inner_bracket,res)  #将匹配到的括号中的内容用计算结果替换
            exp = format_exp(exp)  #处理符号
        else:break  #直到没有括号跳出循环
    return cal(exp)  #将剩下的内容进行计算,然后返回

s = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
ret = main(s)
print(ret)
