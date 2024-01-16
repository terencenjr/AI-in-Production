#!/bin/sh

set -e
echo "Pulling Python 3.9 Slim image"
docker pull python:3.9-slim

echo "Building base image"
docker build --tag "fastapi" --label "fastapi" .

echo "Removing old unused images"
docker image prune --filter "label=fastapi" --force

echo "Running docker compose"
docker-compose up
set +e