#!/bin/bash
# sends a delete request to a URL and displays the body of the responsee
curl -sX OPTIONS -i $1 | grep -oP '(?<=Allow: )[^/r/n]*'
