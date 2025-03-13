all: up

build:
	docker build -t onion .

run:
	docker run -d --name onion_container -p 80:80 onion:latest

stop:
	docker stop onion_container

delete:
	docker rm onion_container && docker rmi onion


restart: stop delete build run

down: stop delete

up: build run

.PHONY: all build run stop delete restart down up