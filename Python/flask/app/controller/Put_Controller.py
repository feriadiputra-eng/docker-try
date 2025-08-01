from app import response, db
from flask import request
from app.model.dosen import Dosen
from app.model.mahasiswa import Mahasiswa

def put_dosen():
    try:
        id = request.form.get('id')
        nidn = request.form.get('nidn')
        name = request.form.get('name')
        phone = request.form.get('phone')
        address = request.form.get('address')

        input = [
            {
                'nidn': nidn,
                'name': name,
                'phone': phone,
                'address': address
            }
        ]

        dosen = Dosen.query.filter_by(id=id).first()

        dosen.nidn = nidn
        dosen.name = name
        dosen.phone = phone
        dosen.address = address

        db.session.commit()

        return response.success(input, 'success change dosen data')
    except Exception as e:
        return response.badrequest([], f'Error: {str(e)}')

def put_mahasiswa():
    try:
        id = request.form.get('id')
        nim = request.form.get('nim')
        name = request.form.get('name')
        phone = request.form.get('phone')
        address = request.form.get('address')
        dosen_one = request.form.get('dosen_one')
        dosen_two = request.form.get('dosen_two')

        input = [
            {
                'nim': nim,
                'name': name,
                'phone': phone,
                'address': address,
                'dosen_one': dosen_one,
                'dosen_two': dosen_two
            }
        ]

        mahasiswa = Mahasiswa.query.filter_by(id=id).first()

        mahasiswa.nim = nim
        mahasiswa.name = name
        mahasiswa.phone = phone
        mahasiswa.address = address
        mahasiswa.dosen_one = dosen_one
        mahasiswa.dosen_two = dosen_two

        db.session.commit()

        return response.success(input, 'success change mahasiswa data')
    except Exception as e:
        return response.badrequest([], f'Error: {str(e)}')