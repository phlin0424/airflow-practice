#!/bin/sh
# Transfer all the raw files under ./raw
aws --endpoint-url http://localhost:9000 s3 cp --recursive ./data/.raw "s3://datalake/uscrn/$(date '+%Y-%m-%d')" --profile etluser