#!/bin/bash
# sends a JSON POST request to a url and displays the body of the response
curl -sH "Content-Type: application/json" -d @"$2" "$1"
