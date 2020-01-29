#!/bin/bash
KEY="XXXXXXXXX"
#HOST="localhost:3000"
HOST="https://YOURDOMAIN:3000"
dash="DASHBOARD NAME"
mkdir dashboards 
curl -k -H "Authorization: Bearer $KEY" $HOST/api/dashboards/db/$dash > dashboards/$dash.json 
