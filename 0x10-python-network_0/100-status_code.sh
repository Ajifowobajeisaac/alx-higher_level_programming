#!/bin/bash
# sends a get to a URL and displays the status of the responsee
curl -o /dev/null -s -w "%{http_code}" $1
