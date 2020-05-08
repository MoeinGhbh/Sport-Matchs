from consumer.config import app
from flask import Flask, render_template, jsonify
from consumer.model import report
import json
from flask_sqlalchemy import SQLAlchemy


# app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/api/v1.0/getData", methods=["GET", "POST"])
def getData():
    res = report.report()
    return jsonify(res)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html'), 404


if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)



