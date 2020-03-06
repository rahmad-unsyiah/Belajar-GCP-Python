# Pakai
# + Flask: Web Framework
# + render_template: Jinja2 untuk bangkitkan halaman dari template
from flask import Flask, render_template

# Inisialisasi framework
# + Parameter pertama: nama modul ini, biasaya nama package, kalau package utama
#                      pakai __name__ (nama berkas)
# + Parameter kedua: directory untuk template
app = Flask(__name__, template_folder="templates")

# Decorator yang menyatakan kalau:
# + Untuk URL: /
# + Jalankan method ini
# + Tetapi hanya untuk method: HTTP GET
@app.route("/", methods=["GET"])
def halaman_utama():
    # Render template yang telah kita buat dengan mengirim parameter:
    # + nama: nama untuk ditampilkan pada halaman
    return render_template("index.j2", nama="Rahmad Dawood")


# Ini jika kita jalankan di command line, diabaikan oleh GCP.
if __name__ == "__main__":
    # Kalau dipanggil dari command line (i.e. python main.py) maka
    #  __name__ = '__main__'
    # Jika diimpor oleh berkas lain, __name__ = 'main' (i.e.nama berkas).
    # Lihat: https://www.geeksforgeeks.org/__name__-special-variable-python/

    # Jalankan aplikasi pada localhost (i.e. 127.0.0.0) dan port 8080
    app.run(host="127.0.0.1", port=8080, debug=True)
