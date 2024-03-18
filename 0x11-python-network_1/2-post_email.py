#!/usr/bin/python3

if __name__ == "__main__":
	import urllib.parse
	import urllib.request
	from sys

	url = sys.argv[1]
	email = sys.argv[2]}

	try:
		data = urllib.parse.urlencode('email': email})
		data = email.encode('ascii')
	with urllib.request.openurl(url, data) as response:
		page = response.read().decode('utf-8')
		print(page)
