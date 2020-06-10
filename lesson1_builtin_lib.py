import numpy as np
import timeit

def test_string():
    import string
    print("***字符基本操作*****************")
    strA = "Hello world python!"
    print(type(strA))
    #string 拼接
    print(strA+strA)
    print(strA*3)
    #返回字符子串
    print(strA[:5])
    print("H" in strA)

    print("***转义字符*****************")
    print("Hello \'world\' !")
    print("Hello \'world\' !")
    print(r"我就是一个'world'!")

    big_str = '''
    hello this is first line
    this is second line
    third line
    end!!!!!!
    '''
    print(big_str)

    print("***大小写处理*****************")
    print(strA.upper())
    print(strA.lower())
    print(strA.capitalize())

    print("***查找*****************")
    print(strA.count("l"))
    print(strA.find("world"))

    #数字判断
    print("***数字字母判断*****************")
    print("Hello".isalpha())
    print("Hello123".isalnum())
    print("1.23".isalnum())
    print("I am 8 years old".isalnum())
    print("123".isdecimal())
    #print(b"123".isdecimal()) # 报错
    print("123".isdigit())
    print(b"123".isdigit())

    #格式化
    print("***格式化*****************")
    data1 = 1.2345678
    print(data1)
    print("格式化%5.2f" % (data1) )

    print("{}今年{}岁了，今年{}年级，期末考试{}分".format("张三",9,"三",265))
    print("{0}今年{1}岁了，今年{2}年级，期末考试{3}分".format("张三",9,"三",265))
    print("{name}今年{age}岁了，今年{grade}年级，期末考试{score}分".format(name = "张三",age = 9,grade = "三", score = 265))

    print("123".zfill(10))

    #拆分和合并
    strA = "Hello world python"
    print(strA)
    str_list  = strA.split(" ")
    print(str_list)
    strA = "--".join(str_list)
    print(strA)
    print(strA.replace("--", " "))


def test_datetime():
    from datetime import datetime as datetime
    # 返回当前系统时间：2019-07-28 15:42:24.765625
    print(datetime.now())
    # 将datetime.datetime类型转化成str类型,输出：Sun Jul 28 15:47:51 2019
    cur_time = datetime.now()
    cur_time = datetime(year = 2020,month = 5,day =1)
    print(cur_time.ctime())
    # 返回当前日期时间的日期部分：2019-07-28
    print(cur_time.now().date())
    # 返回当前日期时间的时间部分：15:42:24.750000
    print(cur_time.now().time())

    #格式化输出  datetime转为字符
    print(cur_time.strftime("%Y-%m-%d %H:%M:%S"))
    #格式化输入 一个字符串转为datetime类型
    last_time = datetime.strptime("2020-01-01 09:30:00","%Y-%m-%d %H:%M:%S")
    print(last_time)

    #演示timedelta
    from datetime import timedelta as timedelta
    date_delta = cur_time - last_time
    print(date_delta)

    date_delta = timedelta(days =1)
    print(date_delta)
    last_time +=date_delta
    print(last_time)

    pass
def test_math():
    import math
    print(math.pi,math.e,math.tau,math.inf,math.nan)

    print(math.ceil(4.01) )
    print(math.floor(4.999))
    print(math.fabs(-3))
    print(math.factorial(5))
    print(math.fmod(20,7))
    print( math.frexp(10))
    print(math.gcd(40,20))
    print(math.isfinite(100))
    print(math.isinf(234))
    print(math.isnan(0.01))
    print(math.isnan(math.nan))
    print(math.trunc(6.789))
    print(math.exp(2))
    print(math.pow(2,7))
    print(math.sqrt(16))


def test_statistics():
    import statistics
    #平均数
    print(statistics.mean([1, 2, 3, 4, 5, 6, 7, 8, 9,10]))
    print(statistics.median([1,3,5,7]))
    print(statistics.median_low([1,3,5,7]))
    print(statistics.median_high([1,3,5,7]))
    print(statistics.median(range(1,10)))
    #总体标准差
    print(statistics.pstdev([1.5,2.5,2.5,2.75,3.25,4.75]))
    #总体方差
    print(statistics.pvariance([1.5,2.5,2.5,2.75,3.25,4.75]))

def test_csv():
    import csv

    #csv读取
    f = open('000001日行情.csv', 'r',encoding = 'utf-8')
    reader = csv.reader(f)
    #略过首行
    #reader.__next__()
    next(reader)
    kline_list = []
    for row in reader:
        kline = {}
        kline["date"] = row[0]
        kline["close"] = float(row[1]) if row[1] != "" else None
        kline["ma5"] = float(row[2]) if row[2] != "" else None
        kline["ma10"] = float(row[3]) if row[3] != "" else None
        kline_list.append(kline)
        #print(row)
    print(reader.line_num)
    print(kline_list)
    f.close()

    # csv读取
    f = open('000001日行情.csv', 'r', encoding='utf-8')
    reader = csv.reader(f)
    #把前四列数据写入新的csv文件
    new_file = open('new_file.csv','w',encoding='utf-8')
    writer = csv.writer(new_file)
    for row in reader:
        new_kline = row[0:4]
        writer.writerow(new_kline)
    new_file.close()

def test_request():
    import requests
    #获取股票日行情
    url = "http://hq.sinajs.cn/list=sz000001"
    #url = "http://hq.sinajs.cn/list=sz000001,sh000001
    response = requests.get(url)
    print(response.text)

    #获取期货日K线
    url = "http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesDailyKLine?symbol=M0"
    #url = "http://hq.sinajs.cn/list=sz000001,sh000001
    response = requests.get(url)
    print(response.text)




def main():
    test_string()
    # test_datetime()
    #test_math()
    #test_statistics()
    #test_csv()
    # test_request()



if __name__ == "__main__":
    main()