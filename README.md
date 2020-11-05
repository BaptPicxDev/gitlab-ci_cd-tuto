# gitlab-ci_cd-tuto
Git repository to provide an example and how to use CI/CD and unit test. It provides pipelines through git to test and deploy your code. Use docker containers. 

# To clone the project :
git clone https://github.com/BaptPicxDev/gitlab-ci_cd-tuto

# Install requirements 
pip install -r requirements.txt

# Build the docker image
docker build -t docker_build .

# Run a docker container with the correct image
docker run --rm -d -it --name docker_container:test docker_build"

# To enter the container while its running
docker exec -it docker_container bash
