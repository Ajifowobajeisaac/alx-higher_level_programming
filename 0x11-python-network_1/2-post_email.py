#!/usr/bin/python3
"""
- takes an url and an email.
- sends a post request to the url.
- with the email as the passed parameter.
- displays the body of the respones.
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
