## Expense Tracker
Expense Tracker is application that can help you track and list expenses, and also analyze charts and statistics about them..

---

## Features
- Expense list.
- Expense charts.
- Monthly budget bar.
- Statistics table.

---

## Tech Stack

| Frontend  | Backend | Database | Deployment           |
|-----------|---------|----------|----------------------|
| React     | Python  | Postgres | Netlify (Frontend)   |
| Bootstrap | Django  | Postgres | Render (Backend API) |

---

## Project Structure

expense-tracker/  
|── client/ # React Frontend  
|── server/ # Python + Django Backend  
|── README.md

---

## Local Setup Instructions

1. **Setup Backend (Server)**
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

    Now you can start server...

        python manage.py runserver

    ...and visit http://localhost:8000/

2. **Setup Frontend (Client)**
   ```
    cd client
    npm install
    npm start
  
3. **Access the app at**
   ```
   http://localhost:3000

---

## Screenshots
- Dashboard:
  <img width="1365" height="598" alt="image" src="/screenshots/dashboard.png" />

- Add budget:
  <img width="1365" height="602" alt="image" src="/screenshots/add-budget.gif" />

- Add expense:
  <img width="1362" height="599" alt="image" src="/screenshots/add-expense.gif" />

- Charts and analytics:
  <img width="1362" height="599" alt="image" src="/screenshots/charts-and-analytics.gif" />

---