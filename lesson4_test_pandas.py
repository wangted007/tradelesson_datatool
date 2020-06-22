import numpy as np
import pandas as pd

def testSeries():
    print("Series创建**************************************")
    array1 = np.array([1, 3, 5, np.NaN, 10])
    ser1 = pd.Series(array1)
    print(type(ser1))
    print(ser1)
    print("index:",ser1.index)
    print("values:",ser1.values)

    ser2=pd.Series([98,99,90])
    ser2.index=['语文','数学','语文'] #可重复
    print(ser2["语文"])
    ser3=pd.Series(data=[99,98,97],dtype=np.float64,index=['语文','数学','历史'])
    print(ser3)

    print("通过字典创建Series***************************")
    dit = {'语文': 90, '数学': 99, '历史': 98}
    ser4 = pd.Series(dit)
    print(ser4)

    print("Series使用**************************************")
    print(ser1[2])
    print("语文成绩:",ser2["语文"])
    print(ser1[2:4])

    print(ser1/4)
    print(ser1[ser1>2])
    print(np.log(ser1))
    print(pd.notnull(ser1))

#基本操作练习
def basicAction():
    df = pd.read_excel("lesson4_000001_daykline.xls")
    print(type(df))
    print(df.head(3))
    print(df.index[0:3])
    print(df.values)
    print(df.shape)
    print(df.describe())

#导入日K数据，计算ma5,ma10,
#进行无效值清除
#输出新的excel文件数据，保留日期，收盘价，ma5,ma10,成交量四列数据
#需要安装xlrd,xlwt支持excel读写
def MADataCalculate():
    klineInDf = pd.read_excel("lesson4_000001_daykline.xls")

    klineInDf["MA5"],klineInDf["MA10"] = klineInDf["Close"].rolling(5).mean(),klineInDf["Close"].rolling(5).mean()
    # priceSeries = klineInDf["Close"]
    # ma5Series = priceSeries.rolling(5).mean()
    # ma10Series= priceSeries.rolling(10).mean()
    # klineInDf["MA5"] = ma5Series
    # klineInDf["MA10"] = ma10Series

    #其他处理
    klineInDf.dropna(axis=1)

    klineInDf.to_excel('lesson4_000001_daykline_MA.xls')
    print(klineInDf)

    #其他处理



def main():
    #testSeries()
    #basicAction()
    MADataCalculate()


if __name__ == "__main__":
    main()