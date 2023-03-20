
import pandas as pd
import numpy as np

def l_12345_zhibiao_point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("落实整改评价（12345热线指标考核）", header=2))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27","a28","a29"]
    data2.columns = d_col
    data2.set_index('a0', inplace=True)
    return round(data2.loc[place, 'a26'],2)
     


def l_12345_zhibiao_rank(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("落实整改评价（12345热线指标考核）", header=2))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17",
             "a18", "a19", "a20", "a21", "a22", "a23", "a24", "a25", "a26","a27","a28","a29"]
    data2.columns = d_col
    data2.set_index('a0', inplace=True)
    return round(data2.loc[place, 'a23'])