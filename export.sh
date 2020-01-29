#!/bin/bash
#KEY="XXXXXXXX"
KEY="XXXXXXXXX"
#HOST="localhost:3000"
HOST="https://YOURDOMAIN:3000"
dash="bed-dashboard-b8-27-eb-8d-ae-69-beddot2"
mkdir dashboards 
curl -k -H "Authorization: Bearer $KEY" $HOST/api/dashboards/db/$dash > dashboards/$dash.json 
#curl -k -H "Authorization: Bearer $KEY" $HOST/api/dashboards/db/$dash | sed 's/"id":[0-9]\+,/"id":0,/' | sed 's/\(.*\)}/\1,"overwrite": true}/' > dashboards/$dash.json
