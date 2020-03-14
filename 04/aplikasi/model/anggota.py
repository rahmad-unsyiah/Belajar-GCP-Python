#
# Controller untuk kind Anggota
#
# Kind Anggota tediri atas property berikut:
# + nama : untuk nama anggota
# + umut : untuk umur anggota
#
from google.cloud import datastore

# Method untuk menambah anggota baru
def tambah(nama, umur):
    # Buat object yang mau disimpan
    anggota = { 'nama':nama, 'umur':umur}

    # Buka koneksi ke datastore
    client = datastore.Client()

    # Minta dibuatkan key baru
    key_baru = client.key("Anggota")
    # Buat entity baru memakai key yang baru dibuat
    entity_baru = datastore.Entity(key=key_baru)
    # Isi data untuk entity baru
    entity_baru.update(anggota)
    # Simpan perubaha data entity baru
    client.put(entity_baru)


# Method untuk mengambil data semua anggota yang ada
def daftar():
    # Buka koneksi ke datastore
    client = datastore.Client()

    # Buat query baru khusus untuk Anggota
    query = client.query(kind="Anggota")
    # Jalankan query, hasilnya berupa iterator
    hasil = query.fetch()
    # Ubah iterator ke list dan kembalikan hasilnya
    return list(hasil)
