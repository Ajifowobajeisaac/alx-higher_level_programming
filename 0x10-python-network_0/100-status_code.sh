#!/bin/bash
# sends a get to a URL and displays the status of the responsee
curl -sI $1 | grep -oP "(?<=HTTP/1.1 )\d*"
