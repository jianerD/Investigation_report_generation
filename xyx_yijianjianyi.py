
import pandas as pd
import numpy as np


#1
def x_qzyjjy_total_point(file_name, place: str):
    try:
        data1 = pd.ExcelFile(file_name)
        data2 = pd.DataFrame(data1.parse("群众意见建议落实情况（绩效奖惩加分）", header=4))
        d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
                     "a16", "a17"]
        data2.columns = d_col
        data2.set_index('a1', inplace=True)
        return '%.2f'%(data2.loc[place, 'a3'])
        pass
    except ValueError as e:
        return "Nan"



#2
def x_qzyjjy_category_rank(file_name, place: str):
    try:
        data1 = pd.ExcelFile(file_name)
        data2 = pd.DataFrame(data1.parse("群众意见建议落实情况（绩效奖惩加分）", header=4))
        d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
                 "a16", "a17"]
        data2.columns = d_col
        data2.set_index('a1', inplace=True)
        return round(data2.loc[place, 'a4'])
        pass
    except ValueError as e:
        return "Nan"


#3
def x_qzyjjy_total_rank(file_name, place: str):
    try:
        data1 = pd.ExcelFile(file_name)
        data2 = pd.DataFrame(data1.parse("群众意见建议落实情况（绩效奖惩加分）", header=4))
        d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
                 "a16", "a17"]
        data2.columns = d_col
        data2.set_index('a1', inplace=True)
        return round(data2.loc[place, 'a5'])
        pass
    except ValueError as e:
        return "Nan"



#4
def x_qzyjjy_satisfaction(file_name, place: str):
    try:
        data1 = pd.ExcelFile(file_name)
        data2 = pd.DataFrame(data1.parse("群众意见建议落实情况（绩效奖惩加分）", header=4))
        d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
                 "a16", "a17"]
        data2.columns = d_col
        data2.set_index('a1', inplace=True)
        return '{:.2%}'.format(data2.loc[place, 'a6'])
        pass
    except ValueError as e:
        return "Nan"


#1-1
def x_qzyjjy_1yes(file_name, place: str):
    try:
        data1 = pd.ExcelFile(file_name)
        data2 = pd.DataFrame(data1.parse("群众意见建议落实情况（绩效奖惩加分）", header=4))
        d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
                 "a16", "a17"]
        data2.columns = d_col
        data2.set_index('a1', inplace=True)
        return round(data2.loc[place, 'a7'])
        pass
    except ValueError as e:
        return "Nan"


#1-2
def x_qzyjjy_1no(file_name, place: str):
    try:
        data1 = pd.ExcelFile(file_name)
        data2 = pd.DataFrame(data1.parse("群众意见建议落实情况（绩效奖惩加分）", header=4))
        d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
                 "a16", "a17"]
        data2.columns = d_col
        data2.set_index('a1', inplace=True)
        return round(data2.loc[place, 'a8'])
        pass
    except ValueError as e:
        return "Nan"


#2-1
def x_qzyjjy_2yes(file_name, place: str):
    try:
        data1 = pd.ExcelFile(file_name)
        data2 = pd.DataFrame(data1.parse("群众意见建议落实情况（绩效奖惩加分）", header=4))
        d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
                 "a16", "a17"]
        data2.columns = d_col
        data2.set_index('a1', inplace=True)
        return round(data2.loc[place, 'a9'])
        pass
    except ValueError as e:
        return "Nan"



#2-2
def x_qzyjjy_2no(file_name, place: str):
    try:
        data1 = pd.ExcelFile(file_name)
        data2 = pd.DataFrame(data1.parse("群众意见建议落实情况（绩效奖惩加分）", header=4))
        d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
                 "a16", "a17"]
        data2.columns = d_col
        data2.set_index('a1', inplace=True)
        return round(data2.loc[place, 'a10'])
        pass
    except ValueError as e:
        return "Nan"



#3-1
def x_qzyjjy_3satisfaction(file_name, place: str):
    try:
        data1 = pd.ExcelFile(file_name)
        data2 = pd.DataFrame(data1.parse("群众意见建议落实情况（绩效奖惩加分）", header=4))
        d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
                 "a16", "a17" ]
        data2.columns = d_col
        data2.set_index('a1', inplace=True)
        return '{:.2%}'.format(data2.loc[place, 'a11'])
        pass
    except ValueError as e:
        return "Nan"


#3-2
def x_qzyjjy_3category_rank(file_name, place: str):
    try:
        data1 = pd.ExcelFile(file_name)
        data2 = pd.DataFrame(data1.parse("群众意见建议落实情况（绩效奖惩加分）", header=4))
        d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
                 "a16", "a17" ]
        data2.columns = d_col
        data2.set_index('a1', inplace=True)
        return round(data2.loc[place, 'a12'])
        pass
    except ValueError as e:
        return "Nan"


#3-3
def x_qzyjjy_3total_rank(file_name, place: str):
    try:
        data1 = pd.ExcelFile(file_name)
        data2 = pd.DataFrame(data1.parse("群众意见建议落实情况（绩效奖惩加分）", header=4))
        d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
                 "a16", "a17" ]
        data2.columns = d_col
        data2.set_index('a1', inplace=True)
        return round(data2.loc[place, 'a13'])
        pass
    except ValueError as e:
        return "Nan"


#4-1
def x_qzyjjy_4satisfaction(file_name, place: str):
    try:
        data1 = pd.ExcelFile(file_name)
        data2 = pd.DataFrame(data1.parse("群众意见建议落实情况（绩效奖惩加分）", header=4))
        d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
                 "a16", "a17" ]
        data2.columns = d_col
        data2.set_index('a1', inplace=True)
        return '{:.2%}'.format(data2.loc[place, 'a14'])
        pass
    except ValueError as e:
        return "Nan"


#4-1
def x_qzyjjy_4satisfaction_number(file_name, place: str):
    try:
        data1 = pd.ExcelFile(file_name)
        data2 = pd.DataFrame(data1.parse("群众意见建议落实情况（绩效奖惩加分）", header=4))
        d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
                 "a16", "a17" ]
        data2.columns = d_col
        data2.set_index('a1', inplace=True)
        return round(data2.loc[place, 'a15'])
        pass
    except ValueError as e:
        return "Nan"


#4-3
def x_qzyjjy_4category_rank(file_name, place: str):
    try:
        data1 = pd.ExcelFile(file_name)
        data2 = pd.DataFrame(data1.parse("群众意见建议落实情况（绩效奖惩加分）", header=4))
        d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
                 "a16", "a17" ]
        data2.columns = d_col
        data2.set_index('a1', inplace=True)
        return round(data2.loc[place, 'a16'])
        pass
    except ValueError as e:
        return "Nan"


#4-4
def x_qzyjjy_4total_rank(file_name, place: str):
    try:
        data1 = pd.ExcelFile(file_name)
        data2 = pd.DataFrame(data1.parse("群众意见建议落实情况（绩效奖惩加分）", header=4))
        d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
                 "a16", "a17" ]
        data2.columns = d_col
        data2.set_index('a1', inplace=True)
        return round(data2.loc[place, 'a17'])
        pass
    except ValueError as e:
        return "Nan"




