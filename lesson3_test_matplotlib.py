import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
#############################################################################################################
#简单的画图例子
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
    fig = plt.figure(num=1, figsize=(15, 8), dpi=80) #开启一个窗口，同时设置大小，分辨率

    ax_top= fig.add_subplot(2, 1, 1) #通过fig添加子图，参数：行数，列数，第几个。
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    c, s = np.cos(x), np.sin(x)
    ax_top.plot(x, c)
    ax_top.plot(x, s)

    ax_bottom = fig.add_subplot(2, 1, 2)
    n = 10
    X = np.arange(n)
    Y = (1 - X / float(n)) * np.random.uniform(.5, 1.0, n)
    ax_bottom.bar(X, Y, facecolor="#0000ff", edgecolor="white")
    # 画数值
    for x, y in zip(X, Y):
        plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')

    plt.show()
#################################################################################################
#用mplfinance画K线
from matplotlib.pylab import date2num
import datetime
import matplotlib as mpl
import mplfinance as mpf
from cycler import cycler# 用于定制线条颜色
import tushare as ts

def date_to_num(dates):
    num_time = []
    for date in dates:
        date_time = datetime.datetime.strptime(date,'%Y-%m-%d')
        num_date = date2num(date_time)
        num_time.append(num_date)
    return num_time

def drawKlineByMflfinance():
    #tuahre新版本
    #ts.set_token("ca9a880eb55cf5479fe8b021615f26d1a59c6f187e9d008a817c4ae0")
    # pro = ts.pro_api()
    # klines = pro.daily(ts_code = '000001.SZ', start_date='2019-01-01')

    # klines = df.values
    # print(klines)
    # print("index:",df.index)
    # num_time = date_to_num(df.index)
    # print(num_time)
    # klines[:,0] = num_time
    # print("new Klines:",klines)
    symbol = "000001"
    df = ts.get_hist_data('000001',start="2019-01-01",end="2019-12-31")
    print("df:",df)
    #日期列
    df['date'] = pd.to_datetime(df.index)
    # 将日期列作为行索引
    df.set_index(['date'], inplace=True)
    df['Open'] = df['open']
    df['Close'] = df['close']
    df['High'] = df['high']
    df['Low'] = df['low']
    df['Volume'] = df['volume']

    #画线
    # 设置基本参数
    # type:绘制图形的类型，有candle, renko, ohlc, line等
    # 此处选择candle,即K线图
    # mav(moving average):均线类型,此处设置7,30,60日线
    # volume:布尔类型，设置是否显示成交量，默认False
    # title:设置标题
    # y_label:设置纵轴主标题
    # y_label_lower:设置成交量图一栏的标题
    # figratio:设置图形纵横比
    # figscale:设置图形尺寸(数值越大图像质量越高)
    kwargs = dict(
        type='candle',
        mav=(7, 30, 60),
        volume=True,
        title='stock:%s 2019 day kline' % (symbol),
        ylabel='OHLC Candles',
        ylabel_lower='Shares\nTraded Volume',
        figratio=(15, 10),
        figscale=5)

    # 设置marketcolors
    # up:设置K线线柱颜色，up意为收盘价大于等于开盘价
    # down:与up相反，这样设置与国内K线颜色标准相符
    # edge:K线线柱边缘颜色(i代表继承自up和down的颜色)，下同。详见官方文档)
    # wick:灯芯(上下影线)颜色
    # volume:成交量直方图的颜色
    # inherit:是否继承，选填
    mc = mpf.make_marketcolors(
        up='red',
        down='green',
        edge='i',
        wick='i',
        volume='in',
        inherit=True)

    # 设置图形风格
    # gridaxis:设置网格线位置
    # gridstyle:设置网格线线型
    # y_on_right:设置y轴位置是否在右
    s = mpf.make_mpf_style(
        gridaxis='both',
        gridstyle='-.',
        y_on_right=False,
        marketcolors=mc)

    # 设置均线颜色，配色表可见下图
    # 建议设置较深的颜色且与红色、绿色形成对比
    # 此处设置七条均线的颜色，也可应用默认设置
    mpl.rcParams['axes.prop_cycle'] = cycler(
        color=['dodgerblue', 'deeppink',
               'navy', 'teal', 'maroon', 'darkorange',
               'indigo'])

    # 设置线宽
    mpl.rcParams['lines.linewidth'] = .5

    # 图形绘制
    # show_nontrading:是否显示非交易日，默认False
    # savefig:导出图片，填写文件名及后缀
    mpf.plot(df,
             **kwargs,
             style=s,
             show_nontrading=False)
             #savefig='A_stock-%s _candle_line' % (symbol) + '.jpg')
    plt.show()

#直接使用matplot绘制K线
def drawKline():
    import lesson3_csv_kline as ck
    #获取K线数据
    dates,klines = ck.readKline('000001_daykline.csv')
    #list转ndarray
    klines = np.array(klines)
    print(dates)
    print(klines)
    sz = len(klines)
    t = [datetime.datetime.strptime(d, '%Y-%m-%d').date() for d in dates]

    #价格图
    ax1 = plt.subplot(211)
    close = klines[:,0]
    ma5 = klines[:,1]
    ma10 = klines[:,2]
    #ax1.plot(t, close,color="blue", linewidth=2.5, linestyle="-", label="close")
    ax1.plot(t, close)
    ax1.plot(t, ma5,)
    ax1.plot(t, ma10)
    plt.setp(ax1.get_xticklabels(), visible=False)
    #ax1.legend(loc='upper left')

    #plt.ylabel('price')

    #成交量图
    ax2 = plt.subplot(212,sharex= ax1)
    volume  = klines[:,3]
    ax2.bar(t,volume,)

    # plt.xlable('date')
    # plt.ylabel('volume')

    plt.title("latest 1 year Kline")

    plt.show()

def main():
    #simpleLineDraw()
    #simpleBarDraw()
    #subChartDraw()
    drawKlineByMflfinance()
    #drawKline()


if __name__ == "__main__":
    main()