
migrate:
	./manage.py migrate

populate:
	./manage.py populate

setupdb: migrate populate