echo "Building base image"
docker build --tag "fastapi" --label "fastapi" .
# docker build --tag "fastapi" --label "fastapi" --no-cache .

echo "Removing unused images"
docker image prune --filter "label=fastapi" --force

echo "Running docker compose"
docker-compose up
