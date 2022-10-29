#!/bin/bash

docker run -d -v $(pwd)/fastapi/app/:/app -p 8000:8000 --name fastapi_tests fastapi
docker run -d -v $(pwd)/postgresql/data/:/var/lib/postgresql/data -p 5432:5432 -e POSTGRES_PASSWORD=admin --name postgresql_tests postgresql
