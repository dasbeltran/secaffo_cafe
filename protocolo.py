from flask import Blueprint, flash, g, redirect, render_template, request, url_for

#from werkzeug.exeptions import abort
from app.db import get_db

bp = Blueprint('protocolo', __name__)

@bp.route('/protocolo')
def index():
    db, c = get_db()
    c.execute(
        'SELECT * FROM protocolo WHERE 1'
    )
    protocolos= c.fetchall()

    return render_template('protocolo/index.html', protocolos = protocolos)