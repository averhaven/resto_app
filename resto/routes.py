from flask import Blueprint, render_template, request, url_for, redirect, flash
from resto.recommender import recommend_resto

bp = Blueprint("resto", __name__)


def validate_german_postal_code(postal_code):
    return len(postal_code) == 5 and postal_code.isdecimal()

@bp.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        postal_code = request.form['postal_code']
        if not validate_german_postal_code(postal_code):
            flash("This is not a valid postal code for Germany.")
        else:
            return redirect(url_for(".postal_code_search", postal_code=postal_code))
    return render_template("home.html")

@bp.route("/recommend/restaurants")
def postal_code_search():
    postal_code = request.args.get('postal_code')
    restaurants = recommend_resto(postal_code)
    return render_template("recommend.html", restaurants=restaurants)