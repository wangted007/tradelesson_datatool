# 定义list的简单的加减乘除算法

def plus(lst1:list , lst2:list):
    result_len = len(lst1) if len(lst1)< len(lst2) else len(lst2)
    result = []
    for i in  range (result_len):
        result.append(lst1[i] + lst2[i])
    return result

def minus(lst1:list,lst2:list):
    result_len = len(lst1) if len(lst1)< len(lst2) else len(lst2)
    result = []
    for i in  range (result_len):
        result.append(lst1[i] - lst2[i])
    return result

def times(lst1:list,lst2:list):
    result_len = len(lst1) if len(lst1)< len(lst2) else len(lst2)
    result = []
    for i in  range (result_len):
        result.append(lst1[i] * lst2[i])
    return result

def divide(lst1:list,lst2:list):
    result_len = len(lst1) if len(lst1)< len(lst2) else len(lst2)
    result = []
    for i in  range (result_len):
        result.append(lst1[i] / lst2[i])
    return result
