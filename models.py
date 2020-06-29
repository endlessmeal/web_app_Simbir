from config import db
import datetime


# model for every image in database
class ImageEdit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal_type = db.Column(db.String(50), nullable=False)
    processed_image = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<Image %r>' % self.processed_image
