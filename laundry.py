
from fplib import ambil, saring, cari, urutkan, jumlahkan, rata_rata, validasi, rupiah

data = [
    {"nama": "Rina", "kg": 3, "tarif": 7000},
    {"nama": "Budi", "kg": 2, "tarif": 12000}
]

def biaya(x):
    return x["kg"] * x["tarif"]

def tampilkan():
    for x in ambil(data, 100):
        print(x["nama"], x["kg"], "kg", rupiah(biaya(x)))

def tambah():
    nama = input("Nama pelanggan: ")
    kg = validasi(float(input("Berat kg: ")), lambda n: n > 0)
    tarif = 7000

    data.append({"nama": nama, "kg": kg, "tarif": tarif})
    print("Data berhasil ditambahkan")

def menu():
    while True:
        print("""
=== LAUNDRY ===
1. Tampilkan data
2. Tambah laundry
3. Cari pelanggan
4. Urut biaya
5. Total pendapatan
0. Keluar
""")
        p = input("Pilih: ")

        if p == "1":
            tampilkan()

        elif p == "2":
            try:
                tambah()
            except ValueError as e:
                print("Error:", e)

        elif p == "3":
            nama = input("Nama: ").lower()
            hasil = cari(data, lambda x: x["nama"].lower() == nama)
            print(hasil or "Tidak ditemukan")

        elif p == "4":
            for x in urutkan(data, kunci=biaya, terbalik=True):
                print(x["nama"], rupiah(biaya(x)))

        elif p == "5":
            print("Total:", rupiah(jumlahkan(data, biaya)))
            print("Rata-rata:", rupiah(rata_rata(data, biaya)))
            print("Jumlah pelanggan:", len(saring(data, lambda x: x["kg"] > 0)))

        elif p == "0":
            break

if __name__ == "__main__":
    menu()
