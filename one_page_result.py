

import xlsxwriter
from one_page import taginonepage,hitinonepage

def find_between(r,first,last):
    try:
        start=r.rindex(first)+len(first)
        end = r.rindex(last,start)
        true_r=r[start:end]
        return true_r
#        try:
#            true_r=int(true_r[::-1])
#            return true_r 
#        except ValueError:
#            return
    except ValueError:
        return
    

workbook = xlsxwriter.Workbook('raw_result.xlsx')
worksheet=workbook.add_worksheet()
row=0
column=0
url='https://archiveofourown.org/tags/search?utf8=%E2%9C%93&query[name]=&query[type]=Freeform&query[canonical]=true'
result=taginonepage(url)
for i in result:
    worksheet.write(row, column, i.get_text())
    row+=1
result=hitinonepage(url)
column=1
row=0
for i in result:
    i=i.get_text()
    i=find_between(i,"(",")")
    try:
        i=int(i)
        print(i)
        worksheet.write(row, column, i)
        row+=1
    except:
        pass

workbook.close()