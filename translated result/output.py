import xlrd
import codecs

workbook = xlrd.open_workbook('2000_F.xlsx')
worksheet = workbook.sheet_by_name("Sheet1")
file=codecs.open("2000.txt","w",'utf-8')
row=1

while worksheet.cell(row,0).value != xlrd.empty_cell.value:
    row_t=str(row)
    try:
        L=(row_t+". "+worksheet.cell(row,0).value+ ": "+ worksheet.cell(row,1).value+"\n")
        file.write(L)
        if worksheet.cell(row,2).value != xlrd.empty_cell.value:
            file.writelines("【注释："+ worksheet.cell(row,2).value+"】"+"\n")    
        file.writelines("\n")
        row = row+1
    except:
        break
    
file.close()
