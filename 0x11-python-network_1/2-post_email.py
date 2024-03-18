#!/usr/bin/python3
"""A script that:
- takes in a URL
- sends a POST request to the passed URL
- takes email as a parameter
- displays the body of the response
"""
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
