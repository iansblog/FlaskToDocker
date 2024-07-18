# Project overview
This is a simple Python/Flask application that can be built from a single project and deployed to the following chip sets:
- linux/amd64
- linux/arm64
- linux/arm/v7 

This project is being used as a test bed for deployment to cloud hosting and locally on a Raspberry PI. 

The project is going to use an environmental variable that can be set by the user in the docker-compose.yml 


## Docker commands
### Build and test
docker build -t neonsunset/helloworld . 

#### Port 5000 (default for flask)
- docker container run -d -p 5000:5000 neonsunset/helloworld:latest 
- Go to http://localhost:5000 and see "Hello world"

#### Port 80 (default for the internet)
- docker container run -d -p 80:5000 neonsunset/helloworld:latest 
- To test the port 80 Go to http://localhost and see "Hello world"

### Build for the Raspbery Pi also. 
- docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7 -t neonsunset/helloworld .

### Multi platform build & push to hub 
- docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7 -t neonsunset/helloworld . --push

## Local deployment using the docker-compose.yml file
- docker compose up

## Docker Hub Location
To see the output on docker hub please go to: 
- [Docker Hub](https://hub.docker.com/r/neonsunset/helloworld)