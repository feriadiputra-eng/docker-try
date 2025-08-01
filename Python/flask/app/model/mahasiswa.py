from app import db
from app.model.dosen import Dosen

class Mahasiswa(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nim = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(25), nullable=False)
    address = db.Column(db.String(150), nullable=False)
    dosen_one = db.Column(db.Integer, db.ForeignKey(Dosen.id, ondelete='CASCADE'))
    dosen_two = db.Column(db.Integer, db.ForeignKey(Dosen.id, ondelete='CASCADE'))

    dosen1 = db.relationship('Dosen', foreign_keys=[dosen_one])
    dosen2 = db.relationship('Dosen', foreign_keys=[dosen_two])

    def __repr__(self):
        return '<Mahasiswa {}>'.format(self.name)