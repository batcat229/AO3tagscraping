import xlsxwriter
from one_page import taginonepage,hitinonepage

def find_between(r,first,last):
    try:
        start=r.rindex(first)+len(first)
        end = r.rindex(last,start)
        true_r=r[start:end]
        return true_r
    except ValueError:
        return
    

workbook = xlsxwriter.Workbook('raw_result1001_2000.xlsx')
worksheet=workbook.add_worksheet()
row=0
column=0
a=2
while a<2001:
    a=str(a)
    url='https://archiveofourown.org/tags/search?page='+a+'&query%5Bcanonical%5D=true&query%5Bname%5D=&query%5Btype%5D=Freeform&utf8=%E2%9C%93'
    a=int(a)
    row=(a-1001)*50+1
    column=0
    result=taginonepage(url)
    for i in result:
        worksheet.write(row, column, i.get_text())
        row+=1
    result=hitinonepage(url)
    column=1
    row=(a-1001)*50+1
    for i in result:
        i=i.get_text()
        i=find_between(i,"(",")")
        try:
            i=int(i)
            worksheet.write(row, column, i)
            row+=1
        except:
            pass
    a+=1
workbook.close()