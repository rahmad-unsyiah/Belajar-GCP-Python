# Pakai app yang sudah dibuat pada package aplikasi
from aplikasi import app

# Ini jika kita jalankan di command line, diabaikan oleh GCP.
if __name__ == "__main__":
    # Kalau dipanggil dari command line (i.e. python main.py) maka
    #  __name__ = '__main__'
    # Jika diimpor oleh berkas lain, __name__ = 'main' (i.e.nama berkas).
    # Lihat: https://www.geeksforgeeks.org/__name__-special-variable-python/

    # Jalankan aplikasi pada localhost (i.e. 127.0.0.0) dan port 8080
    app.run(host="127.0.0.1", port=8080, debug=True)
