#!/usr/bin/python3
""" A script that
- fetches a site
- uses urlib package
"""

if __name__ == '__main__':


	import urllib.request
	with urllib.request.urlopen('https://alx-intranet.htbn.io/status') as res:
		content = res.read()

		print("Body response:")
		print("\t- type:", type(html))
		print("\t- content:", html)
		print("\t- utf8 content:", html.decode('utf-8'))
