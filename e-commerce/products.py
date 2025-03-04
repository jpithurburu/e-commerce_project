from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)

from werkzeug.exceptions import abort

from .auth import login_required 
from .db import get_db

bp = Blueprint('products', __name__)

@bp.route('/')
@login_required
def index():
    if session is not None:
        return render_template('index.html')
    else:
        return redirect(url_for('auth.login'))

