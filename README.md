# Maker Notes
Forked from: https://github.com/sebst/pythonic-news/

A Hacker News lookalike written in Python/Django

## Create a virtual env
```shell script
cd ~
python3 -m venv venv/

Linux
source ~/venv/bin/activate

Windows
<venv>\Scripts\Activate.ps1
```

## Freezing requirements
```shell script
pip freeze > requirements.txt
pip install -r requirements.txt
```

## Setup for local development
### Set up virtual environment
```shell script
python -m venv venv/
source venv/bin/activate
```

### Install Dependencies
```shell script
pip install -r requirements.txt
```

### Migrate Database
```shell script
python manage.py migrate
```

### Extra setup work
* Set ```DEBUG=True``` if necessary
* Add ```127.0.0.1``` to ```ALLOWED_HOSTS```

### Run Django Server
```shell script
python manage.py runserver
```
Now you can access the website at ```127.0.0.1:8000```.

### Get Libs for Windows
https://stackoverflow.com/questions/64261546/how-to-solve-error-microsoft-visual-c-14-0-or-greater-is-required-when-inst
https://www.lfd.uci.edu/~gohlke/pythonlibs/#cffi