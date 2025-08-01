from app import app
from app.controller import Get_Controller, Post_Controller, Put_Controller, Delete_Controller
from flask import request

@app.route("/")
def test():
    return "haha"

@app.route("/secret")
def secret():
    return "<h1>  I Love You</h1><a href='/'> moh</a>"

@app.route("/dosen", methods=['GET','POST','PUT'])
def dosens():
    if request.method == 'GET':
        return Get_Controller.get_dosen()
    elif request.method == 'POST':
        return Post_Controller.post_dosen()
    else:
        return Put_Controller.put_dosen()

@app.route('/dosen/<id>', methods=['GET','DELETE'])
def dosen_id(id):
    if request.method == 'GET':
        return Get_Controller.get_dosen_id(id)
    else:
        return Delete_Controller.delete_dosen(id)

@app.route("/mahasiswa", methods=['GET','POST','PUT'])
def mahasiswas():
    if request.method == 'GET':
        return Get_Controller.get_mahasiswa()
    elif request.method == 'POST':
        return Post_Controller.post_mahasiswa()
    else:
        return Put_Controller.put_mahasiswa()

@app.route('/mahasiswa/<id>', methods=['DELETE'])
def mahasiswa_id(id):
        return Delete_Controller.delete_mahasiswa(id)

if __name__ == "__main__":
    app.run(debug=True)
