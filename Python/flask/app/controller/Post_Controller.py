from app.model.dosen import Dosen
from app.model.mahasiswa import Mahasiswa
from app import response, db
from flask import request

def post_dosen():
    try:
        nidn = request.form.get('nidn')
        name = request.form.get('name')
        phone = request.form.get('phone')
        address = request.form.get('address')

        dosens = Dosen(nidn=nidn, name=name, phone=phone, address=address)
        db.session.add(dosens)
        db.session.commit()

        return response.success([], 'success add new dosen')
    except Exception as e:
        return response.badrequest([], f"Error: {str(e)}")

def post_mahasiswa():
    try:
        nim = request.form.get('nim')
        name = request.form.get('name')
        phone = request.form.get('phone')
        address = request.form.get('address')
        dosen_one = request.form.get('dosen_one')
        dosen_two = request.form.get('dosen_two')

        mahasiswas = Mahasiswa(nim=nim, name=name, phone=phone, address=address, dosen_one=dosen_one, dosen_two=dosen_two)
        db.session.add(mahasiswas)
        db.session.commit()

        return response.success([], 'success add new mahasiswa')
    except Exception as e:
        return response.badrequest([], f"Error: {str(e)}")