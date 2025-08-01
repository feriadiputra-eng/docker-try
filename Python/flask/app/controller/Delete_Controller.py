from app import response, db
from flask import request
from app.model.dosen import Dosen
from app.model.mahasiswa import Mahasiswa

def delete_dosen(id):
    try:
        dosen = Dosen.query.filter_by(id=id).first()
        if not dosen:
            return response.badrequest([], 'cannot find with that id')
        
        db.session.delete(dosen)
        db.session.commit()

        return response.success([], 'success delete dosen data')
    except Exception as e:
        return response.badrequest([], f'Error: {str(e)}')

def delete_mahasiswa(id):
    try:
        mahasiswa = Mahasiswa.query.filter_by(id=id).first()
        if not mahasiswa:
            return response.badrequest([], 'cannot find with that id')
        
        db.session.delete(mahasiswa)
        db.session.commit()

        return response.success([], 'success delete mahasiswa data')
    except Exception as e:
        return response.badrequest([], f'Error: {str(e)}')