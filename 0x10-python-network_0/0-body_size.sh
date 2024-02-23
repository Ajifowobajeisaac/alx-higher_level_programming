#!/bin/bash
# This script take a URL, send a request to the URL and display the size of the response body
curl -sI $1 | grep -oP "(?<=Content-Length: )\d*"
