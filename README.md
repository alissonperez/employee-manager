Employee Manager
==================

An app to manage employees with:

- A Django Admin panel to manage employees' data.
- A read-only API to list all employees.

Installation
-------------

- Python version: **3.4.x**
- Database: **SQLite 3**

### Application setup

After virtual environment creation, install requirements:

```shell
$ pip install -r requirements.txt
```

Then, fill database with some data to test:

```shell
$ make setupdb
```

Now, just run `make serve` and access:

- http://localhost:8000/employee/ To see a json employees' list.
- http://localhost:8000/admin/ To manage employees and departments (use **admin/admin** as user/password).

Testing
---------

Just run:

```shell
$ make test
```

Development notes
------------------

- I kept it as simple as possible. So I didn't use django-rest-framework or similar, just a simple json returning in a view.
- I created a model called Departments to keep it more consistent and make searches and filters easier.
