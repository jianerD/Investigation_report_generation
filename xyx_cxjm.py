
import pandas as pd
import numpy as np

#cs0
def x_csjm_real_point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城乡居民满意度调查总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26", "a27", "a28", "a29"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '%.2f'%(data2.loc[place, 'a3'])


#cs1
def x_csjm_total_point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城乡居民满意度调查总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26", "a27", "a28", "a29"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '%.2f'%(data2.loc[place, 'a4'])


#cs2
def x_csjm_category_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城乡居民满意度调查总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27", "a28", "a29"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a5'])


#cs3
def x_csjm_total_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城乡居民满意度调查总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27", "a28", "a29"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a6'])


#cs4
def x_csjm_satisfaction(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城乡居民满意度调查总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27", "a28", "a29"] 
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '{:.2%}'.format(data2.loc[place, 'a7'])

#cs_c1
def compare_cs1(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城乡居民满意度调查总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27", "a28", "a29"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    a = '%.2f'%(data2.loc[place, 'a4'])
    b = '%.2f'%(83.04-eval(a))
    return b

#cs_ca
def compare_csa(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城乡居民满意度调查总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27", "a28", "a29"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    a = '%.2f'%(data2.loc[place, 'a4'])
    c = '%.2f'%(78.26-eval(a))
    return c

#cs_cc1
def compare_category_cs1(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城乡居民满意度调查总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26", "a27", "a28", "a29"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    if place in ["灵川县", "全州县", "兴安县", "永福县", "平乐县", "荔浦县"]:
        a = data2.iloc[4, 3]-data2.loc[place, 'a4']
        return '%.2f'%(a)
    elif place in ["阳朔县", "灌阳县", "恭城县", "龙胜县", "资源县"]:
        a = data2.iloc[8, 3]-data2.loc[place, 'a4']
        return '%.2f'%(a)
    else:
        a = data2.iloc[13, 3]-data2.loc[place, 'a4']
        return '%.2f'%(a)
    
#cs_cca
def compare_category_csa(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城乡居民满意度调查总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26", "a27", "a28", "a29"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    if place in ["灵川县", "全州县", "兴安县", "永福县", "平乐县", "荔浦县"]:
        a = data2.loc[place, 'a4']-77.16
        return '%.2f'%(a)
    elif place in ["阳朔县", "灌阳县", "恭城县", "龙胜县", "资源县"]:
        a = data2.loc[place, 'a4']-79.49
        return '%.2f'%(a)
    else:
        a = data2.loc[place, 'a4']-78.34
        return '%.2f'%(a)



#nc0
def x_ncjm_real_point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城乡居民满意度调查总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26", "a27", "a28", "a29"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '%.2f'%(data2.loc[place, 'a17'])


#nc1
def x_ncjm_total_point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城乡居民满意度调查总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26", "a27", "a28", "a29"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '%.2f'%(data2.loc[place, 'a18'])


#nc2
def x_ncjm_category_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城乡居民满意度调查总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27", "a28", "a29"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a19'])


#nc3
def x_ncjm_total_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城乡居民满意度调查总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27", "a28", "a29"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a20'])


#nc4
def x_ncjm_satisfaction(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城乡居民满意度调查总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27", "a28", "a29"] 
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '{:.2%}'.format(data2.loc[place, 'a21'])

#nc_c1
def compare_nc1(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城乡居民满意度调查总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27", "a28", "a29"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    a = '%.2f'%(data2.loc[place, 'a18'])
    b = '%.2f'%(80.94-eval(a))
    return b

#nc_ca
def compare_nca(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城乡居民满意度调查总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27", "a28", "a29"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    a = '%.2f'%(data2.loc[place, 'a4'])
    c = '%.2f'%(75.95-eval(a))
    return c

#nc_cc1
def compare_category_nc1(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城乡居民满意度调查总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26", "a27", "a28", "a29"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    if place in ["灵川县", "全州县", "兴安县", "永福县", "平乐县", "荔浦县"]:
        a = data2.iloc[5, 17]-data2.loc[place, 'a18']
        return '%.2f'%(a)
    elif place in ["阳朔县", "灌阳县", "恭城县", "龙胜县", "资源县"]:
        a = data2.iloc[8, 17]-data2.loc[place, 'a18']
        return '%.2f'%(a)
    else:
        a = data2.iloc[13, 17]-data2.loc[place, 'a18']
        return '%.2f'%(a)
    
#nc_cca
def compare_category_nca(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城乡居民满意度调查总结果", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26", "a27", "a28", "a29"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    if place in ["灵川县", "全州县", "兴安县", "永福县", "平乐县", "荔浦县"]:
        a = data2.loc[place, 'a18']-75.05
        return '%.2f'%(a)
    elif place in ["阳朔县", "灌阳县", "恭城县", "龙胜县", "资源县"]:
        a = data2.loc[place, 'a18']-76.60
        return '%.2f'%(a)
    else:
        a = data2.loc[place, 'a18']-76.30
        return '%.2f'%(a)


