# Shared code for building a single Docker Image

# Needed Variables
# SONATYPE_MANTIK_PASSWORD password for Mantik Sonatype
# DOCKER_IMAGE_NAME name of the image
# There are also some optional arguments  below

# Get directory relative directory of this file
SELF_DIR := $(dir $(lastword $(MAKEFILE_LIST)))
include $(SELF_DIR)/docker_shared.Makefile

IMAGE_FULL_NAME = $(DOCKER_REPO)/$(DOCKER_IMAGE_NAME)
REMOTE_IMAGE_NAME = $(REMOTE_REPO_NAME)/$(REMOTE_REPO_GROUP)$(DOCKER_IMAGE_NAME):$(REMOTE_IMAGE_TAG)
DOCKER_EXTRA_ARGS ?=
# If given, use this docker file
DOCKER_FILE ?= ""

ifeq ($(DOCKER_FILE),"")
	DOCKER_FILE_ARGUMENT =
else
	DOCKER_FILE_ARGUMENT = -f $(DOCKER_FILE)
endif

.PHONY: docker
docker: | build docker-unchecked

.PHONY: docker-unchecked
docker-unchecked:
	@echo "IMAGE_FULL_NAME=${IMAGE_FULL_NAME}"
	@echo "REMOTE_IMAGE_NAME=${REMOTE_IMAGE_NAME}"
	$(DOCKER) build $(DOCKER_FILE_ARGUMENT) $(DOCKER_EXTRA_ARGS) -t $(IMAGE_FULL_NAME) .

.PHONY: docker-publish
docker-publish: docker-login
	$(DOCKER) tag $(IMAGE_FULL_NAME) $(REMOTE_IMAGE_NAME)
	$(DOCKER) push $(REMOTE_IMAGE_NAME)
