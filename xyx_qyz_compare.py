import pandas as pd
import numpy as np


def compare_1(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(总表)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    a = '%.2f'%(data2.loc[place, 'a4'])
    b = '%.2f'%(90-eval(a))
    return b


def compare_a(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(总表)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    a = '%.2f'%(data2.loc[place, 'a4'])
    c = '%.2f'%(85.72-eval(a))
    return c

  
def compare_category_1(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(总表)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26", "a27"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    if place in ["灵川县", "全州县", "兴安县", "永福县", "平乐县", "荔浦县"]:
        a = data2.iloc[0, 3]-data2.loc[place, 'a4']
        return '%.2f'%(a)
    elif place in ["阳朔县", "灌阳县", "恭城县", "龙胜县", "资源县"]:
        a = data2.iloc[8, 3]-data2.loc[place, 'a4']
        return '%.2f'%(a)
    else:
        a = data2.iloc[16, 3]-data2.loc[place, 'a4']
        return '%.2f'%(a)
    
    
def compare_category_a(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(总表)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26", "a27"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    if place in ["灵川县", "全州县", "兴安县", "永福县", "平乐县", "荔浦县"]:
        a = data2.loc[place, 'a4']-85.76
        return '%.2f'%(a)
    elif place in ["阳朔县", "灌阳县", "恭城县", "龙胜县", "资源县"]:
        a = data2.loc[place, 'a4']-83.32
        return '%.2f'%(a)
    else:
        a = data2.loc[place, 'a4']-86.50
        return '%.2f'%(a)