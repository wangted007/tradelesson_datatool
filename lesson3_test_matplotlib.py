import numpy as np
from matplotlib import pyplot as plt

#最简单的画图例子
def simpleLineDraw():
    x = np.linspace(-np.pi,np.pi,256,endpoint=True)
    c,s=np.cos(x),np.sin(x)
    plt.figure(1)
    plt.plot(x,c)
    plt.plot(x,s)
    plt.show()
#画柱状图
def simpleBarDraw():
    n =10
    X = np.arange(n)
    Y = (1-X/float(n))*np.random.uniform(.5,1.0,n)
    plt.bar(X , Y ,facecolor="#0000ff" , edgecolor="white")
    #画数值
    for x,y in zip(X , Y):
        plt.text(x+0.4,y+0.05,'%.2f' % y,ha='center' ,va= 'bottom')
    plt.show()

#子图练习
def subChartDraw():
    fig = plt.figure()
    #图1
    fig.add_subplot(2, 1, 1)
    simpleLineDraw()

    #图2
    fig.add_subplot(2, 1, 2)
    simpleBarDraw()

    plt.show()

def main():
    #simpleLineDraw()
    #simpleBarDraw()
    subChartDraw()


if __name__ == "__main__":
    main()