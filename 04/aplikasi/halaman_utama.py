from flask import render_template, request

# Import app dari modul
from aplikasi import app

# Decorator yang menyatakan kalau:
# + Untuk URL: /
# + Jalankan method ini
# + Tetapi hanya untuk method: HTTP GET
@app.route("/", methods=["GET"])
def tampilkan_halaman_utama():
    # Ambil parameter dari URL
    nama = request.args.get("nama")
    umur = request.args.get("umur")

    # Render template yang telah kita buat dengan mengirim parameter:
    # + nama: nama untuk ditampilkan pada halaman
    # + umur: umur untuk ditampilkan pada halaman
    return render_template("index.j2", nama=nama, umur=umur)
