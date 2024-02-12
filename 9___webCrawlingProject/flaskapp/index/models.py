from index import db
from datetime import date

class Book(db.Model):
    __tablename__ = 'books'
    isbn = db.Column(db.String(13), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255))
    publisher = db.Column(db.String(255))
    publishing = db.Column(db.Date)
    coverurl = db.Column(db.Text)

class KyoboRanking(db.Model):
    __tablename__ = 'kyobo_ranking'
    rankingId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(13), db.ForeignKey('books.isbn'), nullable=False)
    inputdate = db.Column(db.Date, default=date.today)
    kyoborank = db.Column(db.Integer)
    kyoborating = db.Column(db.Numeric(3,1))
    kyoboreview = db.Column(db.Integer)
    kyoboupdown = db.Column(db.Integer)
    book = db.relationship('Book', backref=db.backref('kyobo_rankings', lazy=True))

class KyoboPrice(db.Model):
    __tablename__ = 'kyobo_price'
    priceid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(13), db.ForeignKey('books.isbn'), nullable=False)
    inputdate = db.Column(db.Date, default=date.today)
    kyoboprice = db.Column(db.Numeric(10,2))
    kyobosaleprice = db.Column(db.Numeric(10,2))
    kyobopoint = db.Column(db.Integer)
    kyobourl = db.Column(db.Text)
    book = db.relationship('Book', backref=db.backref('kyobo_prices', lazy=True))

class Yes24Ranking(db.Model):
    __tablename__ = 'yes24_ranking'
    rankingid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(13), db.ForeignKey('books.isbn'), nullable=False)
    inputdate = db.Column(db.Date, default=date.today)
    yes24rank = db.Column(db.Integer)
    yes24rating = db.Column(db.Numeric(3,1))
    yes24review = db.Column(db.Integer)
    yes24updown = db.Column(db.Integer)
    book = db.relationship('Book', backref=db.backref('yes24_rankings', lazy=True))

class Yes24Price(db.Model):
    __tablename__ = 'yes24_price'
    priceid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(13), db.ForeignKey('books.isbn'), nullable=False)
    inputdate = db.Column(db.Date, default=date.today)
    yes24price = db.Column(db.Numeric(10,2))
    yes24saleprice = db.Column(db.Numeric(10,2))
    yes24point = db.Column(db.Integer)
    yes24url = db.Column(db.Text)
    book = db.relationship('Book', backref=db.backref('yes24_prices', lazy=True))

class Average(db.Model):
    __tablename__ = 'average'
    priceid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(13), db.ForeignKey('books.isbn'), nullable=False)
    inputdate = db.Column(db.Date, default=date.today)
    averagerating = db.Column(db.Numeric(3,1))
    averageranking = db.Column(db.Numeric(3,1))
    averageweekranking = db.Column(db.Numeric(3,1))
    book = db.relationship('Book', backref=db.backref('averages', lazy=True))


