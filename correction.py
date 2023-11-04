import time
from get_request import simple_get
from bs4 import BeautifulSoup
import xlrd
import xlsxwriter
from retry import retry

def find_between(r,first,last):
    try:
        start=r.index(first)+len(first)
        end = r.index(last,start)
        true_r=r[start:end]
        return true_r
    except ValueError:
        return
    
@retry(Exception,delay=90,tries=5,backoff=2)
def get_counts(url):
    raw_html=simple_get(url)
    html=BeautifulSoup(raw_html, 'html.parser')
    result=html.find_all('h3', attrs={"class":"heading"})
    return result



workbook = xlsxwriter.Workbook('raw_finale_2023.xlsx')
worksheet=workbook.add_worksheet()
date=xlrd.open_workbook('raw_result_2023_2000.xls')
sheet=date.sheets()[0]
r=1
#sheet.nrows
for i in range (1,3000):
    try:
        tag=str(sheet.cell_value(i,0))
        o_count=str(sheet.cell_value(i,1))
        url="https://archiveofourown.org/works/search?work_search%5Bquery%5D=&work_search%5Btitle%5D=&work_search%5Bcreators%5D=&work_search%5Brevised_at%5D=&work_search%5Bcomplete%5D=&work_search%5Bcrossover%5D=&work_search%5Bsingle_chapter%5D=0&work_search%5Bword_count%5D=&work_search%5Blanguage_id%5D=&work_search%5Bfandom_names%5D=&work_search%5Brating_ids%5D=&work_search%5Bcharacter_names%5D=&work_search%5Brelationship_names%5D=&work_search%5Bfreeform_names%5D="+tag+"&work_search%5Bhits%5D=&work_search%5Bkudos_count%5D=&work_search%5Bcomments_count%5D=&work_search%5Bbookmarks_count%5D=&work_search%5Bsort_column%5D=_score&work_search%5Bsort_direction%5D=desc&commit=Search"
        n=get_counts(url)
        t=str(n[1])
        t_count=find_between(t,">"," F")
        worksheet.write(r, 0, tag)
        worksheet.write(r, 1, o_count)
        worksheet.write(r, 2, t_count)
        print(i)
        print(tag)
        print(t_count)
        r=r+1
        time.sleep(6)
    except:
        break
    
print("finished")
workbook.close()