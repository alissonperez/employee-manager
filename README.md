Employee Manager
==================

An app to manage employess with:

- A Django Admin panel to manage employees' data
- A read-only API to list all employees

Installation
-------------

Python version: *3.4.x*
Database: *SQLite3*

### Application setup

After virtual environment creation, install requirements:

```shell
$ pip install -r requirements.txt
```

To migrate and fill database with some data to test:

```shell
$ make setupdb
```

Now, just run `make serve` and access:

- http://localhost:8000/employee/ To see an employees list.
- http://localhost:8000/admin/ To manage employees and departments (use **admin/admin** as user/password).

Development notes
------------------

- I kept it as simple as possible. So I didn't use django-rest-framework or similar, just a simple json returning on a view.