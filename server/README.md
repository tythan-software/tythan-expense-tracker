**Setup Backend (Server)**
    ```
    Install packages:

        pipenv install

    This will install the virtual environments and all dependencies.

    Now start the virtual environment shell:

        pipenv shell

    Run migrations:

        python manage.py makemigrations
        python manage.py migrate

    Create superuser:

        python manage.py createsuperuser

    Run data:
        python manage.py seed_data
        python manage.py clear_db

    Now you can start server...

        python manage.py runserver

    ...and visit http://localhost:8000/