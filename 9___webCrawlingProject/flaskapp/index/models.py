from index import db
from datetime import datetime

class Books(db.Model):
    isbn = db.Column(db.String(13), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255))
    publisher = db.Column(db.String(255))
    publishing = db.Column(db.Date)
    coverUrl = db.Column(db.Text)

class KyoboRanking(db.Model):
    rankingId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(13), db.ForeignKey('books.isbn'), nullable=False)
    inputDate = db.Column(db.Date, default=datetime.utcnow)
    kyoboRank = db.Column(db.Integer)
    kyoboRating = db.Column(db.Numeric(3, 1))
    kyoboReview = db.Column(db.Integer)
    book = db.relationship('Books', backref=db.backref('kyobo_rankings', cascade='all, delete-orphan'))

class KyoboPrice(db.Model):
    priceId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(13), db.ForeignKey('books.isbn'), nullable=False)
    inputDate = db.Column(db.Date, default=datetime.utcnow)
    kyoboPrice = db.Column(db.Numeric(10, 2))
    kyoboSalePrice = db.Column(db.Numeric(10, 2))
    kyoboPoint = db.Column(db.Integer)
    kyobourl = db.Column(db.Text)
    book = db.relationship('Books', backref=db.backref('kyobo_prices', cascade='all, delete-orphan'))

class Yes24Ranking(db.Model):
    rankingId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(13), db.ForeignKey('books.isbn'), nullable=False)
    inputDate = db.Column(db.Date, default=datetime.utcnow)
    yes24Rank = db.Column(db.Integer)
    yes24Rating = db.Column(db.Numeric(3, 1))
    yes24Review = db.Column(db.Integer)
    book = db.relationship('Books', backref=db.backref('yes24_rankings', cascade='all, delete-orphan'))

class Yes24Price(db.Model):
    priceId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(13), db.ForeignKey('books.isbn'), nullable=False)
    inputDate = db.Column(db.Date, default=datetime.utcnow)
    yes24Price = db.Column(db.Numeric(10, 2))
    yes24SalePrice = db.Column(db.Numeric(10, 2))
    yes24Point = db.Column(db.Integer)
    yes24url = db.Column(db.Text)
    book = db.relationship('Books', backref=db.backref('yes24_prices', cascade='all, delete-orphan'))

class Average(db.Model):
    priceId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(13), db.ForeignKey('books.isbn'), nullable=False)
    inputDate = db.Column(db.Date, default=datetime.utcnow)
    averageRating = db.Column(db.Numeric(3, 1))
    averageRanking = db.Column(db.Numeric(3, 1))
    averageWeekRanking = db.Column(db.Integer)
    book = db.relationship('Books', backref=db.backref('averages', cascade='all, delete-orphan'))

