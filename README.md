# Django Base Structure - Project Structure
* Project -> Django Base Structure and its Structure
* Apps -> App and its Structure
* 3rd Party Apps -> ..., Using Packages and Modules
* IDE -> *PyCharm, VSCode
* Virtual Envinronment -> venv
* README.md file
* .gitignore file
* Requirements.txt file
* Version Control System -> Git
* Versions Store -> GitHub
* In App Folder “utils” directory for utility functions and helper modules
* Using an “api” directory for housing REST API-related files if your project includes APIs

##  TODO
* Database -> PostgreSQL
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
* Use Isolated Docker Container

# Tools - Extras
* Code Quality — flake8
* Environment Manager — venv
* Documentation — Swagger
* Testing — pytest
* IDE — Pycharm, VSCode, Vim
* Debug — pdb

## Some Points
* Denormalisations
* Business Logic
* 12 Factors: Codebase, Dependencies, Config, Backing services, Build, release, run, Processes, Port binding, Concurrency, Disposability, Dev/prod parity, Logs, Admin processes

## Coding Style
* PEP 8
* Testable, Test Driven Development
* Avoid Writing Fat Views

## Naming Conventions
* Project -> django_base_structure, for github alter to django-base-structure
* Apps -> namely it should be short, all-lowercase and not include numbers, dashes, periods, spaces, or special characters. It also, in general, should be the plural of an app's main model, so our posts app would have a main model called Post. Exp: rest_framework, polls.
* Name the variables properly: Never use single characters, for example, ‘x’ or ‘X’ as variable names. It might be okay for your normal Python scripts, but when you are building a web application, you must name the variable properly as it determines the readability of the whole project.
* Naming of packages and modules: Lowercase and short names are recommended for modules. Underscores can be used if their use would improve readability. Python packages should also have short, all-lowercase names, although the use of underscores is discouraged.
* Since module names are mapped to file names (models.py, urls.py, and so on), it is important that module names be chosen to be fairly short as some file systems are case insensitive and truncate long names.
* Naming a class: Class names should follow the PascalCase and singular naming convention, and classes for internal use can have a leading underscore in their name. -> Article, User, Post, Comment, Tag, Category, etc.
* Naming a Related-Name: It is reasonable to indicate a related-name in plural as related-name addressing returns queryset. ->
    * class Item(models.Model): owner = models.ForeignKey(Owner, related_name='items')
* Redundant model name in a field name -> (user_status to status), use singular snake_case
* Global variable names: First of all, you should avoid using global variables, but if you need to use them, prevention of global variables from getting exported can be done via __all__, or by defining them with a prefixed underscore (the old, conventional way).
* Function names and method argument: Names of functions should be in lowercase and separated by an underscore (snake_case) and self as the first argument to instantiate methods. For classes or methods, use CLS or the objects for initialization.
* Method names and instance variables: Use the function naming rules—lowercase with words separated by underscores as necessary to improve readability. Use one leading underscore only for non-public methods and instance variables.
* Function and variable names in snake_case
* Constants snake_case capitalized
* Naming templates -> [application]/[model]_[function].html, address_book/contact_list.html

## Importing a Package
* Import packages in the following order:
    * Standard library imports -> (import os)
    * Related third party imports -> (from rest_framwwork import *)
    * Local application/library specific imports -> (from .models import User) not use like (from models import *)
* Import from Python standard library(1st)
* Import from core Django(2nd)
* Import from 3rd party vendor(3rd)
* Import from Django Apps(4th)(Current Project)
* Avoid import *

## The importance of blank lines
* Two blank lines: A double blank lines can be used to separate top-level functions and the class definition, which enhances code readability.
* Single blank lines: A single blank line can be used in the use cases–for example, each function inside a class can be separated by a single line, and related functions can be grouped together with a single line. You can also separate the logical section of source code with a single line.

## Indentation/Space
* Use 4 spaces for indentation(Python 3 disallows mixing the use of tabs and spaces for indentation)
* Separate top level function and classes with two blank lines
* Separate method definition inside class by one line
* Maximum length of line should be less than 80 characters
* There should be no trailing white spaces

### Sources
* https://peps.python.org/pep-0008/#package-and-module-names
* https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/
* https://django-best-practices.readthedocs.io/en/latest/projects.html, https://django-best-practices.readthedocs.io/en/latest/applications.html
* https://steelkiwi.medium.com/best-practices-working-with-django-models-in-python-b17d98ab92b
* https://pythonislove.com/django-urls-naming-conventions-and-best-practices
* https://google.github.io/styleguide/pyguide.html

