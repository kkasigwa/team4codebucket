#!/bin/bash

aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin 730335227492.dkr.ecr.eu-west-1.amazonaws.com

# aws s3 cp s3://s3b-stf-iflightneo-output-error-311-dev-euwe1-01/311_code . --recursive
aws s3 cp s3://s3b-iflightneoint-dev-euwe1-crewlink-mq-publisher/publisher_code . --recursive

# docker build -t lmb-iflightneoint-dev-euwe1-crewlink-mq-publisher-service .

docker tag lmb-iflightneoint-dev-euwe1-crewlink-mq-publisher-service:latest 730335227492.dkr.ecr.eu-west-1.amazonaws.com/lmb-iflightneoint-dev-euwe1-crewlink-mq-publisher-service:latest

docker push 730335227492.dkr.ecr.eu-west-1.amazonaws.com/lmb-iflightneoint-dev-euwe1-crewlink-mq-publisher-service:latest

