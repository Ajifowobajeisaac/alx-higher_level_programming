import urllib.request
with urllib.request.urlopen('https://alx-intranet.htbn.io/status') as response:
	html = response.read()
