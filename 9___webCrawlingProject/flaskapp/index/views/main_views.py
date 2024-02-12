from flask import Blueprint, render_template, request

from index.models import books, kyoboranking, kyoboprice

from datetime import datetime

from index import db

bp = Blueprint('main', __name__, url_prefix='/')

# @bp.route('/hello')
# def hello_pybo():
#     return 'Hello, Pybo!'


@bp.route('/')
def index():
    # Specific date you're interested in
    specific_date = datetime(2024, 2, 13).date()

    # ORM query
    books_info = db.session.query(books, kyoboprice, kyoboranking)\
        .join(kyoboprice, books.isbn == kyoboprice.isbn)\
        .join(kyoboranking, books.isbn == kyoboranking.isbn)\
        .filter(kyoboprice.inputdate == specific_date)\
        .order_by(kyoboranking.kyoborank.asc())
        
    page = request.args.get('page', type=int, default=1)  # 페이지
    books_info = books_info.paginate(page=page, per_page=10)
    return render_template('main/index.html', books_info=books_info)

