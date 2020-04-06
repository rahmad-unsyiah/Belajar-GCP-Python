# Berkas untuk nyatakan directory ini adalah sebuah package

# Impor apa-apa saja yang dibutuhkan
from flask import Flask

# Inisialisasi framework
# + Parameter pertama: nama modul ini, biasaya nama package, kalau package utama
#                      pakai __name__ (nama berkas)
# + Parameter kedua: directory untuk template
app = Flask(__name__, template_folder="../templates")

# Paksa muat semua atur untuk view agar semua app.route terdata 
from aplikasi import halaman_utama
import aplikasi.daftar
import aplikasi.form
