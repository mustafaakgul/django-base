# Django Base Structure
* Project -> Django Base Structure
* Apps -> App
* 3rd Party Apps -> ...
* [Django](https://www.djangoproject.com/) - The web framework used
* [Django Rest Framework](https://www.django-rest-framework.org/) - The web framework used
* SonarLint - The IDE extension used
* GitHub Copilot - The IDE extension used
* [Docker](https://www.docker.com/) - The container used
* [Docker Compose](https://docs.docker.com/compose/) - The container used
* [Docker Hub](https://hub.docker.com/) - The container used
* Separate settings for local, production and test
* Separate requirements for local, production and test
* Separate urls for local, production and test
* Separate wsgi for local, production and test
* Separate asgi for local, production and test
* Add .env file
* Add .env.example file
* Add .env.test file
* Add .gitignore file
* Add .gitattributes file
* Add .pre-commit-config.yaml file
* Add .readthedocs.yml file
* Add .travis.yml file
* Add LICENSE file
* Add Makefile file
* Add README.md file
* Add app folder
* Add config folder
* Add docs folder
* Add manage.py file
* Add requirements folder
* Add requirements.txt file
* Add requirements_dev.txt file
* Add requirements_docs.txt file
* Add requirements_test.txt file
* Add .github folder
* Add .github/workflows folder
* Add .github/workflows/python-app.yml file
* Add .isort.cfg file
* Add .flake8 file
* Add .bandit file
* Add .mypy.ini file
* Add .black file
* Add .coverage file
* Add .editorconfig file
* Add pipfile and pipfile.lock

## Naming Conventions
* Project -> django_base_structure
* Apps -> namely it should be short, all-lowercase and not include numbers, dashes, periods, spaces, or special characters. It also, in general, should be the plural of an app's main model, so our posts app would have a main model called Post

### Sources
* https://peps.python.org/pep-0008/#package-and-module-names
* https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/
* https://django-best-practices.readthedocs.io/en/latest/projects.html

## Project Structure
```
.
├── .github
│   └── workflows
│       └── python-app.yml
├── .gitignore
├── .isort.cfg
├── .flake8
├── .bandit
├── .mypy.ini
├── .black
├── .coverage
├── .editorconfig
├── .env
├── .env.example
├── .env.test
├── .gitattributes
├── .gitignore
├── .pre-commit-config.yaml
├── .pylintrc
├── .readthedocs.yml
├── .travis.yml
├── LICENSE
├── Makefile
├── README.md
├── app
│   ├── __init__.py
│   ├── asgi.py
│   ├── migrations
│   ├── settings
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── local.py
│   │   ├── production.py
│   │   └── test.py
│   ├── urls.py
│   └── wsgi.py
├── config
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── local.py
│   │   ├── production.py
│   │   └── test.py
│   ├── urls.py
│   └── wsgi.py
├── docs
│   ├── Makefile
│   ├── conf.py
│   ├── index.rst
│   ├── make.bat
│   └── requirements.txt
├── manage.py
├── requirements
│   ├── base.txt
│   ├── local.txt
│   ├── production.txt
│   └── test.txt
├── requirements.txt
├── requirements_dev.txt
├── requirements_docs.txt
├── requirements_test.txt
```

## How to run
```
$ python manage.py runserver
```

## How to run test
```
$ python manage.py test
```

## How to run coverage
```
$ coverage run --source='.' manage.py test
$ coverage report
```

## How to run flake8
```
$ flake8
```

## How to run isort
```
$ isort -rc .
```

## How to run black
```
$ black .
```

## How to run mypy
```
$ mypy .
```

## How to run bandit
```
$ bandit -r .
```

## How to run pylint
```
$ pylint .
```

## How to run pre-commit
```
$ pre-commit run --all-files
```

## How to run docker
```
$ docker-compose up
```

## How to run docker test
```
$ docker-compose -f docker-compose.test.yml up
```

## How to run docker coverage
```
$ docker-compose -f docker-compose.coverage.yml up
```

## How to run docker flake8
```
$ docker-compose -f docker-compose.flake8.yml up
```

## How to run docker isort
```
$ docker-compose -f docker-compose.isort.yml up
```

## How to run docker black
```
$ docker-compose -f docker-compose.black.yml up
```

## How to run docker mypy
```
$ docker-compose -f docker-compose.mypy.yml up
```

## How to run docker bandit
```
$ docker-compose -f docker-compose.bandit.yml up
```

## How to run docker pylint
```
$ docker-compose -f docker-compose.pylint.yml up
```

## How to run docker pre-commit
```
$ docker-compose -f docker-compose.pre-commit.yml up
```

## How to run docker build
```
$ docker-compose -f docker-compose.build.yml up
```