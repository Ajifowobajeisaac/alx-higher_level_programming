#!/bin/bash
# sends a request to the URL and display the size of the response body
curl -sI $1 | grep -oP "(?<=Content-Length: )\d*"
