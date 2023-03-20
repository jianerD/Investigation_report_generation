import numpy as np
import pandas as pd


def l_ldpj_total_no1_point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("领导评价结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", ]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return int(data2.loc[place, 'a8'])


def l_ldpj_total_no2_point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("领导评价结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", ]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return int(data2.loc[place, 'a9'])


def l_ldpj_total_no3_point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("领导评价结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", ]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return int(data2.loc[place, 'a10'])


def l_ldpj_kaohe_no1_point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("领导评价结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", ]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return int(data2.loc[place, 'a16'])


def l_ldpj_kaohe_no2_point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("领导评价结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", ]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return int(data2.loc[place, 'a17'])


def l_ldpj_kaohe_no3_point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("领导评价结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", ]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return int(data2.loc[place, 'a18'])


def l_mydc_total_rate(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("2022年度社会评价总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26", "a27", "a28", "a29", "a30", "a31", "a32",
             "a33", "a34", "a35", "a36", "a37", "a38", "a39", "a40"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a13'], 2)


def l_mydc_total_point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("2022年度社会评价总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26", "a27", "a28", "a29", "a30", "a31", "a32",
             "a33", "a34", "a35", "a36", "a37", "a38", "a39", "a40"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a12'], 2)


def l_mydc_benlei_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("2022年度社会评价总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26", "a27", "a28", "a29", "a30", "a31", "a32",
             "a33", "a34", "a35", "a36", "a37", "a38", "a39", "a40"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a13'], 2)


def l_mydc_quanshi_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("2022年度社会评价总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26", "a27", "a28", "a29", "a30", "a31", "a32",
             "a33", "a34", "a35", "a36", "a37", "a38", "a39", "a40"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a14'], 2)


def l_mydc_benlei_maxpoint(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("2022年度社会评价总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26", "a27", "a28", "a29", "a30", "a31", "a32",
             "a33", "a34", "a35", "a36", "a37", "a38", "a39", "a40"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    if place in ["灵川县", "全州县", "兴安县", "永福县", "平乐县", "荔浦县"]:
        return round(data2.iloc[6, 11], 2)
    elif place in ["阳朔县", "灌阳县", "恭城县", "龙胜县", "资源县"]:
        return round(data2.iloc[15, 11], 2)
    else:
        return round(data2.iloc[25, 7], 2)


def l_mydc_benlei_avgpoint(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("2022年度社会评价总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26", "a27", "a28", "a29", "a30", "a31", "a32",
             "a33", "a34", "a35", "a36", "a37", "a38", "a39", "a40"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    if place in ["灵川县", "全州县", "兴安县", "永福县", "平乐县", "荔浦县"]:
        return round(data2.iloc[9, 11], 2)
    elif place in ["阳朔县", "灌阳县", "恭城县", "龙胜县", "资源县"]:
        return round(data2.iloc[18, 11], 2)
    else:
        return round(data2.iloc[28, 11], 2)


def l_db1wy_total_point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级“两代表一委员”总结果", header=3))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a16'], 2)


def l_db1wy_total_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级“两代表一委员”总结果", header=3))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a18'], 2)


def l_db1wy_benlei_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级“两代表一委员”总结果", header=3))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a17']


def l_db1wy_benlei_maxpoint(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级“两代表一委员”总结果", header=3))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    if place in ["灵川县", "全州县", "兴安县", "永福县", "平乐县", "荔浦县"]:
        return 90
    elif place in ["阳朔县", "灌阳县", "恭城县", "龙胜县", "资源县"]:
        return 90
    else:
        return 89.88


def l_2021_db1wy_total_rank(file_name, pl: str):
    if pl == '灵川县':
        return 17
    elif pl == '全州县':
        return 4
    elif pl == '兴安县':
        return 13
    elif pl == '永福县':
        return 4
    elif pl == '平乐县':
        return 15
    elif pl == '荔浦县':
        return 1
    elif pl == '阳朔县':
        return 12
    elif pl == '灌阳县':
        return 9
    elif pl == '龙胜县':
        return 1
    elif pl == '资源县':
        return 13
    elif pl == '恭城县':
        return 4
    elif pl == '临桂区':
        return 9
    elif pl == '象山区':
        return 8
    elif pl == '秀峰区':
        return 4
    elif pl == '叠彩区':
        return 15
    elif pl == '七星区':
        return 9
    else:
        return 1


def l_db1wy_benlei_avgpoint(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("2022年度社会评价总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26", "a27", "a28", "a29", "a30", "a31", "a32",
             "a33", "a34", "a35", "a36", "a37", "a38", "a39", "a40"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    if place in ["灵川县", "全州县", "兴安县", "永福县", "平乐县", "荔浦县"]:
        return round(data2.iloc[9, 16], 2)
    elif place in ["阳朔县", "灌阳县", "恭城县", "龙胜县", "资源县"]:
        return round(data2.iloc[18, 16], 2)
    else:
        return round(data2.iloc[28, 16], 2)


def l_ddb_total_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级党代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a4'], 2)


def l_ddb_benlei_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级党代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a4'], 2)


def l_ddb_q1_point(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级党代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a7'], 2)


def l_ddb_q2_point(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级党代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a11'], 2)


def l_ddb_q3_point(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级党代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a15'], 2)


def l_ddb_q4_point(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级党代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a19'], 2)


def l_ddb_q5_point(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级党代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a23'], 2)


def l_rddb_total_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级人大代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a4'], 2)


def l_rddb_benlei_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级人大代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a5'], 2)


def l_rddb_q1_point(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级人大代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a7'], 2)


def l_rddb_q2_point(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级人大代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a11'], 2)


def l_rddb_q3_point(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级人大代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a15'], 2)


def l_rddb_q4_point(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级人大代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a19'], 2)


def l_rddb_q5_point(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级人大代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a23'],2)


def l_zxwy_total_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级政协委员", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a4'], 2)


def l_zxwy_benlei_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级政协委员", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a5'], 2)


def l_zxwy_q1_point(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级政协委员", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a7'], 2)


def l_zxwy_q2_point(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级政协委员", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a11'], 2)


def l_zxwy_q3_point(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级政协委员", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a15'], 2)


def l_zxwy_q4_point(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级政协委员", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a19'], 2)


def l_zxwy_q5_point(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级政协委员", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a23'],2)


def l_shpj_total_point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("2022年度社会评价总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26", "a27", "a28", "a29", "a30", "a31", "a32",
             "a33", "a34", "a35", "a36", "a37", "a38", "a39", "a40"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a2'], 2)


def l_shpj_total_rate(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("2022年度社会评价总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26", "a27", "a28", "a29", "a30", "a31", "a32",
             "a33", "a34", "a35", "a36", "a37", "a38", "a39", "a40"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a3'], 2)


def l_shpj_benlei_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("2022年度社会评价总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26", "a27", "a28", "a29", "a30", "a31", "a32",
             "a33", "a34", "a35", "a36", "a37", "a38", "a39", "a40"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a4']


def l_shpj_quanshi_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("2022年度社会评价总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26", "a27", "a28", "a29", "a30", "a31", "a32",
             "a33", "a34", "a35", "a36", "a37", "a38", "a39", "a40"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a5']


def l_ldpj_total_point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("2022年度社会评价总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26", "a27", "a28", "a29", "a30", "a31", "a32",
             "a33", "a34", "a35", "a36", "a37", "a38", "a39", "a40"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a6'], 2)


def l_ldpj_total_rate(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("2022年度社会评价总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26", "a27", "a28", "a29", "a30", "a31", "a32",
             "a33", "a34", "a35", "a36", "a37", "a38", "a39", "a40"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a7'], 2)


def l_ldpj_benlei_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("2022年度社会评价总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26", "a27", "a28", "a29", "a30", "a31", "a32",
             "a33", "a34", "a35", "a36", "a37", "a38", "a39", "a40"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a8']


def l_ldpj_quanshi_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("2022年度社会评价总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26", "a27", "a28", "a29", "a30", "a31", "a32",
             "a33", "a34", "a35", "a36", "a37", "a38", "a39", "a40"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a9']


def l_sldpj_point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("2022年度社会评价总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26", "a27", "a28", "a29", "a30", "a31", "a32",
             "a33", "a34", "a35", "a36", "a37", "a38", "a39", "a40"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a10']


def l_szdwldpj_point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("2022年度社会评价总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26", "a27", "a28", "a29", "a30", "a31", "a32",
             "a33", "a34", "a35", "a36", "a37", "a38", "a39", "a40"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a11']


def l_ldpj_fenqu_maxpoint(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("2022年度社会评价总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26", "a27", "a28", "a29", "a30", "a31", "a32",
             "a33", "a34", "a35", "a36", "a37", "a38", "a39", "a40"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    if place in ["灵川县", "全州县", "兴安县", "永福县", "平乐县", "荔浦县"]:
        return round(data2.iloc[6, 5], 2)
    elif place in ["阳朔县", "灌阳县", "恭城县", "龙胜县", "资源县"]:
        return round(data2.iloc[15, 5], 2)
    else:
        return round(data2.iloc[25, 5], 2)


def l_szldpj_fenqu_maxpoint(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("2022年度社会评价总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26", "a27", "a28", "a29", "a30", "a31", "a32",
             "a33", "a34", "a35", "a36", "a37", "a38", "a39", "a40"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    if place in ["灵川县", "全州县", "兴安县", "永福县", "平乐县", "荔浦县"]:
        return round(data2.iloc[6, 10], 2)
    elif place in ["阳朔县", "灌阳县", "恭城县", "龙胜县", "资源县"]:
        return round(data2.iloc[15, 10], 2)
    else:
        return round(data2.iloc[25, 10], 2)


def l_2021_zonghe_point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("2021年度社会评价总结果 (3)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24"]
    data2.columns = d_col
    data2.set_index('a0', inplace=True)
    return round(data2.loc[place, 'a1'], 2)


def l_2021_shehui_benlei_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("2021年度社会评价总结果 (3)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24"]
    data2.columns = d_col
    data2.set_index('a0', inplace=True)
    return data2.loc[place, 'a2']


def l_2021_shehui_quanshi_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("2021年度社会评价总结果 (3)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24"]
    data2.columns = d_col
    data2.set_index('a0', inplace=True)
    return data2.loc[place, 'a3']


def l_2021_mydc_benlei_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("2021年度社会评价总结果 (3)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24"]
    data2.columns = d_col
    data2.set_index('a0', inplace=True)
    return data2.loc[place, 'a8']


def l_2021_mydc_quanshi_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("2021年度社会评价总结果 (3)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24"]
    data2.columns = d_col
    data2.set_index('a0', inplace=True)
    return data2.loc[place, 'a9']


def l_2021_ldpj_quanshi_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("2021年度社会评价总结果 (3)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24"]
    data2.columns = d_col
    data2.set_index('a0', inplace=True)
    return data2.loc[place, 'a6']


def l_2021_ldpj_benlei_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("2021年度社会评价总结果 (3)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24"]
    data2.columns = d_col
    data2.set_index('a0', inplace=True)
    return data2.loc[place, 'a5']


def l_2021_2db1wy_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("2021年度社会评价总结果 (3)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24"]
    data2.columns = d_col
    data2.set_index('a0', inplace=True)
    return data2.loc[place, 'a11']


def l_2021_csjm_nz_benlei_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城乡居民满意度调查总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26", "a27", "a28", "a29", "a30", "a31", "a32",
             "a33", "a34", "a35", "a36", "a37", "a38", "a39", "a40", "a41", "a42",
             "a43"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a9']


def l_2021_csjm_nz_quanshi_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城乡居民满意度调查总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26", "a27", "a28", "a29", "a30", "a31", "a32",
             "a33", "a34", "a35", "a36", "a37", "a38", "a39", "a40", "a41", "a42",
             "a43"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a10']


def l_ddb_total_point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级党代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a3'], 2)


def l_ddb_total_satisfaction_rate(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级党代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a6']


def l_ddb_q1_satisfaction_rate(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级党代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a10']


def l_ddb_q1_quanshi_rank(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级党代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a9']


def l_ddb_q1_benlei_rank(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级党代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a8']


def l_ddb_q2_satisfaction_rate(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级党代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a14']


def l_ddb_q2_quanshi_rank(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级党代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a13']


def l_ddb_q2_benlei_rank(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级党代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a12']


def l_ddb_q3_satisfaction_rate(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级党代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a18']


def l_ddb_q3_quanshi_rank(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级党代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a17']


def l_ddb_q3_benlei_rank(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级党代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a16']


def l_ddb_q4_satisfaction_rate(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级党代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a22']


def l_ddb_q4_quanshi_rank(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级党代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a21']


def l_ddb_q4_benlei_rank(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级党代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a20']


def l_ddb_q5_satisfaction_rate(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级党代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a26']


def l_ddb_q5_quanshi_rank(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级党代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a25']


def l_ddb_q5_benlei_rank(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级党代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a24']


def l_zxwy_total_point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级政协委员", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a3'], 2)


def l_zxwy_total_satisfaction_rate(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级政协委员", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a6']


def l_zxwy_q1_satisfaction_rate(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级政协委员", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a10']


def l_zxwy_q1_quanshi_rank(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级政协委员", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a9']


def l_zxwy_q1_benlei_rank(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级政协委员", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a8']


def l_zxwy_q2_satisfaction_rate(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级政协委员", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a14']


def l_zxwy_q2_quanshi_rank(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级政协委员", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a13']


def l_zxwy_q2_benlei_rank(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级政协委员", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a12']


def l_zxwy_q3_satisfaction_rate(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级政协委员", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a18']


def l_zxwy_q3_quanshi_rank(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级政协委员", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a17']


def l_zxwy_q3_benlei_rank(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级政协委员", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a16']


def l_zxwy_q4_satisfaction_rate(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级政协委员", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a22']


def l_zxwy_q4_quanshi_rank(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级政协委员", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a21']


def l_zxwy_q4_benlei_rank(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级政协委员", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a20']


def l_zxwy_q5_satisfaction_rate(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级政协委员", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a26']


def l_zxwy_q5_quanshi_rank(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级政协委员", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a25']


def l_zxwy_q5_benlei_rank(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级政协委员", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a24']


def l_rddb_total_point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级人大代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a3'], 2)


def l_rddb_total_satisfaction_rate(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级人大代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a6']


def l_rddb_q1_satisfaction_rate(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级人大代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a10']


def l_rddb_q1_quanshi_rank(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级人大代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a9']


def l_rddb_q1_benlei_rank(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级人大代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a8']


def l_rddb_q2_satisfaction_rate(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级人大代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a14']


def l_rddb_q2_quanshi_rank(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级人大代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a13']


def l_rddb_q2_benlei_rank(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级人大代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a12']


def l_rddb_q3_satisfaction_rate(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级人大代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a18']


def l_rddb_q3_quanshi_rank(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级人大代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a17']


def l_rddb_q3_benlei_rank(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级人大代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a16']


def l_rddb_q4_satisfaction_rate(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级人大代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a22']


def l_rddb_q4_quanshi_rank(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级人大代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a21']


def l_rddb_q4_benlei_rank(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级人大代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a20']


def l_rddb_q5_satisfaction_rate(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级人大代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a26']


def l_rddb_q5_quanshi_rank(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级人大代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a25']


def l_rddb_q5_benlei_rank(file_name, place):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("县级人大代表", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return data2.loc[place, 'a24']


# l_l1 = l_ldpj_total_point(wj1,pl)
# # 领导评价总分
# l_l2 = l_ldpj_total_rate(wj1, pl)
# # 满意率
# l_l3 = l_ldpj_total_no1_point(wj1,pl)
# # 市领导一等数
# l_l4 = l_ldpj_total_no2_point(wj1,pl)
# # 市领导二等数
# l_l5 = l_ldpj_total_no3_point(wj1,pl)
# # 市领导三等数
# l_l6 = l_ldpj_kaohe_no1_point(wj1,pl)
# # 相关领导一等数
# l_l7 = l_ldpj_kaohe_no2_point(wj1,pl)
# # 相关领导二等数
# l_l8 = l_ldpj_kaohe_no3_point(wj1,pl)
# # 相关领导三等数
# l_m1 = l_mydc_total_point(wj1,pl)
# # 民意调查总得分
# l_m2 = l_mydc_total_rate(wj1,pl)
# # 民意调查得分率
# l_m3 = l_mydc_quanshi_rank(wj1,pl)
# # 民意调查全市排名
# l_m4 = l_m3 - l_2021_mydc_quanshi_rank(wj2,pl)
# # 民意调查全市排名 2022-2021
# l_m5 = 75.89 - l_m1
# # 民意调查差第一名得分
# l_m6 = l_m1- 73.48
# # 民意调查 得分高于平均分
# l_m7 = l_mydc_benlei_rank(wj1,pl)
# # 民意调查本类排名
# l_m8 = l_m7 - l_2021_mydc_benlei_rank(wj2,pl)
# # 民意调查本类排名 2022-2021
# l_m9 = l_mydc_benlei_maxpoint(wj1,pl) - l_mydc_total_point(wj1,pl)
# # 民意调查差最高得分
# l_m10 = l_mydc_total_point(wj1,pl)  - l_mydc_benlei_avgpoint(wj1,pl)
# # 民意调查比平均分高
# l_dw1 = l_db1wy_total_point(wj1,pl)
# # 2代表1委员 总得分
# l_dw2 = l_db1wy_total_rank(wj1,pl)
# # 2代表1委员 全市排名
# l_dw3 = l_db1wy_total_rank(wj1,pl) - l_2021_db1wy_total_rank(wj2,pl)
# # 2代表1委员 全市排名 2022-2021
# l_dw4 = 89.92 - l_dw1
# # 2代表1委员比第一名得分低
# l_dw5 = l_dw2 - 89.378
# # 2代表1委员比平均分高
# l_dw6 = l_db1wy_benlei_rank(wj1,pl)
# # 21本类排名
# l_dw7 = l_db1wy_benlei_rank(wj1,pl) - l_2021_2db1wy_rank(wj2,pl)
# #  21本类比2021年高
# l_dw8 = l_db1wy_benlei_maxpoint(wj1,pl) - l_dw1
# # 21本类比第一名低
# l_dw9 = l_dw1 - l_db1wy_benlei_avgpoint(wj1,pl)
# # 21 比平均分高
# l_d1 = l_ddb_total_point(wj1,pl)
# # 党代表总分
# l_d2 = l_ddb_total_satisfaction_rate(wj1,pl)
# # 总体满意率
# l_d3 = l_ddb_total_rank(wj1,pl)
# # 总体排名
# l_d4 = l_ddb_benlei_rank(wj1,pl)
# # 本类排名
# l_d5 = l_ddb_q1_point(wj1,pl)
# # 1题分
# l_d6 = l_ddb_q1_satisfaction_rate(wj1,pl)
# # 1题满意率
# l_d7 = l_ddb_q1_quanshi_rank(wj1,pl)
# # 1题全市排名
# l_d8 = l_ddb_q1_benlei_rank(wj1,pl)
# # 1题本类排名
# l_d9 = l_ddb_q2_point(wj1,pl)
# # 2题分
# l_d10 = l_ddb_q2_satisfaction_rate(wj1,pl)
# # 2题满意率
# l_d11 = l_ddb_q2_quanshi_rank(wj1,pl)
# # 2题全市排名
# l_d12 = l_ddb_q2_benlei_rank(wj1,pl)
# # 2题本类排名
# l_d13 = l_ddb_q3_point(wj1,pl)
# # 3题分
# l_d14 = l_ddb_q3_satisfaction_rate(wj1,pl)
# # 3题满意率
# l_d15 = l_ddb_q3_quanshi_rank(wj1,pl)
# # 3题全市排名
# l_d16 = l_ddb_q3_benlei_rank(wj1,pl)
# # 3题本类排名
# l_d17 = l_ddb_q4_point(wj1,pl)
# # 4题分
# l_d18 = l_ddb_q4_satisfaction_rate(wj1,pl)
# # 4题满意率
# l_d19 = l_ddb_q4_quanshi_rank(wj1,pl)
# # 4题全市排名
# l_d20 = l_ddb_q4_benlei_rank(wj1,pl)
# # 4题本类排名
# l_d21 = l_ddb_q5_point(wj1,pl)
# # 5题分
# l_d22 = l_ddb_q5_satisfaction_rate(wj1,pl)
# # 5题满意率
# l_d23 = l_ddb_q5_quanshi_rank(wj1,pl)
# # 5题全市排名
# l_d24 = l_ddb_q5_benlei_rank(wj1,pl)
# # 5题本类排名
# l_r1 = l_rddb_total_point(wj1,pl)
# # 人大代表总分
# l_r2 = l_rddb_total_satisfaction_rate(wj1,pl)
# # 人大代表满意率
# l_r3 = l_rddb_total_rank(wj1,pl)
# # 人大代表全市排名
# l_r4 = l_rddb_benlei_rank(wj1,pl)
# # 本类排名
# l_r5 = l_rddb_q1_point(wj1,pl)
# # 1题分
# l_r6 = l_rddb_q1_satisfaction_rate(wj1,pl)
# # 1题满意率
# l_r7 = l_rddb_q1_quanshi_rank(wj1,pl)
# # 1题全市排名
# l_r8 = l_rddb_q1_benlei_rank(wj1,pl)
# # 1题本类排名
# l_r9 = l_rddb_q2_point(wj1,pl)
# # 2题分
# l_r10 = l_rddb_q2_satisfaction_rate(wj1,pl)
# # 2题满意率
# l_r11 = l_rddb_q2_quanshi_rank(wj1,pl)
# # 2题全市排名
# l_r12 = l_rddb_q2_benlei_rank(wj1,pl)
# # 2题本类排名
# l_r13 = l_rddb_q3_point(wj1,pl)
# # 3题分
# l_r14 = l_rddb_q3_satisfaction_rate(wj1,pl)
# # 3题满意率
# l_r15 = l_rddb_q3_quanshi_rank(wj1,pl)
# # 3题全市排名
# l_r16 = l_rddb_q3_benlei_rank(wj1,pl)
# # 3题本类排名
# l_r17 = l_rddb_q4_point(wj1,pl)
# # 4题分
# l_r18 = l_rddb_q4_satisfaction_rate(wj1,pl)
# # 4题满意率
# l_r19 = l_rddb_q4_quanshi_rank(wj1,pl)
# # 4题全市排名
# l_r20 = l_rddb_q4_benlei_rank(wj1,pl)
# # 4题本类排名
# l_r21 = l_rddb_q5_point(wj1,pl)
# # 5题分
# l_r22 = l_rddb_q5_satisfaction_rate(wj1,pl)
# # 5题满意率
# l_r23 = l_rddb_q5_quanshi_rank(wj1,pl)
# # 5题全市排名
# l_r24 = l_rddb_q5_benlei_rank(wj1,pl)
# # 5题本类排名
# l_z1 = l_zxwy_total_point(wj1,pl)
# # 政协委员总分
# l_z2 = l_zxwy_total_satisfaction_rate(wj1,pl)
# # 政协委员总体满意度
# l_z3 = l_zxwy_total_rank(wj1,pl)
# # 政协委员全市排名
# l_z4 = l_zxwy_benlei_rank(wj1,pl)
# # 政协委员本类排名
# l_z5 = l_zxwy_q1_point(wj1,pl)
# # 1题分
# l_z6 = l_zxwy_q1_satisfaction_rate(wj1,pl)
# # 1题满意率
# l_z7 = l_zxwy_q1_quanshi_rank(wj1,pl)
# # 1题全市排名
# l_z8 = l_zxwy_q1_benlei_rank(wj1,pl)
# # 1题本类排名
# l_z9 = l_zxwy_q2_point(wj1,pl)
# # 2题分
# l_z10 = l_zxwy_q2_satisfaction_rate(wj1,pl)
# # 2题满意率
# l_z11 = l_zxwy_q2_quanshi_rank(wj1,pl)
# # 2题全市排名
# l_z12 = l_zxwy_q2_benlei_rank(wj1,pl)
# # 2题本类排名
# l_z13 = l_zxwy_q3_point(wj1,pl)
# # 3题分
# l_z14 = l_zxwy_q3_satisfaction_rate(wj1,pl)
# # 3题满意率
# l_z15 = l_zxwy_q3_quanshi_rank(wj1,pl)
# # 3题全市排名
# l_z16 = l_zxwy_q3_benlei_rank(wj1,pl)
# # 3题本类排名
# l_z17 = l_zxwy_q4_point(wj1,pl)
# # 4题分
# l_z18 = l_zxwy_q4_satisfaction_rate(wj1,pl)
# # 4题满意率
# l_z19 = l_zxwy_q4_quanshi_rank(wj1,pl)
# # 4题全市排名
# l_z20 = l_zxwy_q4_benlei_rank(wj1,pl)
# # 4题本类排名
# l_z21 = l_zxwy_q5_point(wj1,pl)
# # 5题分
# l_z22 = l_zxwy_q5_satisfaction_rate(wj1,pl)
# # 5题满意率
# l_z23 = l_zxwy_q5_quanshi_rank(wj1,pl)
# # 5题全市排名
# l_z24 = l_zxwy_q5_benlei_rank(wj1,pl)
# # 5题本类排名
