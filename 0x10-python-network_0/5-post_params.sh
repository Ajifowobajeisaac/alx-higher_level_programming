#!/bin/bash
# sends a post reqeust with data
curl -sd "email=test@gmail.com" -d "subject=I will always be here for PLD" $1
