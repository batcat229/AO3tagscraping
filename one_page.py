from get_request import simple_get
from bs4 import BeautifulSoup
#
def taginonepage(url):
    raw_html=simple_get(url)
    html=BeautifulSoup(raw_html, 'html.parser')
    result=html.find_all(attrs={"class":"tag"},href=True)
    return result
        


def hitinonepage(url):
    raw_html=simple_get(url)
    html=BeautifulSoup(raw_html, 'html.parser')
    result=html.find_all(attrs={"class":"canonical"})
    return result

        