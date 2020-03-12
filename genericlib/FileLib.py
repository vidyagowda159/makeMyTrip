class fileData:
    import openpyxl
    def readData(self,sheetname,row,col,filepath):
        obj=self.openpyxl.load_workbook(filepath)
        s=obj.get_sheet_by_name(sheetname)
        res=s.cell(row=row,column=col).value
        return res

    def writeData(self,sheetname,row,col,filepath,data):
        obj=self.openpyxl.load_workbook(filepath)
        s=obj.get_sheet_by_name(sheetname)
        s.cell(row=row,column=col).value=data

    def maxRowCount(self):
        sheet=self.openpyxl.Workbook().active
        return sheet.max_row

    def maxColCount(self):
        from openpyxl import Workbook
        book = Workbook()
        sheet = book.active
        return sheet.max_column

    def xlData(self,sheetname,file):
        objfile = fileData()
        maxRow = objfile.maxRowCount()
        maxCol=objfile.maxColCount()
        data=[]

        for i in range(1, maxRow + 1):
            for j in range(1,maxCol+1):
                data.append(objfile.readData(sheetname, i + 1, j, file))

            return data



