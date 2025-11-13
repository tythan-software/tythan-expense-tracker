```
Expense-Tracker/
│
├── manage.py
├── requirements.txt         # List of dependencies (if not using Pipenv)
├── Pipfile                  # Dependency management file (Pipenv)
├── .env                     # environment variables (not in git)
│
├── config/          # Project configuration (settings, URLs, WSGI/ASGI)
│   ├── __init__.py
│   ├── asgi.py
│   ├── wsgi.py
│   ├── urls.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py     # Common settings
│   │   ├── dev.py      # Development overrides
│   │   ├── prod.py     # Production overrides
│   │   └── test.py     # Test-specific settings
│
├── apps/                   # All Django apps live here
│   ├── core/               # A folder containing core "stuff" for settings
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── urls.py         # The place registers url patterns across modules
│   │   ├── exceptions.py   # Define how exception to respond
│   │   ├── middleware.py   # Define successful API response
│   │
│   ├── common/             # A folder containing common "stuff" for the entire project
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── models.py       # Base model
│   │   ├── constansts.py
│   │   ├── pagination.py   # Custom pagination
│   │   ├── permissions.py  # Permission defination
│   │   ├── utils.py        # Helper methods
│   │
│   ├── modules/ 
│   │   ├── users/          # Custom Django User
│   │   │   ├── __init__.py
│   │   |   ├── admin.py
│   │   │   ├── models.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   ├── serializers.py
│   │   │   ├── services.py       # Business logic (optional)
│   │   │   ├── tests/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── test_models.py
│   │   │   │   ├── test_views.py
│   │   │   │   └── test_serializers.py
│   │   │   └── migrations/
│   │   │
│   │   ├── auths/       # Wrapper JWT
│   │   │   ├── ...
│   │   │
│   │   ├── expenses/    # Another module
│   │   │   ├── ...
│   │   
│   ├── management/     # Data scripts
│
├── static/             # Static files (For Admin panel)
├── media/              # User-uploaded files