from flask import Blueprint, jsonify
from .scraping.example import fetch_title

bp = Blueprint("routes", __name__)

@bp.get("/")
def health():
    return jsonify(ok=True)

@bp.get("/scrape")
def scrape():
    title = fetch_title("https://www.python.org/")
    return jsonify(title=title)
