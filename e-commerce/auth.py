import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from .db import *

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('POST', 'GET'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
            
        if error is None:
            try:
                db.execute(
                    'INSERT INTO user (username, password) VALUES (?, ?)',
                    (username, generate_password_hash(password))
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for('auth.login'))
            
        flash(error)
        
    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()
        
        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'
        
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        
        flash(error)
        
    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    
    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()
        
        
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        
        return view(**kwargs)
    
    return wrapped_view

@bp.route('/change_password', methods=('POST', 'GET'))
@login_required
def change_password():
    if request.method == 'POST':
        user_id = session.get('user_id')
        new_password = request.form['new_password']
        current_password = request.form['current_password']
        db = get_db()
        error = None
        
        if not new_password:
            error = 'Please enter the new password.'
        elif not current_password:
            error = 'Please enter your current password.'
        
        if error is None:
                user = db.execute(
                    'SELECT * FROM user WHERE id = (?)', (user_id,) 
                ).fetchone()
                if check_password_hash(user['password'], current_password) is True:
                    db.execute(
                        'UPDATE user SET password = ? WHERE id = (?)', (generate_password_hash(new_password),user_id,) 
                    ).fetchone()
                    db.commit()
                    error = 'Password changed successfully'
                    flash(error)
                else:
                    error = 'Please enter the current password again.'
                    flash(error)
                return redirect(url_for('auth.login'))
    return render_template('auth/change_password.html')
