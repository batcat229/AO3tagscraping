from get_request import simple_get
from bs4 import BeautifulSoup
from retry import retry

#Definitions

@retry(Exception,delay=90,tries=5,backoff=2)
def hitinonepage(url:str)->list:
    count=1
    try:
        raw_html=simple_get(url)
        html=BeautifulSoup(raw_html, 'html.parser')
        result=html.find_all(attrs={"class":"canonical"})
        return result
    except:
        print("Tring the "+ str(count)+ " times")
        count=count+1
        raise Exception("Fail")
#Input url of the search website of AO3 and output all the tags and hits in that page


def find_between_r(text:str,first_letter:str,last_letter:str)->str:
    try:
        start=text.rindex(first_letter)+len(first_letter)
        end = text.rindex(last_letter,start)
        true_r=text[start:end]
        return true_r
    except ValueError:
        return        
#Input text, first letter,last letter and output the last text between the first letter and the last letter
        

def find_between(text:str,first_letter:str,last_letter:str)->str:
    try:
        start=text.index(first_letter)+len(first_letter)
        end = text.index(last_letter,start)
        true_r=text[start:end]
        return true_r
    except ValueError:
        return        
#Input text, first letter,last letter and output the text between the first letter and the last letter


def total_hit(character:str)->str:
    url='https://archiveofourown.org/tags/search?page=1&query%5Bcanonical%5D=true&query%5Bname%5D='+character+'%2A&query%5Btype%5D=Freeform&utf8=%E2%9C%93'
    raw_html=simple_get(url)
    html=BeautifulSoup(raw_html, 'html.parser')
    hit_tag=html.find_all(attrs={"title":"Tag search results help"})
    r=hit_tag[0].find_parent('h3')
    raw=r.text.split()
    result=raw[0]
    return result
#Inout a character and output how many canonical words begin with the character

    
def count_pages(total_tag:int,page_tag:int)->int:
    a=total_tag//page_tag+1
    return a
#Input the total number of the tags and how many tags were in one page, output how many pages are there


@retry(Exception,delay=90,tries=5,backoff=2)
def get_counts(url):
    raw_html=simple_get(url)
    html=BeautifulSoup(raw_html, 'html.parser')
    result=html.find_all('h3', attrs={"class":"heading"})
    return result
#Input the url of the tag and return all the 'h3' tag object (including the true usage of the tags) 
    
