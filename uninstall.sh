#!/bin/bash

docker-compose down --rmi all -v --remove-orphans

sudo rm -R ./postgresql/data/
mkdir ./postgresql/data