## Migrations
* Do not modify the files created by makemigration command(do not add custom sql command)
* Place custom sql command if needed in a separate file and do not mix it with the auto generated files from makemigration command
* Forward and backward migration work only on auto generated files by makemigration command
* Not all migration can be reversed
* Add — database=<dbConfigName> always in your migration
* Forward Migration
  * python manage.py migrate appname 0002 — settings=project.settings.<Env> — database=<dbConfigName>
  * python manage.py migrate appname 0003 — settings=project.settings.<Env> — database=<dbConfigName>
  * Suppose it added all the migration 0001.py , 0002.py , 0003.py , 0004.py
* Backward Migration
  * (Remove New migrations -0002.py , 0003.py , 0004.py)
  * python manage.py migrate appname 0001 — settings=project.settings.<Env> — database=<dbConfigName>

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

project/
    gitignore
    README.md
    docs/
    requirements/
        local.txt
        qa.txt
        prod.txt
        base.txt
    project/
        settings/
            base.py //copy of original settings.py
            qa.py
            local.py
            prod.py
        urls.py
        wsgi.py
        settings_default.py //renamed settings->settings_default
    app1/
    app2/
        v1/
            api.py // entry point , not much logic
            service.py // all business logic
            util.py // any helper
        test/
        migrations/
        admin.py
        models.py
        apps.py
        urls.py
        views.py
    utils/
        service/
        helper/
        
App Style Structure
project/apps/portal/
├── __init__.py
├── admin.py
├── apps.py
├── management
│   ├── __init__.py
│   └── commands
│       ├── __init__.py
│       └── update_portal_feeds.py
├── migrations
│   └── __init__.py
├── models.py
├── static
│   └── portal
│       ├── css
│       ├── img
│       └── js
├── templates
│   └── portal
│       └── index.html
├── templatetags
│   ├── __init__.py
│   └── portal.py
├── tests.py
├── urls.py
└── views.py

#Good practice
root_folder/
    my_app1/
    my_app2/
    my_app3/
    templates/

#If you want to make your app reusable
root_folder/
    my_app1/
        templates/
    my_app2/
        templates/
    my_app3/
        templates/
```

## Model Style Ordering
```
The Django Coding Style suggests the following order of inner classes, methods and attributes:

If choices is defined for a given model field, define each choice as a tuple of tuples, with an all-uppercase name as a class attribute on the model.
All database fields
Custom manager attributes
class Meta
def __str__()
def save()
def get_absolute_url()
Any custom methods
Example:

from django.db import models
from django.urls import reverse

class Company(models.Model):
    # CHOICES
    PUBLIC_LIMITED_COMPANY = 'PLC'
    PRIVATE_COMPANY_LIMITED = 'LTD'
    LIMITED_LIABILITY_PARTNERSHIP = 'LLP'
    COMPANY_TYPE_CHOICES = (
        (PUBLIC_LIMITED_COMPANY, 'Public limited company'),
        (PRIVATE_COMPANY_LIMITED, 'Private company limited by shares'),
        (LIMITED_LIABILITY_PARTNERSHIP, 'Limited liability partnership'),
    )

    # DATABASE FIELDS
    name = models.CharField('name', max_length=30)
    vat_identification_number = models.CharField('VAT', max_length=20)
    company_type = models.CharField('type', max_length=3, choices=COMPANY_TYPE_CHOICES)

    # MANAGERS
    objects = models.Manager()
    limited_companies = LimitedCompanyManager()

    # META CLASS
    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'

    # TO STRING METHOD
    def __str__(self):
        return self.name

    # SAVE METHOD
    def save(self, *args, **kwargs):
        do_something()
        super().save(*args, **kwargs)  # Call the "real" save() method.
        do_something_else()

    # ABSOLUTE URL METHOD
    def get_absolute_url(self):
        return reverse('company_details', kwargs={'pk': self.id})

    # OTHER METHODS
    def process_invoices(self):
        do_something()
```

## How to run
```
$ virtual venv
$ source venv/bin/activate
$ python manage.py runserver
$ python manage.py runserver --settings=settings.local
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

## Some Frequently Notes
* Null: It is database-related. Defines if a given database column will accept null values or not.
* Blank: It is validation-related. It will be used during forms validation, when calling form.is_valid().