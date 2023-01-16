from flask import Blueprint, render_template, request, redirect, url_for
from database import users

home_blueprint = Blueprint("home", __name__)


@home_blueprint.route("/")
def home():
    return render_template("home.html")


@home_blueprint.route("/signup", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        users.insert_one({"email": email, "username": username, "password": password})
        return redirect(url_for("home.home"))
    return render_template('signup.html')