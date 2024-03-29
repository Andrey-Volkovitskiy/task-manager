# Task manager

**This is the final training project of "Python Developer" specialization.**

*Django / DRF web app that helps office workers manage tasks*

Deployed at: https://task-man.up.railway.app/

* Implemented the web app using Django ClassBasdViews
* Practiced implementation of CRUD operations and user permissions
* The UI localized in two languages (Eng/Ru) using i18n
* The REST API added using DFR
* The app covered with 126 tests (unit & end-to-end)
* Parameterized fixtures and fixture factories used
* The code refactored to follow DRY, KISS

---
### Tests and code quality assessment:
[![Linter](https://github.com/Andrey-Volkovitskiy/python-project-52/actions/workflows/flake8_linter.yml/badge.svg)](https://github.com/Andrey-Volkovitskiy/python-project-52/actions/workflows/flake8_linter.yml)    [![Pytest (with postgres)](https://github.com/Andrey-Volkovitskiy/python-project-52/actions/workflows/pytest_with_postgres.yml/badge.svg)](https://github.com/Andrey-Volkovitskiy/python-project-52/actions/workflows/pytest_with_postgres.yml)

[![Maintainability](https://api.codeclimate.com/v1/badges/b06b8d9b092a3a4c9712/maintainability)](https://codeclimate.com/github/Andrey-Volkovitskiy/python-project-52/maintainability)    [![Test Coverage](https://api.codeclimate.com/v1/badges/b06b8d9b092a3a4c9712/test_coverage)](https://codeclimate.com/github/Andrey-Volkovitskiy/python-project-52/test_coverage)


---
This project was built using these tools:

| Tool                                                                        | Description                                             |
|-----------------------------------------------------------------------------|---------------------------------------------------------|
| [Django](https://www.djangoproject.com/)         | Web framework  |
| [Django ORM](https://docs.djangoproject.com/en/4.2/topics/db/)         | Database-abstraction API  |
| [Django REST Framework](https://www.django-rest-framework.org/)         | Web-API toolkit  |
| [PostgreSQL](https://www.postgresql.org)         | Database management system  |
| [Bootstrap](https://getbootstrap.com/)         | CSS framework  |
| [Docker](https://www.docker.com)       | Container-based platform for building apps  |
| [Poetry](https://poetry.eustace.io/)         | Python dependency manager  |
| [Pytest](https://docs.pytest.org/)               | Testing framework |
| [Factory Boy](https://factoryboy.readthedocs.io/)      | Factories as fixtures replacement |
| [Flake8](https://flake8.pycqa.org/)               | Linter to check code style |
| [Code Climate](https://codeclimate.com/)               | Clean Code verification system |
| [GitHub Actions](https://github.com/features/actions)               | Continuous Integration (CI) |
| [Railway](https://railway.app)               | Deployment platform |
| [Rollbar](https://rollbar.com/)               | Error logging & tracking service |
| [Swagger UI](https://swagger.io/tools/swagger-ui/)               | API documentation |

---

### REST-API
- https://task-man.up.railway.app/api/v1/ - API root
- https://task-man.up.railway.app/api/v1/schema/docs/ - Swagger UI documentation

---
### Installation and running
The application stores data using PostgresSQL (connected via DATABASE_URL).

- *make install* - to install dependencies
- *make migrate* - to migrate a database
- *make start* - to start the app
- *make dev* - to start app on development web server
- *make test* - to run tests
- *make lint* - to run linter (Flake8)

(more service commands can be found in Makefile)

---

*ER diagram*
![er diagram](https://github.com/Andrey-Volkovitskiy/python-project-52/blob/main/staticfiles/readme/er_diagram.jpg?raw=true)

---

*Bootstrap interface*
![Bootstrap interface](https://github.com/Andrey-Volkovitskiy/python-project-52/blob/main/staticfiles/readme/task_manager.jpg?raw=true)

---

*Error tracking (Rollbar)*
![Error tracking (Rollbar)](https://github.com/Andrey-Volkovitskiy/python-project-52/blob/main/staticfiles/readme/rollbar.jpg?raw=true)
