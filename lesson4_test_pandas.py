import numpy as np
import pandas as pd


def test_series():
    print("Series创建**************************************")
    array1 = np.array([1, 3, 5, np.NaN, 10])
    ser1 = pd.Series(array1)
    print(type(ser1))
    print(ser1)
    print("index:", ser1.index)
    print("values:", ser1.values)

    ser2 = pd.Series([98, 99, 90])
    ser2.index = ['语文', '数学', '语文']  #可重复
    print(ser2["语文"])
    ser3=pd.Series(data=[99, 98, 97],dtype=np.float64, index=['语文', '数学', '历史'])
    print(ser3)

    print("通过字典创建Series***************************")
    dit = {'语文': 90, '数学': 99, '历史': 98}
    ser4 = pd.Series(dit)
    print(ser4)

    print("Series使用**************************************")
    print(ser1[2])
    print("语文成绩:", ser2["语文"])
    print(ser1[2:4])

    print(ser1/4)
    print(ser1[ser1 > 2])
    print(np.log(ser1))
    print(pd.notnull(ser1))

#基本操作练习
def basic_action():
    dates = pd.date_range('20200101', periods=6)
    df1 = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print(df1)

    df2 = pd.DataFrame({'A': 1.,
                        'B': pd.Timestamp('20200102'),
                        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                        'D': np.array([3] * 4, dtype='int32'),
                        'E': pd.Categorical(["test", "train", "test", "train"]),
                        'F': 'foo'})
    print(df2)
    #多个列不同类型
    print(df2.dtypes)
    #数据浏览
    print(df2.head(3))
    print(df2.tail(3))
    print(df2.index)
    print(df2.columns)

    #to_numpy 转换
    print(df1.to_numpy())
    print(df1.describe())
    print(df1.sort_index(axis=0, ascending=False))
    print(df1.sort_values(axis="index", by="B", ascending=False))

    print("**选择整行整列**************")
    print(df1["A"])
    print(df1[0:3])
    print(df1["20200102":"20200105"])

    print(df1.loc[dates[0]])
    print(df1.loc[:, ['A', 'C']])
    print(df1.loc['20200102':'20200105', ['A', 'C']])
    print(df1.iloc[[1, 2, 4], [0, 2]])

    print(df1.at[dates[0], 'A'])
    print(df1.iat[0, 1])


    #增加和删除列
    print("**增加和删除列***************************************")
    print(df1)
    df3 = df1.reindex(index=dates[0:4],columns = list(df1.columns) +['E'])
    df3.loc[dates[0]:dates[1], 'E'] = 1
    s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20200102', periods=6))
    df3['F'] = s1
    print(df3)
    df3 = df3.drop(['D'], axis=1)
    print(df3)
    #丢失值处理
    print(df3.dropna())
    print(df3.fillna(value=-1))

    #数据合并
    df3_a = df1.head(1)
    df3_b = df1.tail(2)
    print(pd.concat([df3_a,df3_b]))

    #group by
    df4 = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                             'foo', 'bar', 'foo', 'foo'],
                       'B': ['one', 'one', 'two', 'three',
                             'two', 'two', 'one', 'three'],
                       'C': np.random.randn(8),
                       'D': np.random.randn(8)})
    print(df4)
    print(df4.groupby('A').count())
    print(df4.groupby(['A','B']).sum())

    #时间序列
    print("**时间序列***************************")
    rng = pd.date_range('1/1/2020', periods=100, freq='min')
    ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
    print(ts)
    print(ts.resample('5Min').sum())

#导入日K数据，计算ma5,ma10,
#进行无效值清除
#输出新的excel文件数据，保留日期，收盘价，成交量，ma5，ma10数据
#需要安装xlrd,xlwt支持excel读写
def MA_data_calculate():
    # klineInDf = pd.read_excel("lesson4_000001_daykline.xls")
    # klineInDf["MA5"],klineInDf["MA10"] = klineInDf["Close"].rolling(5).mean(),klineInDf["Close"].rolling(5).mean()
    # klineInDf.to_excel('lesson4_000001_daykline_MA.xls')

    klineInDf = pd.read_excel("lesson4_000001_daykline.xls", index_col="Date")
    priceSeries = klineInDf["Close"]
    ma5Series = priceSeries.rolling(5).mean()
    ma10Series= priceSeries.rolling(10).mean()
    klineInDf["MA5"] = ma5Series
    klineInDf["MA10"] = ma10Series
    #其他处理
    #清除NaN只
    klineInDf = klineInDf[['Close','Volume','MA5','MA10']]
    klineInDf = klineInDf.dropna(axis=0)
    print(klineInDf)
    klineInDf.to_excel('lesson4_000001_daykline_MA.xls')



def main():
    #test_series()
    #basic_action()
    MA_data_calculate()


if __name__ == "__main__":
    main()