from flask import render_template , session , redirect , url_for
from flask import request
from . import main
from .. import db
from ..models import Item

@main.route('/' , methods=['GET' , 'POST'])
def index():
    if request.method == 'POST':
        data = request.form.get('search','')
        item = Item.query.filter_by(name = data).all()
        if item:
            return render_template('myindex.html' , items = item)
        else:
            return render_template('haveNot.html')
    items = Item.query.all()
    return render_template('myindex.html', items = items )

@main.route('/item/<itemName>')
def item(itemName):
    if request.method == 'POST':
        data = request.form.get('search','')
        item = Item.query.filter_by(name = data).all()
        if item:
            return render_template('myindex.html' , items = item)
        else:
            return render_template('haveNot.html')
    item = Item.query.filter_by(name = itemName).first()
    return render_template('item.html' , itemName = item)

@main.route('/title/<titleName>')
def title(titleName):
    if request.method == 'POST':
        data = request.form.get('search','')
        item = Item.query.filter_by(name = data).all()
        if item:
            return render_template('myindex.html' , items = item)
        else:
            return render_template('haveNot.html')
    title = Item.query.filter_by(title = titleName).all()
    return render_template('myindex.html' , items = title)
