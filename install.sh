#!/bin/bash

docker build -t fastapi -f ./fastapi/Dockerfile ./
docker build -t postgresql -f ./postgresql/Dockerfile ./