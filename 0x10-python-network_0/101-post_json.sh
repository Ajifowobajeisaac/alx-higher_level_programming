#!/bin/bash
# sends a JSON POST request to a url and displays the body of the response
curl -H "Content-Type: application/json" -d @{$2} "$1"
