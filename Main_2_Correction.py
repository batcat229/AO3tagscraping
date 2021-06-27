# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 14:44:42 2021

@author: Marry
"""

import time
from get_request import simple_get
from bs4 import BeautifulSoup
import xlrd
import xlsxwriter
import Definition
import datetime

#Note from author:
#Please merge and sort the raw result ('raw_result.xlsx') manual (in Excel)
#and delete the duplicate tags before excecuting the correction
#It's convenient esaier (and safer, because you can see it) to do this out of python.
#And I'm still trying to make a pure dummy program


workbook = xlsxwriter.Workbook('raw_finale.xlsx')
data=xlrd.open_workbook('raw_result.xlsx')
worksheet=workbook.add_worksheet()

#workbook = xlsxwriter.Workbook('sample_corrected.xlsx')
#data=xlrd.open_workbook('sample.xlsx')  
#The sample is the raw result from 2020

sheet=data.sheets()[0]

start_date=datetime.date(2021,6,27)
end_date=datetime.date(2020,6,28)
#set the time zone, but only in days

today=datetime.date.today()
start_delta=today-start_date
start_delta=str(start_delta.days)
end_delta=today-end_date
end_delta=str(end_delta.days)
delta=start_delta+'-'+end_delta+'+days'

r=1
for i in range (1,sheet.nrows):
#for i in range(1,5):  #sample
    print(str(i)+"/"+str(sheet.nrows))
    try:
        tag_name=str(sheet.cell_value(i,0))
        raw_count=str(sheet.cell_value(i,1))
        url="https://archiveofourown.org/works/search?utf8=%E2%9C%93&commit=Search&work_search%5Bquery%5D=&work_search%5Btitle%5D=&work_search%5Bcreators%5D=&work_search%5Brevised_at%5D="+delta+"&work_search%5Bcomplete%5D=&work_search%5Bcrossover%5D=&work_search%5Bsingle_chapter%5D=0&work_search%5Bword_count%5D=&work_search%5Blanguage_id%5D=&work_search%5Bfandom_names%5D=&work_search%5Brating_ids%5D=&work_search%5Bcharacter_names%5D=&work_search%5Brelationship_names%5D=&work_search%5Bfreeform_names%5D="+tag_name+"&work_search%5Bhits%5D=&work_search%5Bkudos_count%5D=&work_search%5Bcomments_count%5D=&work_search%5Bbookmarks_count%5D=&work_search%5Bsort_column%5D=_score&work_search%5Bsort_direction%5D=desc"
        dummy=Definition.get_counts(url)
        dummy_2=str(dummy[1])
        print(dummy_2)
        true_count=Definition.find_between(dummy_2,">"," F")
        print(true_count)
        worksheet.write(r, 0, tag_name)
        worksheet.write(r, 1, raw_count)
        worksheet.write(r, 2, true_count)
        r=r+1
        time.sleep(5)
    except:
        break
    
print("finished")
workbook.close()