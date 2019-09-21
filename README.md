# admin-server
This is the admin server for lsof.top - its django based.

This controls the database schema for everything, if a service requires a table schema change or additional tables - you must create the required objects here first and then create migrations.

# Quickstart
```
1. pip install -r requirements.txt
2. python manage.py migrate
3. python manage.py runserver
```

# To-do
- Different record types