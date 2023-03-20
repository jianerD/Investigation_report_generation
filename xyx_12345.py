import pandas as pd
import numpy as np


#0
def x_12345_real_point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("落实整改评价（12345热线）", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21" ]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '%.2f'%(data2.loc[place, 'a3'])


#1
def x_12345_total_point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("落实整改评价（12345热线）", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21" ]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '%.2f'%(data2.loc[place, 'a4'])



#2
def x_12345_category_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("落实整改评价（12345热线）", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21" ]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a5'])



#3
def x_12345_total_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("落实整改评价（12345热线）", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21" ]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a6'])



#4
def x_12345_satisfaction(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("落实整改评价（12345热线）", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21" ]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '{:.2%}'.format(data2.loc[place, 'a7'])



#1-1
def x_12345_yes(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("落实整改评价（12345热线）", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21" ]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a8'])



#1-2
def x_12345_no(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("落实整改评价（12345热线）", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21" ]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a9'])


#2-1
def x_12345_2point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("落实整改评价（12345热线）", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21" ]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '%.2f'%(data2.loc[place, 'a10'])



#2-2
def x_12345_2category_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("落实整改评价（12345热线）", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21" ]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a11'])



#2-3
def x_12345_2total_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("落实整改评价（12345热线）", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21" ]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a12'])



#2-4
def x_12345_2satisfaction(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("落实整改评价（12345热线）", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21" ]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '{:.2%}'.format(data2.loc[place, 'a13'])



#3-1
def x_12345_3point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("落实整改评价（12345热线）", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21" ]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '%.2f'%(data2.loc[place, 'a14'])



#3-2
def x_12345_3category_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("落实整改评价（12345热线）", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21" ]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a15'])



#3-3
def x_12345_3total_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("落实整改评价（12345热线）", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21" ]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a16'])



#3-4
def x_12345_3satisfaction(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("落实整改评价（12345热线）", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21" ]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '{:.2%}'.format(data2.loc[place, 'a17'])



#4-1
def x_12345_4point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("落实整改评价（12345热线）", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21" ]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '%.2f'%(data2.loc[place, 'a18'])



#4-2
def x_12345_4category_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("落实整改评价（12345热线）", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21" ]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a19'])



#4-3
def x_12345_4total_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("落实整改评价（12345热线）", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21" ]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a20'])



#4-4
def x_12345_4satisfaction(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("落实整改评价（12345热线）", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21" ]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return '{:.2%}'.format(data2.loc[place, 'a21'])