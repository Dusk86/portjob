# 读取excel表格数据
# xls: xlrd/xlsx：openpyxl
import xlrd

"""
sheet_names(): 获取所有sheet页名
sheet_by_index:根据所在的下标获取sheet页
sheet_by_name():根据名字获取sheet页
sheets：获取一个Excel文件中所有的sheet表格
nrows: 获取表格的行数
ncols:获取表格的列数

Cell: 
sheet.cell(row,col): 获取指定行和列的 cell对象
sheet.row_slice(row,start_col,end_col):指定 行的 某几列的 cell对象
sheet.col_slice(col,start_row,end_row):获取指定列的 某几行cell对象
sheet.cell_value(row,col):获取指定行和列的值
sheet.row_values(row,start_col,end_col):获取指定行的某几列的值
sheet.col_values(col,start_row,end_row):获取指定列的某几行的值
"""

class MyExcel:
    # 读取表格数据
    def read_excel_sheet(self, file, sheet_name):
        li = []
        # 打开excel文件
        wb = xlrd.open_workbook(filename=file)
        # 获取所有工作表名称
        sheet_names = wb.sheet_names()
        # 判断输入的表名是否实际存在于excel内
        if sheet_name not in sheet_names:
            print('ERROR!!!\n输入表名错误，输入表名为：{} 实际表名为：{}'.format(sheet_name, sheet_names))
        # 通过工作表名称获取某张表格
        sheet_data = wb.sheet_by_name(sheet_name)
        # 获取表格内第二行到最后一行数据
        for i in range(1, sheet_data.nrows):  # 获取总行数
            d = []
            # 遍历列数据
            for j in range(0, sheet_data.ncols):  # 获取总列数
                # 将每一列的行数据存入数组d中
                d = sheet_data.row_values(i)
            # 向li中添加数据
            li.append(d)
        return li






