NS ?= cgarciaarano
VERSION ?= latest
IMAGE_NAME ?= twitter-flask

.PHONY: build

build:
	docker build -t ${IMAGE_NAME}:${VERSION} -f docker/Dockerfile .

tag:
	docker tag ${IMAGE_NAME}:${VERSION} ${IMAGE_NAME}:${VERSION}

test:
	docker run --rm ${IMAGE_NAME}:${VERSION} python --version
