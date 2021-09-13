# Common code for using docker inside Makefiles
DOCKER_REPO = mantikai
CI_COMMIT_REF_SLUG ?= local
REMOTE_REPO_NAME ?= mdocker.rcxt.de
# Can be overriden to have the full image name
REMOTE_REPO_GROUP ?=
DOCKER_USERNAME ?= mantik.ci
DOCKER_PASSWORD ?= $(SONATYPE_MANTIK_PASSWORD)
DOCKER ?= docker

REMOTE_IMAGE_TAG ?= $(or $(CI_COMMIT_TAG),$(CI_COMMIT_REF_SLUG))

.PHONY: docker-login
docker-login:
	@# Trick to not show the password
	@mkdir -p target
	@touch target/sonatype_password
	@chmod 600 target/sonatype_password
	@echo $(DOCKER_PASSWORD) > target/docker_password
	cat target/docker_password | $(DOCKER) login -u $(DOCKER_USERNAME) --password-stdin $(REMOTE_REPO_NAME)
	@rm target/docker_password