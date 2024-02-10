from flask import Blueprint, render_template

from index.models import Books, KyoboRanking, KyoboPrice

from datetime import datetime

from index import db

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


# @bp.route('/')
# def index():
#     return 'Pybo index'
@bp.route('/')
def index():
    # Specific date you're interested in
    specific_date = datetime(2024, 2, 10).date()

    # ORM query
    books_info = db.session.query(Books, KyoboPrice, KyoboRanking)\
        .join(KyoboPrice, Books.isbn == KyoboPrice.isbn)\
        .join(KyoboRanking, Books.isbn == KyoboRanking.isbn)\
        .filter(KyoboPrice.inputDate == specific_date).all()

    return render_template('main/index.html', books_info=books_info)