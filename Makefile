pull:
	git config --global --add safe.directory /home/mitchbr/Repositories/stonelifting
	git pull

build:
	docker-compose up -d --build
	docker-compose exec app python3 manage.py migrate


deploy: pull build
