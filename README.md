# User Validation Web Application

Login name and password are submitted to a Flask server and checked against a SQLite database.
Success shows a welcome page; failure shows an error message.

## Run locally
```
pip install -r requirements.txt
python init_db.py
python app.py
```
Open http://127.0.0.1:5000  (sample users: admin/admin123, student/pass@123)

## Live demo page
https://muskandeshwal2907.github.io/lab11/
