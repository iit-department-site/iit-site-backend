SERVICE_NAME=backend_service

build:
	@echo ">>> Start image building"
	docker-compose -f docker-compose.yml build $(c)
	@echo ">>> Building is over"

up:
	@echo ">>> Up docker containers"
	docker-compose -f docker-compose.yml up $(c)

down:
	@echo ">>> Down docker containers"
	docker-compose -f docker-compose.yml down $(c)

restart:
	@echo ">>> Restart docker containers"
	docker-compose -f docker-compose.yml stop $(c)
	docker-compose -f docker-compose.yml up -d $(c)


clone_platform:
	@echo ">>> Clone project"
	git config --global user.email $(PLATFORM_GIT_EMAIL)
	git config --global user.name $(PLATFORM_GIT_USERNAME)
	git clone --branch master $(PLATFORM_REPOSITORY_URL)
