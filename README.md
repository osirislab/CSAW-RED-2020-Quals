![Autodeploy](https://github.com/osirislab/CSAW-RED-2020-Quals/workflows/Autodeploy/badge.svg)

# CSAW-RED-2020-Quals

Some useful Docker commands:
docker system prune -af   # get rid of images that aren't in use, save space on your box
docker run -it [container name] /bin/sh  # get shell in a Docker container to debug
docker build --tag=[image name] . # build a Docker container
docker run  -p 4000:1000 [container name] # run a Docker file, listening on your port 4000 (internally the container is listening on port 1000)
docker container ps # list Docker containers
docker image ls # list Docker images
docker cp [containerId}:/file/path/in/container/file /host/local/path/file # Do something like copy a binary out of the Docker container
docker run [image-name] # Execute a Docker image