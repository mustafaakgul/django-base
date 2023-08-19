# Django Base Structure - Project Structure
* Project -> Django Base Structure
* Apps -> App
* 3rd Party Apps -> ...
* IDE -> *PyCharm, VSCode
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
* Project -> django_base_structure, for github alter to django-base-structure
* Apps -> namely it should be short, all-lowercase and not include numbers, dashes, periods, spaces, or special characters. It also, in general, should be the plural of an app's main model, so our posts app would have a main model called Post. Exp: rest_framework, polls.
* Name the variables properly: Never use single characters, for example, ‘x’ or ‘X’ as variable names. It might be okay for your normal Python scripts, but when you are building a web application, you must name the variable properly as it determines the readability of the whole project.
* Naming of packages and modules: Lowercase and short names are recommended for modules. Underscores can be used if their use would improve readability. Python packages should also have short, all-lowercase names, although the use of underscores is discouraged.
* Since module names are mapped to file names (models.py, urls.py, and so on), it is important that module names be chosen to be fairly short as some file systems are case insensitive and truncate long names.
* Naming a class: Class names should follow the CamelCase and singular naming convention, and classes for internal use can have a leading underscore in their name. -> Article, User, Post, Comment, Tag, Category, etc.
* Naming a Related-Name: It is reasonable to indicate a related-name in plural as related-name addressing returns queryset. ->
    * class Item(models.Model): owner = models.ForeignKey(Owner, related_name='items')
* Global variable names: First of all, you should avoid using global variables, but if you need to use them, prevention of global variables from getting exported can be done via __all__, or by defining them with a prefixed underscore (the old, conventional way).
* Function names and method argument: Names of functions should be in lowercase and separated by an underscore and self as the first argument to instantiate methods. For classes or methods, use CLS or the objects for initialization.
* Method names and instance variables: Use the function naming rules—lowercase with words separated by underscores as necessary to improve readability. Use one leading underscore only for non-public methods and instance variables.

## Importing a Package
* Import packages in the following order:
    * Standard library imports -> (import os)
    * Related third party imports -> (from rest_framwwork import *)
    * Local application/library specific imports -> (from .models import User) not use like (from models import *)

## The importance of blank lines
* Two blank lines: A double blank lines can be used to separate top-level functions and the class definition, which enhances code readability.
* Single blank lines: A single blank line can be used in the use cases–for example, each function inside a class can be separated by a single line, and related functions can be grouped together with a single line. You can also separate the logical section of source code with a single line.

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
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
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