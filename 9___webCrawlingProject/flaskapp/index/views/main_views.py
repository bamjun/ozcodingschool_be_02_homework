from flask import Blueprint, render_template, request

from index.models import books, kyoboranking, kyoboprice
from datetime import datetime, timedelta

from index import db
import random, json


bp = Blueprint('main', __name__, url_prefix='/')

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
        .filter(kyoboprice.inputdate == specific_date, kyoboranking.inputdate == specific_date)\
        .order_by(kyoboranking.kyoborank.asc())

    data = dataForBubbleChart(books_info)    


    page = request.args.get('page', type=int, default=1)  # 페이지
    books_info = books_info.paginate(page=page, per_page=10)
    return render_template('main/index.html', books_info=books_info, data=json.dumps(data, ensure_ascii=False), specific_date=specific_date, select_date=get_unique_input_dates())

@bp.route('detail/<int:specific_date>/')
def select_date_page(specific_date):
    specific_date = datetime.strptime(str(specific_date), '%Y%m%d').strftime('%Y-%m-%d')

    # ORM query
    books_info = db.session.query(books, kyoboprice, kyoboranking)\
        .join(kyoboprice, books.isbn == kyoboprice.isbn)\
        .join(kyoboranking, books.isbn == kyoboranking.isbn)\
        .filter(kyoboprice.inputdate == specific_date, kyoboranking.inputdate == specific_date)\
        .order_by(kyoboranking.kyoborank.asc())

    data = dataForBubbleChart(books_info)    

    page = request.args.get('page', type=int, default=1)  # 페이지
    books_info = books_info.paginate(page=page, per_page=10)


    return render_template('main/index.html', books_info=books_info, data=json.dumps(data, ensure_ascii=False), specific_date=specific_date, select_date=get_unique_input_dates())

def get_unique_input_dates():
    # kyoboranking 테이블에서 중복 없는 inputdate를 조회하고, 날짜별로 정렬합니다.
    unique_dates = kyoboranking.query.with_entities(kyoboranking.inputdate.distinct().label('unique_dates')).order_by(kyoboranking.inputdate.desc()).all()
    
    # 조회 결과를 리스트로 변환합니다. 각 원소는 날짜(datetime 객체)입니다.
    dates_list = [date.unique_dates.strftime('%Y%m%d') for date in unique_dates]
    return dates_list


def calculate_colors(n):
    colors = [
        f"hsla({random.randint(0,360)}, 100%, {random.randint(30,60)}%, 0.5)"
        for i in range(n)
    ]
    return colors


def dataForBubbleChart(books_info):
    data = {"datasets": []}
    category_data = {}

    # 카테고리 개수에 따라 색상 계산
    unique_categories = set(b.category for b, p, r in books_info)
    colors = calculate_colors(len(unique_categories))
    
    for b, p, r in books_info:
        index_kyoboupdown = r.kyoboupdown
        index_review = r.kyoboreview
        index_kyoboupdown = max(min(r.kyoboupdown, 54), -54)  # 값 조정
        index_kyoboupdown_tip = f"⬆️{abs(index_kyoboupdown)}" if index_kyoboupdown > 0 else "❄️0" if index_kyoboupdown == 0 else f"⬇️{abs(index_kyoboupdown)}"

        if b.category not in category_data:
            color_index = len(category_data)  # 현재 카테고리 인덱스를 색상 인덱스로 사용
            category_data[b.category] = {
                "label": b.category,
                "data": [{
                    "x": r.kyoborank, 
                    "y": index_kyoboupdown, 
                    "r": index_review, 
                    "link": p.kyobourl, 
                    "tooltip": f"{r.kyoborank}. {b.title} ⭐{b.category} {index_kyoboupdown_tip} 리뷰 : {index_review}",
                }],
                "borderColor": f"hsla({random.randint(0,360)}, 100%, 50%, 0.5)",
                "backgroundColor": f"hsla({random.randint(0,360)}, 100%, {random.randint(30,60)}%, 0.5)",
            }
        else:
            category_data[b.category]["data"].append({
                "x": r.kyoborank, 
                "y": index_kyoboupdown, 
                "r": index_review, 
                "link": p.kyobourl, 
                "tooltip": f"{r.kyoborank}. {b.title} ⭐{b.category} {index_kyoboupdown_tip} 리뷰 : {index_review}",
            })

    for x in category_data.values():
        data["datasets"].append(x)
        
    return data
