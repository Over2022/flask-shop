from flask import Flask, request, redirect
from flask import render_template
from models import db, Item
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/')
def index():
    items = Item.query.order_by(Item.price).all()
    return render_template('index.html', items=items)


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/draft/')
def draft():
    return render_template('draft.html')


@app.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        firm = request.form['firm']
        info = request.form['info']
        price = request.form['price']
        currency = request.form['currency']
        # theDate = datetime.strptime(request.form['theDate'], '%Y-%m-%d')
        theDate = request.form.get('theDate')
        item = Item(title=title, firm=firm, info=info, price=price, currency=currency, theDate=theDate)
        print(type(theDate))

        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')

        except:
            return 'Произошла ошибка'

    else:
        return render_template('create.html')


@app.route('/db')
def create_db():
    db.create_all()
    return 'All tables created'


if __name__ == '__main__':
    app.debug = True
    app.run()
