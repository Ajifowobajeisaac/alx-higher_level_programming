#!/bin/bash
# sends a getrequest with a specified header varaible to a URL and displays the body of the responsee
curl -sH "X-School-User-Id: 98" $1
