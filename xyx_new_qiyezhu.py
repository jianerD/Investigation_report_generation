import pandas as pd
import numpy as np


#
def x_qyz_real_point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(总表)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '%.2f'%(data2.loc[place, 'a3'])


#1
def x_qyz_total_point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(总表)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '%.2f'%(data2.loc[place, 'a4'])



#2
def x_qyz_category_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(总表)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a5'])



#3
def x_qyz_total_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(总表)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a6'])



#4
def x_qyz_satisfaction(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(总表)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '{:.2%}'.format(data2.loc[place, 'a7'])



#1-1
def x_qyz_1point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(总表)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '%.2f'%(data2.loc[place, 'a8'])



#1-2
def x_qyz_1category_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(总表)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a9'])



#1-3
def x_qyz_1total_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(总表)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a10'])



#1-4
def x_qyz_1satisfaction(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(总表)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '{:.2%}'.format(data2.loc[place, 'a11'])


#2-1
def x_qyz_2point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(总表)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '%.2f'%(data2.loc[place, 'a12'])



#2-2
def x_qyz_2category_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(总表)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a13'])



#2-3
def x_qyz_2total_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(总表)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a14'])



#2-4
def x_qyz_2satisfaction(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(总表)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '{:.2%}'.format(data2.loc[place, 'a15'])



#3-1
def x_qyz_3point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(总表)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '%.2f'%(data2.loc[place, 'a16'])



#3-2
def x_qyz_3category_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(总表)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a17'])



#3-3
def x_qyz_3total_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(总表)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a18'])



#3-4
def x_qyz_3satisfaction(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(总表)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '{:.2%}'.format(data2.loc[place, 'a19'])



#4-1
def x_qyz_4point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(总表)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '%.2f'%(data2.loc[place, 'a20'])



#4-2
def x_qyz_4category_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(总表)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a21'])



#4-3
def x_qyz_4total_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(总表)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a22'])



#4-4
def x_qyz_4satisfaction(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(总表)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '{:.2%}'.format(data2.loc[place, 'a23'])



#5-1
def x_qyz_5point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(总表)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '%.2f'%(data2.loc[place, 'a24'])



#5-2
def x_qyz_5category_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(总表)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a25'])



#5-3
def x_qyz_5total_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(总表)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a26'])



#5-4
def x_qyz_5satisfaction(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(总表)", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '{:.2%}'.format(data2.loc[place, 'a27'])