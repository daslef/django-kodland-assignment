# Kodland Django App

## Setup

The first thing to do is to **clone** the repository:

```sh
$ git clone https://github.com/daslef/django-kodland-assignment.git
$ cd django-kodland-assignment
```

Create a **virtual environment** to install dependencies in and activate it:

*On Unix*

```sh
$ virtualenv env
$ source env/bin/activate
```

*On Windows*

```sh
$ virtualenv env
$ source env/Scripts/activate
```

You can also use *python venv* instead of *virtualenv*, like this:

```sh
$ python -m venv env
```

Then install the **dependencies**:

```sh
(env)$ pip install -r requirements.txt
```

## Usage

Once `pip` has finished downloading the dependencies:

```sh
(env)$ cd app
(env)$ python manage.py runserver
```

### Then navigate to `http://127.0.0.1:8000/blog/` to see Main Page, and `http://127.0.0.1:8000/blog/new` to check form.

## Databases

There are two databases you could find in `settings.py` (default - postgres, testing - sqlite3)

```python
DATABASES = {
    'test': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'jxvcmhju',
        'USER': 'jxvcmhju',
        'PASSWORD': 'LiDyaA61DEarJYJa8tePveTB7_4Tl8WI',
        'HOST': 'drona.db.elephantsql.com',
        'PORT': ''
    }
}
```

I was using DbaaS solution **ElephantSQL** to bring Postgres in our house.

## Security

There is no security at all now: hard-coded secret key, db-password, etc. 
Of course it should be refactored to the enviroment variables or something like that.