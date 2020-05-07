from consumer.config import app
# import flask 
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index_aa():
    # return ''
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html'), 404


if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)



