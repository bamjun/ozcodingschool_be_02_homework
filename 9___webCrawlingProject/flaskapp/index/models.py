from index import db
from datetime import datetime

class books(db.Model):
    __tablename__ = 'books'
    isbn = db.Column(db.String(13), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255))
    publisher = db.Column(db.String(255))
    publishing = db.Column(db.Date)
    coverurl = db.Column(db.Text)
    category = db.Column(db.String(20))


class kyoboranking(db.Model):
    __tablename__ = 'kyobo_ranking'
    rankingid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(13), db.ForeignKey('books.isbn'), nullable=False)
    inputdate = db.Column(db.Date, default=datetime.utcnow)
    kyoborank = db.Column(db.Integer)
    kyoborating = db.Column(db.Numeric(3, 1))
    kyoboreview = db.Column(db.Integer)
    kyoboupdown = db.Column(db.Integer)
    book = db.relationship('books', backref=db.backref('kyobo_ranking', cascade='all, delete-orphan'))

class kyoboprice(db.Model):
    __tablename__ = 'kyobo_price'
    priceid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(13), db.ForeignKey('books.isbn'), nullable=False)
    inputdate = db.Column(db.Date, default=datetime.utcnow)
    kyoboprice = db.Column(db.Numeric(10, 2))
    kyobosaleprice = db.Column(db.Numeric(10, 2))
    kyobopoint = db.Column(db.Integer)
    kyobourl = db.Column(db.Text)
    book = db.relationship('books', backref=db.backref('kyobo_price', cascade='all, delete-orphan'))

class Yes24Ranking(db.Model):
    __tablename__ = 'yes24_ranking'
    rankingid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(13), db.ForeignKey('books.isbn'), nullable=False)
    inputdate = db.Column(db.Date, default=datetime.utcnow)
    yes24rank = db.Column(db.Integer)
    yes24rating = db.Column(db.Numeric(3, 1))
    yes24review = db.Column(db.Integer)
    yes24updown = db.Column(db.Integer)
    book = db.relationship('books', backref=db.backref('yes24_ranking', cascade='all, delete-orphan'))

class Yes24Price(db.Model):
    __tablename__ = 'yes24_price'
    priceid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(13), db.ForeignKey('books.isbn'), nullable=False)
    inputdate = db.Column(db.Date, default=datetime.utcnow)
    yes24price = db.Column(db.Numeric(10, 2))
    yes24saleprice = db.Column(db.Numeric(10, 2))
    yes24point = db.Column(db.Integer)
    yes24url = db.Column(db.Text)
    book = db.relationship('books', backref=db.backref('yes24_price', cascade='all, delete-orphan'))


class average(db.Model):
    __tablename__ = 'average'
    priceid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(13), db.ForeignKey('books.isbn'), nullable=False)
    inputdate = db.Column(db.Date, default=datetime.utcnow)
    averagerating = db.Column(db.Numeric(3, 1))
    averageranking = db.Column(db.Numeric(3, 1))
    averageweekranking = db.Column(db.Integer)
    book = db.relationship('books', backref=db.backref('averages', cascade='all, delete-orphan'))











# from index import db
# from datetime import date

# class books(db.Model):
#     __tablename__ = 'books'
#     isbn = db.Column(db.String(13), primary_key=True)
#     title = db.Column(db.String(255), nullable=False)
#     author = db.Column(db.String(255))
#     publisher = db.Column(db.String(255))
#     publishing = db.Column(db.Date)
#     coverurl = db.Column(db.Text)

# class kyoboranking(db.Model):
#     __tablename__ = 'kyobo_ranking'
#     rankingid = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     isbn = db.Column(db.String(13), db.ForeignKey('books.isbn'), nullable=False)
#     inputdate = db.Column(db.Date, default=date.today)
#     kyoborank = db.Column(db.Integer)
#     kyoborating = db.Column(db.Numeric(3,1))
#     kyoboreview = db.Column(db.Integer)
#     kyoboupdown = db.Column(db.Integer)
#     book = db.relationship('books', backref=db.backref('kyobo_rankings', lazy=True))

# class kyoboprice(db.Model):
#     __tablename__ = 'kyobo_price'
#     priceid = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     isbn = db.Column(db.String(13), db.ForeignKey('books.isbn'), nullable=False)
#     inputdate = db.Column(db.Date, default=date.today)
#     kyoboprice = db.Column(db.Numeric(10,2))
#     kyobosaleprice = db.Column(db.Numeric(10,2))
#     kyobopoint = db.Column(db.Integer)
#     kyobourl = db.Column(db.Text)
#     book = db.relationship('books', backref=db.backref('kyobo_prices', lazy=True))

# class Yes24Ranking(db.Model):
#     __tablename__ = 'yes24_ranking'
#     rankingid = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     isbn = db.Column(db.String(13), db.ForeignKey('books.isbn'), nullable=False)
#     inputdate = db.Column(db.Date, default=date.today)
#     yes24rank = db.Column(db.Integer)
#     yes24rating = db.Column(db.Numeric(3,1))
#     yes24review = db.Column(db.Integer)
#     yes24updown = db.Column(db.Integer)
#     book = db.relationship('books', backref=db.backref('yes24_rankings', lazy=True))

# class Yes24Price(db.Model):
#     __tablename__ = 'yes24_price'
#     priceid = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     isbn = db.Column(db.String(13), db.ForeignKey('books.isbn'), nullable=False)
#     inputdate = db.Column(db.Date, default=date.today)
#     yes24price = db.Column(db.Numeric(10,2))
#     yes24saleprice = db.Column(db.Numeric(10,2))
#     yes24point = db.Column(db.Integer)
#     yes24url = db.Column(db.Text)
#     book = db.relationship('books', backref=db.backref('yes24_prices', lazy=True))

# class Average(db.Model):
#     __tablename__ = 'average'
#     priceid = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     isbn = db.Column(db.String(13), db.ForeignKey('books.isbn'), nullable=False)
#     inputdate = db.Column(db.Date, default=date.today)
#     averagerating = db.Column(db.Numeric(3,1))
#     averageranking = db.Column(db.Numeric(3,1))
#     averageweekranking = db.Column(db.Numeric(3,1))
#     book = db.relationship('books', backref=db.backref('averages', lazy=True))

