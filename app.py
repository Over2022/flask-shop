from flask import Flask
from flask import render_template
from models import db, Item


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///shop.db'
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/draft/')
def draft():
    return render_template('draft.html')


@app.route('/create/')
def create():
    return render_template('create.html')



@app.route('/db')
def create_db():
    db.create_all()
    return 'All tables created'


if __name__ == '__main__':
    app.debug = True
    app.run()