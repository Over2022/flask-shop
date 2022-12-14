from flask import Flask
from flask import render_template
from flask import url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///shop.db'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/draft/')
def draft():
    return render_template('draft.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
