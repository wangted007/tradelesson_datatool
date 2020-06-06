
#python默认内置库
def test_builtin_lib():

    import random as rd
    data1 = rd.random()
    print(data1)
    pass




#外部安装库
def test_setup_lib():
    import numpy as np
    print(np.ones((5,3)))
    pass


#自定义库
def test_self_lib():
    import  min_math_lib as min_math
    lst1 = [5,6,7,8]
    lst2 = [1,2,3,4]
    print(min_math.plus(lst1,lst2))
    print(min_math.minus(lst1,lst2))
    print(min_math.times(lst1,lst2))
    print(min_math.divide(lst1,lst2))


def main():
    test_builtin_lib()
    test_setup_lib()
    test_self_lib()



if __name__ == "__main__":
    main()