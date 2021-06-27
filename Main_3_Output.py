import xlrd
import codecs

workbook = xlrd.open_workbook('finale_c.xlsx')
worksheet = workbook.sheets()[0]
file=codecs.open("top_100_c_o.txt","w",'utf-8')
row=0

for row in range(1,101):
    print(int(worksheet.cell(row,0).value))
    if(worksheet.cell_type(row,0)== xlrd.XL_CELL_EMPTY):
        file.write(str(worksheet.cell(row,1).value))
        file.write(": ")
        a=str(int(worksheet.cell(row,4).value))
        file.write(a)       
        file.write(" → " )   
        file.write("榜外") #tranlsation:(drop) from the top 100 list
    elif(int(worksheet.cell(row,0).value)>100 ):
        file.write(str(worksheet.cell(row,1).value))
        file.write(": ")
        a=str(int(worksheet.cell(row,4).value))
        file.write(a)
        file.write(" → " )     
        file.write(str(int(worksheet.cell(row,0).value)))
            
#    row_t=str(row)
    file.write("\n\n")
    row = row+1
    
file.close()
 