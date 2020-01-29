#!/bin/bash
KEY="XXXXXXXXXXXXXX"
HOST="localhost:3000"
dash=$1
curl -i -H "Content-Type: application/json" -H "Authorization: Bearer $KEY" -X POST $HOST/api/dashboards/db -d @dashboards/$dash.json

