# Berkas untuk nyatakan directory ini adalah sebuah package

# Impor apa-apa saja yang dibutuhkan
from flask import Flask

# Inisialisasi framework
# + Parameter pertama: nama modul ini, biasaya nama package, kalau package utama
#                      pakai __name__ (nama berkas)
# + Parameter kedua: directory untuk template
app = Flask(__name__, template_folder="../templates")

# Umumkan(=muat) apa-apa saja yang akan diperlihatkan ke dunia luar pada 
# package ini
from aplikasi import halaman_utama

# Umumkan(=muat) su-package apa-apa saja yang akan diperlihatkan ke dunia luar
import aplikasi.daftar
import aplikasi.form
