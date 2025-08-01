from app.model.dosen import Dosen
from app.model.mahasiswa import Mahasiswa
from app import response, app, db
from flask import request

# --------------- GET dosen ---------------

def format_array_dosen(datas):
    array = []

    for i in datas:
        array.append(single_object_dosen(i))

    return array

def single_object_dosen(data):
    return {
        'id' : data.id,
        'nidn' : data.nidn,
        'name' : data.name,
        'phone' : data.phone,
        'address' : data.address
    }

def get_dosen():
    try:
        dosen = Dosen.query.all()
        data = format_array_dosen(dosen)
        return response.success(data, "success")
    except Exception as e:
        return response.badrequest([], f"Error: {str(e)}")

# --------------- GET mahasiswa ---------------

def format_array_mahasiswa(datas):
    array = []

    for i in datas:
        array.append(single_object_mahasiswa(i))

    return array

def single_object_mahasiswa(data):
    return {
        'id' : data.id,
        'nim' : data.nim,
        'name' : data.name,
        'phone' : data.phone,
        'address' : data.address,
        'dosen_one' : single_object_dosen(data.dosen1) if data.dosen1 else None,
        'dosen_two' : single_object_dosen(data.dosen2) if data.dosen2 else None,
    }

def get_mahasiswa():
    try:
        mahasiswa = Mahasiswa.query.all()
        data = format_array_mahasiswa(mahasiswa)
        return response.success(data, "success")
    except Exception as e:
        return response.badrequest([], f"Error: {str(e)}") 

# --------------- GET dosen by id ---------------

def get_dosen_id(id):
    try:
        dosen = Dosen.query.filter_by(id=id).first()
        mahasiswa = Mahasiswa.query.filter((Mahasiswa.dosen_one == id) | (Mahasiswa.dosen_two == id))

        if not dosen:
            return response.badrequest([], 'no data')

        datamahasiswa = format_Mahasiswa(mahasiswa)

        data = single_detail_mahasiswa(dosen, datamahasiswa)

        return response.success(data, 'success get dosen by id')

    except Exception as e:
        return response.badrequest([], f"Error: {str(e)}") 

def single_detail_mahasiswa(dosen, mahasiswa):
    data = {
        'id' : dosen.id,
        'nidn' : dosen.nidn,
        'name' : dosen.name,
        'phone' : dosen.phone,
        'address' : dosen.address,
        'mahasiswa' : mahasiswa
    }

    return data

def single_Mahasiswa(mahasiswa):
    return {
        'id' : mahasiswa.id,
        'nim' : mahasiswa.nim,
        'name' : mahasiswa.name,
        'phone' : mahasiswa.phone,
        'address' : mahasiswa.address
    }

def format_Mahasiswa(data):
    array = []
    for i in data:
        array.append(single_Mahasiswa(i))
    return array
