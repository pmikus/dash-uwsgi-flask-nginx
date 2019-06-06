build:
	@docker build \
		--tag pmikus/dash-uwsgi-flask-nginx .

run:
	@docker run \
		--detach \
		--net host \
		--name dash-uwsgi-flask-nginx pmikus/dash-uwsgi-flask-nginx:latest

clean:
	@docker rm --force dash-uwsgi-flask-nginx > /dev/null || true

clear:
	@docker rmi --force pmikus/dash-uwsgi-flask-nginx > /dev/null || true

tty:
	@docker exec -it dash-uwsgi-flask-nginx /bin/bash

all: clean clear build run

