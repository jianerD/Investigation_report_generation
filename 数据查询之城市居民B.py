# wj = r'C:\Users\丁健一\Desktop\政府满意度项目\自动报告生成\报告生成项目\datasets\后续数据\提交1.2022年度桂林市县（市、区）社会评价统计结果.xls'
# pl = "灵川县"
# 社会评价数据查询之城市居民A卷

# 总得分
import pandas as pd

def q_csjm_B_total_point(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城市居民评价 B卷", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17","a18", "a19", "a20", "a21", "a22"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a3'],2)


# 本类排名

def q_csjm_B_rank1(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城市居民评价 B卷", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17","a18", "a19", "a20", "a21", "a22"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a4'],2)


# 全市排名

def q_csjm_B_rank2(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城市居民评价 B卷", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17","a18", "a19", "a20", "a21", "a22"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a5'],2)



# 满意度

def q_csjm_B_dos(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城市居民评价 B卷", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17","a18", "a19", "a20", "a21", "a22"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a6'],2)


# 问题1得分

def q_csjm_B_q1_score(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城市居民评价 B卷", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17","a18", "a19", "a20", "a21", "a22"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a7'],2)


# 问题1本类排名

def q_csjm_B_q1_rank1(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城市居民评价 B卷", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17","a18", "a19", "a20", "a21", "a22"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a8'],2)


# 问题1全市排名

def q_csjm_B_q1_rank2(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城市居民评价 B卷", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17","a18", "a19", "a20", "a21", "a22"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a9'],2)



# 问题1满意度

def q_csjm_B_q1_dos(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城市居民评价 B卷", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17","a18", "a19", "a20", "a21", "a22"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a10'],2)


# 问题2得分

def q_csjm_B_q2_score(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城市居民评价 B卷", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17","a18", "a19", "a20", "a21", "a22"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a11'],2)


# 问题2本类排名

def q_csjm_B_q2_rank1(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城市居民评价 B卷", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17","a18", "a19", "a20", "a21", "a22"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a12'],2)


# 问题2全市排名

def q_csjm_B_q2_rank2(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城市居民评价 B卷", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17","a18", "a19", "a20", "a21", "a22"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a13'],2)



# 问题2满意度

def q_csjm_B_q2_dos(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城市居民评价 B卷", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17","a18", "a19", "a20", "a21", "a22"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a14'],2)


# 问题3得分

def q_csjm_B_q3_score(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城市居民评价 B卷", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17","a18", "a19", "a20", "a21", "a22"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a15'],2)


# 问题3本类排名

def q_csjm_B_q3_rank1(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城市居民评价 B卷", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17","a18", "a19", "a20", "a21", "a22"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a16'],2)


# 问题3全市排名

def q_csjm_B_q3_rank2(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城市居民评价 B卷", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17","a18", "a19", "a20", "a21", "a22"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a17'],2)



# 问题3满意度

def q_csjm_B_q3_dos(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城市居民评价 B卷", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17","a18", "a19", "a20", "a21", "a22"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a18'],2)


# 问题4得分

def q_csjm_B_q4_score(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城市居民评价 B卷", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17","a18", "a19", "a20", "a21", "a22"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a19'],2)


# 问题4本类排名

def q_csjm_B_q4_rank1(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城市居民评价 B卷", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17","a18", "a19", "a20", "a21", "a22"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a20'],2)


# 问题4全市排名

def q_csjm_B_q4_rank2(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城市居民评价 B卷", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17","a18", "a19", "a20", "a21", "a22"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a21'],2)



# 问题4满意度

def q_csjm_B_q4_dos(file_name, place: str):
    data1 = pd.ExcelFile(file_name)
    data2 = pd.DataFrame(data1.parse("城市居民评价 B卷", header=4))
    d_col = ["a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14", "a15",
             "a16", "a17","a18", "a19", "a20", "a21", "a22"]
    data2.columns = d_col
    data2.set_index('a1', inplace=True)
    return round(data2.loc[place, 'a22'],2)
