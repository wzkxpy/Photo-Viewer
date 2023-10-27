from exts import db


class Image(db.Model):
    __tablename__ = 'imageList'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    datetime = db.Column(db.DateTime)
    address = db.Column(db.String(40))
    url = db.Column(db.String(20), nullable=False, unique=True)
