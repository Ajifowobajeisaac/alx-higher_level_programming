#!/usr/bin/python3
"""
- sript takes an url and an email
- sends a post request to the url
- with the email as the passed parameter.
- email must be sent in an email variable
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
