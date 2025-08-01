from app import db

class Dosen(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nidn = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(25), nullable=False)
    address = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return '<Dosen {}>'.format(self.name)