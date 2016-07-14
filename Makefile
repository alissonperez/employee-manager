
migrate:
	./manage.py migrate

populate:
	./manage.py populate

setupdb: migrate populate

serve:
	./manage.py runserver

test:
	./manage.py test
