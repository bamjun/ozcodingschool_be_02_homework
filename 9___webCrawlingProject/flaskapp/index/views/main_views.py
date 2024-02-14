from flask import Blueprint, render_template, request

from index.models import books, kyoboranking, kyoboprice
from datetime import datetime, timedelta

from index import db

bp = Blueprint('main', __name__, url_prefix='/')

# @bp.route('/hello')
# def hello_pybo():
#     return 'Hello, Pybo!'


@bp.route('/')
def index():
    now = datetime.now()

    # 오전 9시 이전인지 확인합니다.
    if now.hour < 9:
        # 2일 전 날짜를 구합니다.
        date_to_display = now - timedelta(days=2)
    else:
        # 1일 전 날짜를 구합니다.
        date_to_display = now - timedelta(days=1)

    specific_date = date_to_display.strftime('%Y-%m-%d')

    # ORM query
    books_info = db.session.query(books, kyoboprice, kyoboranking)\
        .join(kyoboprice, books.isbn == kyoboprice.isbn)\
        .join(kyoboranking, books.isbn == kyoboranking.isbn)\
        .filter(kyoboprice.inputdate == specific_date)\
        .filter(kyoboranking.inputdate == specific_date)\
        .order_by(kyoboranking.kyoborank.asc())
        
    page = request.args.get('page', type=int, default=1)  # 페이지
    books_info = books_info.paginate(page=page, per_page=10)
    return render_template('main/index.html', books_info=books_info)

