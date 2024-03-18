#!/usr/bin/python3
"""
- Takes a url and an email.
- Sends a POST request to the url with the email as parameter.
"""
import urllib.parse
import urllib.request
from sys

if __name__ == "__main__":

	url = sys.argv[1]
	email = sys.argv[2]}


	data = urllib.parse.urlencode('email': email})
	data = email.encode('ascii')
	with urllib.request.openurl(url, data) as response:
		page = response.read().decode('utf-8')
		print(page)
