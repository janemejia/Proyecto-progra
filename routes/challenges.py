from flask import Blueprint, render_template, redirect, url_for


challenges= Blueprint("challenges", __name__, url_prefix="/challenges")

@challenges.route("/")
def home():
    return render_template("challenges/home.html")

