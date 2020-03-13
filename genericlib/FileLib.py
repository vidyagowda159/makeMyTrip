import openpyxl
from openpyxl import Workbook

class fileData:
    filepath_User = r'C:\Users\Vidyashree\PycharmProjects\makeMyTrip\username_pwd.xlsx'
    filepath_flightsheet = r'C:\Users\Vidyashree\PycharmProjects\makeMyTrip\flight_sheet.xlsx'

    def readData(self,sheetname,row,col,filepath):
        obj=openpyxl.load_workbook(filepath)
        s=obj.get_sheet_by_name(sheetname)
        res=s.cell(row=row,column=col).value
        return res

    def writeData(self,sheetname,row,col,filepath,data):
        obj=openpyxl.load_workbook(filepath)
        s=obj.get_sheet_by_name(sheetname)
        s.cell(row=row,column=col).value=data
        obj.save(filepath)

    def maxRowCount(self):
        sheet=openpyxl.Workbook().active
        return sheet.max_row

    def maxColCount(self):
        book = Workbook()
        sheet = book.active
        return sheet.max_column

    def xlReadData(self,sheetname,file):
        objfile = fileData()
        maxRow = objfile.maxRowCount()
        maxCol=objfile.maxColCount()
        data=[]

        for i in range(1, maxRow + 1):
            for j in range(1,maxCol+1):
                data.append(objfile.readData(sheetname, i + 1, j, file))

            return data



