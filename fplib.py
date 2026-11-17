
# fplib.py
# Library bersama untuk 5 aplikasi

from functools import reduce


# 1. PIPE
def pipe(data, *fungsi):
    return reduce(lambda hasil, f: f(hasil), fungsi, data)


# 2. AMBIL
def ambil(data, jumlah=5):
    return data[:jumlah]


# 3. SARING
def saring(data, kondisi):
    return list(filter(kondisi, data))


# 4. CARI
def cari(data, kondisi):
    return next((x for x in data if kondisi(x)), None)


# 5. URUTKAN
def urutkan(data, kunci=None, terbalik=False):
    return sorted(data, key=kunci, reverse=terbalik)


# 6. KELOMPOKKAN
def kelompokkan(data, kunci):
    hasil = {}

    for item in data:
        kategori = kunci(item)
        hasil.setdefault(kategori, []).append(item)

    return hasil


# 7. JUMLAHKAN
def jumlahkan(data, kunci=lambda x: x):
    return sum(kunci(x) for x in data)


# 8. RATA-RATA
def rata_rata(data, kunci=lambda x: x):
    data = list(data)

    if not data:
        return 0

    return jumlahkan(data, kunci) / len(data)


# 9. VALIDASI
def validasi(nilai, kondisi, pesan="Data tidak valid"):
    if not kondisi(nilai):
        raise ValueError(pesan)

    return nilai


# 10. RUPIAH
def rupiah(nilai):
    return "Rp" + f"{nilai:,.0f}".replace(",", ".")
