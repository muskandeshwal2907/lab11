import sqlite3
from flask import Flask, render_template, request
from werkzeug.security import check_password_hash

app = Flask(__name__)
DB = "users.db"


def get_user(username):
    con = sqlite3.connect(DB)
    # Parameterised query -> prevents SQL injection
    row = con.execute(
        "SELECT username, password_hash FROM users WHERE username = ?", (username,)
    ).fetchone()
    con.close()
    return row


@app.route("/")
def index():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")
    user = get_user(username)
    if user and check_password_hash(user[1], password):
        return render_template("success.html", username=user[0])
    return render_template("login.html", error="Invalid login name or password."), 401


if __name__ == "__main__":
    app.run(debug=True)
