python version 3.8.10

RUN pip install -r requirement.txt

#CREATE DATABASE

#create a local_settings.py file in the project configuration folder and add the below code into that.

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "opportunity_form",
        "USER": "<username>",
        "PASSWORD": "<password>",
        "HOST": "localhost",
        "PORT": "",
    }
}


#RUN MIGRATIONS USING THE COMMAND

python manage.py migrate


#RUN THE SERVER USING THE COMMAND

python manage.py runserver

pre-commit hook is added for automate some tasks right before committing the code.
If files are not nicely formatted this will give you error.

to manually run the hook the given command can be used.

pre-commit run --files *
