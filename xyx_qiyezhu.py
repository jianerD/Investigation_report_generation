import pandas as pd
import numpy as np


#1
def x_wltzz_total_point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(外来投资者) ", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '%.2f'%(data2.loc[place, 'a3'])




#2
def x_wltzz_category_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(外来投资者) ", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a4'])




#3
def x_wltzz_total_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(外来投资者) ", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a5'])



#4
def x_wltzz_satisfaction(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(外来投资者) ", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '{:.2%}'.format(data2.loc[place, 'a6'])




#1-1
def x_wltzz_1point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(外来投资者) ", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '%.2f'%(data2.loc[place, 'a7'])




#1-2
def x_wltzz_1category_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(外来投资者) ", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a8'])




#1-3
def x_wltzz_1total_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(外来投资者) ", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a9'])




#1-4
def x_wltzz_1satisfaction(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(外来投资者) ", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '{:.2%}'.format(data2.loc[place, 'a10'])



#2-1
def x_wltzz_2point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(外来投资者) ", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '%.2f'%(data2.loc[place, 'a11'])




#2-2
def x_wltzz_2category_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(外来投资者) ", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a12'])




#2-3
def x_wltzz_2total_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(外来投资者) ", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a13'])




#2-4
def x_wltzz_2satisfaction(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(外来投资者) ", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '{:.2%}'.format(data2.loc[place, 'a14'])




#3-1
def x_wltzz_3point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(外来投资者) ", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '%.2f'%(data2.loc[place, 'a15'])



#3-2
def x_wltzz_3category_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(外来投资者) ", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a16'])




#3-3
def x_wltzz_3total_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(外来投资者) ", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a17'])




#3-4
def x_wltzz_3satisfaction(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(外来投资者) ", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '{:.2%}'.format(data2.loc[place, 'a18'])




#4-1
def x_wltzz_4point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(外来投资者) ", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '%.2f'%(data2.loc[place, 'a19'])




#4-2
def x_wltzz_4category_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(外来投资者) ", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a20'])




#4-3
def x_wltzz_4total_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(外来投资者) ", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a21'])




#4-4
def x_wltzz_4satisfaction(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(外来投资者) ", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '{:.2%}'.format(data2.loc[place, 'a22'])




#5-1
def x_wltzz_5point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(外来投资者) ", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '%.2f'%(data2.loc[place, 'a23'])




#5-2
def x_wltzz_5category_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(外来投资者) ", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a24'])



#5-3
def x_wltzz_5total_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(外来投资者) ", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a25'])




#5-4
def x_wltzz_5satisfaction(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("企业主评价(外来投资者) ", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '{:.2%}'.format(data2.loc[place, 'a26'])