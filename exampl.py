import requests
from bs4 import BeautifulSoup

def spider() :
	choice = '2017'

	url = 'http://www.ajou.ac.kr/kr/ajou/notice.jsp'
	source_code = requests.get(url)
	plain_text = source_code.text
	
	soup = BeautifulSoup(plain_text, 'lxml')

	titles = soup.find_all("td", attrs={'class':'td title_comm'})
	writers = soup.find_all("td", attrs={'class':'td al_center'})
	for title in titles:
		if choice in title.find('a').text:
			print(title.find('a').text)
			print(title.find('a')['href'])
			incoming_select_page(url, title.find('a')['href'])
	
	for writer in writers:
		print(writer.text)

#selected page url
def incoming_select_page(url, herl):
	new_url = url+""+herl
	print(new_url)


spider()
