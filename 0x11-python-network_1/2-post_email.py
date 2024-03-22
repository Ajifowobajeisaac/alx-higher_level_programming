#!/usr/bin/python3
"""
- Takes a url and an email.
- Sends a POST request to the url with the email as parameter.
"""

if __name__ == "__main__":
    import urllib.parse
    import urllib.request
    import sys

    url = sys.argv[1]
    value = sys.argv[2]}
    data = urllib.parse.urlencode({'email': value}).encode('ascii')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        page = response.read().decode('utf-8')
        print(page)
