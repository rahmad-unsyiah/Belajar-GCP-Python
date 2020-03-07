from flask import render_template, request

# Import app dari modul
from aplikasi.daftar import app

# Decorator yang menyatakan kalau:
# + Untuk URL: /daftar
# + Jalankan method ini
# + Tetapi hanya untuk method: HTTP GET
@app.route("/daftar", methods=["GET"])
def tampilkan_halaman_daftar():
    daftar_nama = [ {"nama":"Rahmad", "umur":5},
                    {"nama":"Dawood", "umur":15}, 
                    {"nama":"Rahmad Dawood", "umur":25} ]
    return render_template("daftar.j2", daftar_tampil = daftar_nama)
