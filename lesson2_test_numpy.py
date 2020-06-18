import numpy as np
import timeit

def test_def():
    #定义和属性
    #arr1 = np.array([1.0,2,3,4],ndmin = 3)
    #arr1 = np.array([[1,2,3,4],[5,6,7,8]])
    arr1 = np.array([[[1,2,3,4],[5,6,7,8],[5,6,7,8]],[[11,12,13,14],[15,16,17,18],[15,16,17,18]]],dtype = np.float)
    print(arr1)
    #print("type :",type(arr1))
    print("shape :", arr1.shape)
    print("dtype :", arr1.dtype)
    print("strides :", arr1.strides)
    print("size :", arr1.size)
    print("itemsize :", arr1.itemsize)

    #和list计算效率比较
    t1 = timeit.timeit(stmt = 'for _ in range(10): my_arr2 = my_arr * 2',setup ='import numpy as np;my_arr = np.arange(1000000)'  , number=1)
    t2 = timeit.timeit(stmt = 'for _ in range(10): my_list2 = [x * 2 for x in my_list]', setup = 'my_list = list(range(1000000))', number=1)
    print(round(t1,4),round(t2,4))

def test_create():
    print("***常用创建****************************************")
    arr1 = np.arange(5, dtype=float)
    print('arange create:',arr1)
    arr1 = np.linspace(10, 20, 5, endpoint =  False)
    print('arange linspace:',arr1)

    print('zeros1:', np.zeors((5)))
    print('zeros2:', np.zeors((5, 4)))
    print('ones1:', np.ones((5, 4, 3)))
    print('empty1:', np.empty((5, 4)))
    print('full1:', np.full((5, 4), 3))
    print('eye1:', np.eye(3, 4))
    print('linspace1:',np.linspace(0, 10, num=4))

def test_slice():
    #切片获取
    print("***切片获取****************************************")
    arr1 = np.arange(10)
    sli = slice(2, 7, 2)  # 从索引 2 开始到索引 7 停止，间隔为2
    print(arr1[sli])

    arr1 = np.array([[1,2,3],[3,4,5],[4,5,6]])
    print (arr1[...,1])   # 第2列元素
    print (arr1[1,...])   # 第2行元素
    print (arr1[...,1:])  # 第2列及剩下的所有元素

    print(arr1[arr1 >3])

    arr2 = np.arange(0,100,10)
    print(np.where(arr2 <3))

def test_action():
    # 数据操作
    print("***数组操作****************************************")
    arr1 = np.arange(9).reshape(3, 3)
    print('原始数组：')
    print(arr1)
    #生成迭代
    print('flat：')
    flat1 = arr1.flatten()
    flat1 = arr1.flatten(order = 'F')
    for item in flat1:
        print(item)
    #转置
    print(np.transpose(arr1))
    print(arr1.T)

def test_math():
    #数组计算
    print("***数组计算****************************************")
    a = np.arange(25)
    a = a.reshape((5, 5))
    b = np.array([10, 62, 1, 14, 2, 56, 79, 2, 1, 45,
                  4, 92, 5, 55, 63, 43, 35, 6, 53, 24,
                  56, 3, 56, 44, 78])
    b = b.reshape((5, 5))
    print("a",a)
    print("b",b)
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a ** 2)
    print(a < b)
    print(a > b)

    # dot 点积运算
    print(a.dot(b))

    #sum, min, max, cumsum
    print(a.sum())
    print(a.min())
    print(a.max())
    print(a.cumsum())

def main():
    test_def()
    # test_create()
    # test_action()
    # test_slice()
    # test_math()



if __name__ == "__main__":
    main()