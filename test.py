import requests
from bs4 import BeautifulSoup

q="파티장"
searchpage = requests.get('http://www.inven.co.kr/board/ff14/4485?name=subjcont&keyword={}'.format(q))
bsoup = BeautifulSoup(searchpage.content, 'html.parser')
message = ""
results = bsoup.findAll("a", attrs={"class":"sj_ln"})