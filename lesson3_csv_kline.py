# 定义list的简单的加减乘除算法

def readKlineFromCsv1(path:str, code='utf-8'):
    import csv

    #csv读取
    f = open(path, 'r',encoding = code)
    reader = csv.reader(f)
    #略过首行
    #reader.__next__()
    next(reader)
    kline_result_list = []
    for row in reader:
        kline = {}
        kline["Date"] = row[0]
        kline["Close"] = float(row[5]) if row[5] != "" else None
        kline["Ma5"] = float(row[6]) if row[6] != "" else None
        kline["Ma10"] = float(row[7]) if row[7] != "" else None
        kline["Volume"] = float(row[8].replace(",","")) if row[8] != "" else None
        kline_result_list
    print(kline_result_list)
    f.close()

    return kline_result_list

def readKline(path:str, code='utf-8'):
    import csv

    #csv读取
    f = open(path, 'r',encoding = code)
    reader = csv.reader(f)
    #略过首行
    #reader.__next__()
    next(reader)
    kline_date = []
    kline_result_list = []
    for row in reader:
        #处理日期
        kline_date.append(row[0])
        #处理K线数据
        kline = []
        kline.append(float(row[5]) if row[5] != "" else None)
        kline.append(float(row[6]) if row[6] != "" else None)
        kline.append(float(row[7]) if row[7] != "" else None)
        kline.append(float(row[8].replace(",","")) if row[8] != "" else None)
        kline_result_list.append(kline)
    print(kline_date)
    print(kline_result_list)
    f.close()

    return kline_date, kline_result_list
