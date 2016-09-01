# -*- coding:utf8 -*-
from flask import render_template , session , redirect , url_for, abort, flash , current_app
from flask_login import login_required, current_user
from flask import request
from . import main
from .forms import EditProfileForm, EditProfileAdminForm , ItemForm
from .. import db
from ..models import Item, Role, User
from ..decorators import admin_required

@main.route('/' , methods=['GET' , 'POST'])
def index():
    if request.method == 'POST':
        data = request.form.get('search','')
        item = Item.query.filter_by(name = data).all()
        if item:
            return render_template('myindex.html' , items = item)
        else:
            return render_template('haveNot.html')
    # items = Item.query.all()
    page = request.args.get('page', 1, type=int)
    pagination = Item.query.order_by(Item.id).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
    # pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
    #     page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
    #     error_out=False)
    items = pagination.items
    return render_template('myindex.html', items = items,
                           pagination=pagination)
    # return render_template('myindex.html', items = items )

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


@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)


@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.tel = form.tel.data
        db.session.add(current_user)
        flash('Your profile has been updated.')
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.tel.data = current_user.tel
    return render_template('edit_profile.html', form=form)


@main.route('/edit-profile/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    form = EditProfileAdminForm(user=user)
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        user.confirmed = form.confirmed.data
        user.role = Role.query.get(form.role.data)
        user.name = form.name.data
        user.location = form.location.data
        user.tel = form.tel.data
        db.session.add(user)
        flash('The profile has been updated.')
        return redirect(url_for('.user', username=user.username))
    form.email.data = user.email
    form.username.data = user.username
    form.confirmed.data = user.confirmed
    form.role.data = user.role_id
    form.name.data = user.name
    form.location.data = user.location
    user.tel = form.tel.data
    return render_template('edit_profile.html', form=form, user=user)

@main.route('/adminUpload', methods=['GET', 'POST'])
@login_required
@admin_required
def adminUpload():
    form = ItemForm()
    if form.validate_on_submit():
        item = Item(name=form.name.data,
                    detal=form.detal.data,
                    img1=form.img1.data,
                    img2=form.img2.data,
                    img3=form.img3.data,
                    title=form.title.data)
        db.session.add(item)
        db.session.commit()
        flash(u'已发布新物品')
        return redirect(url_for('.adminUpload', form=form))
    return render_template('adminUpload.html', form=form)

# @main.route('/upload', methods=['GET', 'POST'])
# @login_required
# @admin_required
# def upload():
#     if request.method == 'POST':
#         url1 = request.form.get('linkurl','')
#     return current_app.send_static_file('upload.html')