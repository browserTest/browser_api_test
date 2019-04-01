import xlrd
from config.config import *


"""获取execl中所有数据"""
def get_excel_all_data(data_file_name, sheet_name):

    #新建一个空的列表，存放所有数据
    data_list = []


    #打开excel并获取其数据
    get_execl = xlrd.open_workbook(data_file_name)
    get_sheet = get_execl.sheet_by_name(sheet_name)

    #获取当前sheet页标题栏
    get_header = get_sheet.row_values(0)

    #获取到当前sheet页所有数据
    for i in range(1, get_sheet.nrows):
        even_row_data = dict(zip(get_header, get_sheet.row_values(i)))
        data_list.append(even_row_data)

    return data_list


"""根据用例名称获取对应的数据"""
def get_need_data(data_list, case_name):
    for i in data_list:
        if case_name == i['case_name']:
            return i

