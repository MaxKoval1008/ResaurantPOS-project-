build-dev:
	make stop-dev
	docker-compose -f build/dev/docker-compose.yml up -d --build
run-dev:
	docker-compose  -f build/dev/docker-compose.yml up -d --build
stop-dev:
	docker-compose -f build/dev/docker-compose.yml down -v
logs-dev:
	docker-compose -f build/dev/docker-compose.yml logs -f

build-production:
	make stop-production
	docker-compose -f build/prod/docker-compose.prod.yml up -d --build
stop-production:
	docker-compose -f build/prod/docker-compose.prod.yml down -v
logs-production:
	docker-compose -f build/prod/docker-compose.prod.yml logs -f
