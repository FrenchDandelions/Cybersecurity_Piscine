all: up

build:
	cd srcs/ && bash create_files.sh && cd -
	docker build -t stockholm .

run:
	docker run -v ./srcs:/srcs -d --name stockholm_container stockholm:latest

stop:
	docker stop stockholm_container

delete:
	docker rm stockholm_container ; docker rmi stockholm

restart: stop delete build run

enter:
	docker exec -it stockholm_container bash

down: stop delete

up: build run

.PHONY: all build run stop delete restart down up
