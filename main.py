import requests
from bs4 import BeautifulSoup


# 본인 SP_LOGIN_SESSION 값
tmp = open('login_cookie.txt', 'r')
login_cookie = tmp.read()	
tmp.close()

user_agent = 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'
headers = {'User-Agent': user_agent}
dummy_cookies = {'SP_LOGIN_SESSION' : login_cookie}


def get_soup(url):
	req = requests.get(url, cookies=dummy_cookies, headers=headers)
	soup = BeautifulSoup(req.content, 'html.parser')
	return soup


def get_page_count():
	url = "https://g12017647.sp.pf.mbga.jp/?url=http%3A%2F%2Fm.i-sidem.idolmaster.jp%2Ffriend%2F"
	soup = get_soup(url)
	page = int(soup.select('div.direct-pager>a')[-1].get_text())
	load_page(page)

def load_page(page):
	for i in range(1, page + 1):
		url = f"http://g12017647.sp.pf.mbga.jp/?url=http%3A%2F%2Fm.i-sidem.idolmaster.jp%2Ffriend%2Findex%2Fmodified%2Fasc%2F{i}%3Fopensocial_app_id%3D12017647%26opensocial_viewer_id%3D165431357%26opensocial_owner_id%3D165431357%26ah%3D805542e458"
		soup = get_soup(url)
		write_info(soup)

def write_info(soup):
	friend_info = soup.find_all('span', class_='va-middle')
	num = 0
	for i in range(0, 10):
		try:
			s = friend_info[num].get_text() + '/' + friend_info[num + 1].get_text() + '\n'
			num += 8
			f.write(s)
		except IndexError:
			break

if __name__ == "__main__":
	f = open('list.txt','w')
	get_page_count()
	f.close()




