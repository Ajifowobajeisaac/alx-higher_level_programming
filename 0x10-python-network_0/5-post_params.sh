#!/bin/bash
# sends a getrequest with a specified header varaible to a URL and displays the body of the responsee
curl -sd "email=test@gmail.com" -d "subject=I will always be here for PLD" $1
