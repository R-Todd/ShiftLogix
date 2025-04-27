from flask import Blueprint, render_template


def create_home_blueprint():
    bp = Blueprint("home", __name__)

    @bp.route("/")
    def landing():
        return render_template("home.html")

    return bp