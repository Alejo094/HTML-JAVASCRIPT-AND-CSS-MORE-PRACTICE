import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")

@app.route("/", methods=["GET", "POST"])
def index():

    name = request.form.get("name")
    month = request.form.get("month")
    day = request.form.get("day")

    if request.method == "POST":

        # Add the user's entry into the database

        db.execute("INSERT INTO BIRTHDAYS (name,month,day) VALUES (?,?,?)",name,month,day)

        return redirect("/")

    else:

        # Display the entries in the database on index.html

        birthdays_rows = db.execute("SELECT * FROM birthdays")

        return render_template("index.html",  birthdays_rows = birthdays_rows)


