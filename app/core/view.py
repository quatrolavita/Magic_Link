from flask import render_template, url_for, redirect
from sqlalchemy.exc import IntegrityError
from app import db
from . import core
from .form import CreateDeleteEmail
from ..models import User
from .email import send_mail


@core.route('/')
def index():

    users_data = User.query.all()

    return render_template('index.html', data_list=users_data)


@core.route('/magic_link/<token>')
def magic_link(token):

    user = User.decode_token(token)

    if user is not None:
        user.increment_counter()
        return redirect(url_for('core.index'))

    return redirect(url_for('core.index'))


@core.route('/create_delete', methods=['GET', 'POST'])
def create_delete_email():

    form = CreateDeleteEmail()

    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()
        if user is not None:
            db.session.delete(user)
            db.session.commit()
            return redirect(url_for('core.index'))

        new_user = User(email=form.email.data)

        try:
            db.session.add(new_user)
            db.session.commit()
        except IntegrityError:
            return render_template('create_delete_email.html')

        token = new_user.generate_token()
        send_mail(new_user.email, 'Magic Link', 'invite',
                  user=new_user, token=token)
        return redirect(url_for('core.index'), 302)

    return render_template('create_delete_email.html', form=form)
