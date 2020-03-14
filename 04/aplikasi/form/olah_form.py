from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

# Pakai app dari package yang diatasnya
from aplikasi.form import app

# Import model
from aplikasi.model.anggota import tambah

# Decorator yang menyatakan kalau:
# + Untuk URL: /daftar
# + Jalankan method ini
# + Tetapi hanya untuk method: HTTP POST
@app.route("/form", methods=["POST"])
def form_anggota():
    # Ambil parameter dari form
    nama = request.form.get("txtNama")
    umur = request.form.get("txtUmur")
    umur = int(umur)

    # Panggil business logic untuk tangani permintaan,
    # dalam ha ini tambah anggota baru
    tambah(nama, umur)

    # Buat URL untuk redirect dengan mengirimkan dua parameter: nama dan umur
    # Perhatikan: 
    # + Parameter pertama adalah nama method yang ingin dijalankan,
    #   Flask akan mencari URL yang dapat menjalankan method ini, 
    #   sesuai .route yang terdaftar.
    # + Paramerter selanjutnya adalaha parameter yang akan dikirim, 
    #   disini ada dua, yaitu yang bernama: nama dan umur.
    url = url_for("tampilkan_halaman_utama", nama=nama, umur=umur)

    # Redirect ke URL yang telah dibangun
    return redirect(url)

