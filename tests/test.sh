#!/bin/bash

export PG_HOST=127.0.0.1
export PG_PORT=5432
export PG_USER=test
export PG_PASSWORD=test
export PG_DBNAME=postgres
export SECRET_KEY=4o7wrqsup*pc*m_etd$mu$8klfl2r$l1_073a+-j_tkvq9a+b7 # TODO
export MINIO_ACCESS_KEY_ID=user
export MINIO_SECRET_ACCESS_KEY=password
export MINIO_STORAGE_BUCKET_NAME=static
export MINIO_API=http://127.0.0.1:9000
python3 manage.py test $1
