from get_request import simple_get
from bs4 import BeautifulSoup
import Definition
import string
import time
import xlsxwriter

workbook = xlsxwriter.Workbook('raw_result.xlsx')

First_Characters=list(string.ascii_lowercase)
#First_Characters=["u","z"] #Sample list

for i in First_Characters:
    print(i)
    try:
        worksheet=workbook.add_worksheet(i)
        row=0
        column=0      
        number_of_tags=Definition.total_hit(i) #count the total usage of the tag with word begin with i
        number_of_pages=Definition.count_pages(int(number_of_tags),50)#count the page of the tag with word begin with i
        number_of_pages=number_of_pages+1
        for j in range(1,number_of_pages):          
            print("page: "+str(j)+"/"+str(number_of_pages)) #notice
            url="https://archiveofourown.org/tags/search?page="+str(j)+"&query%5Bcanonical%5D=true&query%5Bname%5D="+i+"%2A&query%5Btype%5D=Freeform&utf8=%E2%9C%93"
            tag_with_usage_in_the_page=Definition.hitinonepage(url)
            time.sleep(5) #reduce the possibility of refusion from AO3, but I also set a retry decorator to prevent unexpect stop
            for k in tag_with_usage_in_the_page:
                text=str(k)
                usage_of_the_tag=Definition.find_between_r(text,"(",")")
                usage_of_the_tag=int(usage_of_the_tag)
                if(usage_of_the_tag >= 200): #only record the tag with more than 200 usage, just to save memory
                    column=0  
                    k=k.find('a') #find the tag object which only contains the name of the tag
                    worksheet.write(row, column, k.get_text())
                    column=1
                    worksheet.write(row, column, usage_of_the_tag)
                    row+=1

                    
    except:
        print('finish')
        break
    
    
workbook.close()