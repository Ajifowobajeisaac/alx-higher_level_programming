#!/usr/bin/env bash
# This script take a URL, send a request to the URL and display the size of the response body

url="$1"

curl -sI $url | grep -oP "(?<=Content-Length: )\d*"
