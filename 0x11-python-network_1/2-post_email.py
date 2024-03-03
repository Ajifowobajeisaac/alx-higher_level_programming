#!/usr/bin/python3
"""
- Takes a url and an email
- Sends a POST request to the url with the email as parameter
"""

if __name__ == "__main__":
	import urllib
	from sys import argv

	url = argv[1]
	emails = {'email' : argv[2]}

	email = urllib.parse.urlencode(emails)
	email = email.encode('utf-8')
	req = urllib.request.Request(url, email)
	with urllib.request.openurl(req) as response:
		page = response.read()
		print(page)
