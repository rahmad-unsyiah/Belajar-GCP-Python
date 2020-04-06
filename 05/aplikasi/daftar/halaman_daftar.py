from flask import render_template, request, jsonify

# Import app dari modul
from aplikasi.daftar import app

# Import model
#from aplikasi.model.anggota import ambil_daftar_anggota
from aplikasi.model.anggota import daftar

# Decorator yang menyatakan kalau:
# + Untuk URL: /daftar
# + Jalankan method ini
# + Tetapi hanya untuk method: HTTP GET
@app.route("/daftar", methods=["GET"])
def tampilkan_halaman_daftar():
    # Panggil business logic untuk tangani permintaa, 
    # dalam hal ini ambil daftar anggota
    daftar_nama = daftar()

    # Serahkan ke Jinja2 untuk ditampilkan sesuai template
    return render_template("daftar.j2", daftar_tampil=daftar_nama)


# Decorator yang menyatakan kalau:
# + Untuk URL: /api/daftar
# + Jalankan method ini
# + Tetapi hanya untuk method: HTTP GET
@app.route("/api/daftar", methods=["GET"])
def api_daftar():
    daftar_peserta = daftar()

    # Harus dibungkus dengan object, karena endpoints tidak bisa langsung array
    daftar_peserta = {"daftar":daftar_peserta}

    # Ubah list dari dictionary ke JSON
    daftar_peserta = jsonify(daftar_peserta)

    # Kembalikan hasilnya dan kode HTTP 200 yang berarti OK (=sukses)
    return daftar_peserta, 200
