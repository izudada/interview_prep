# Makefile for Interview Coach AI app

# Variables
IMAGE_NAME=interview-coach
CONTAINER_NAME=interview-coach-container

# Build Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Run the container
run:
	docker run -p 8501:8501 --name $(CONTAINER_NAME) $(IMAGE_NAME)

# Stop and remove container
stop:
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true

# Remove image
clean:
	docker rmi $(IMAGE_NAME) || true

# Run docker-compose (if using docker-compose.yml)
up:
	docker-compose up --build

down:
	docker-compose down
