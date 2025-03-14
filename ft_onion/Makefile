all: up

build:
	docker build -t onion .

run:
	docker run -d --name onion_container -p 8080:4242 onion:latest

stop:
	docker stop onion_container

delete:
	docker rm onion_container ; docker rmi onion


restart: stop delete build run

enter:
	docker exec -it onion_container bash

get_url:
	docker exec -it onion_container cat /var/lib/tor/hidden_service/hostname

down: stop delete

up: build run

.PHONY: all build run stop delete restart down up