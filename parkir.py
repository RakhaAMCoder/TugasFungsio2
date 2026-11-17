
from fplib import ambil, saring, cari, urutkan, kelompokkan, jumlahkan, rata_rata, validasi, rupiah

# Data kendaraan
kendaraan = [
    {"plat": "N 1234 AB", "jenis": "Motor", "jam": 2},
    {"plat": "N 5678 CD", "jenis": "Mobil", "jam": 3}
]

# Menghitung biaya parkir
def biaya(x):
    if x["jenis"] == "Motor":
        tarif = 2000
    else:
        tarif = 5000

    return x["jam"] * tarif

# Menampilkan kendaraan
def tampilkan():
    print("\n=== DATA PARKIR ===")

    for x in ambil(kendaraan, 100):
        print(
            x["plat"],
            "|", x["jenis"],
            "|", x["jam"], "jam",
            "|", rupiah(biaya(x))
        )

# Menambahkan kendaraan
def tambah():
    plat = input("Nomor plat: ").strip().upper()

    jenis = input("Jenis kendaraan (Motor/Mobil): ").strip().title()

    validasi(
        jenis,
        lambda x: x in ["Motor", "Mobil"],
        "Jenis kendaraan harus Motor atau Mobil"
    )

    jam = validasi(
        int(input("Lama parkir (jam): ")),
        lambda x: x > 0,
        "Jam parkir harus lebih dari 0"
    )

    kendaraan.append({
        "plat": plat,
        "jenis": jenis,
        "jam": jam
    })

    print("Kendaraan berhasil dicatat!")

# Menu utama
def menu():
    while True:
        print("""
=== MANAJEMEN PARKIR ===
1. Tampilkan kendaraan
2. Tambah kendaraan
3. Cari kendaraan
4. Kelompokkan kendaraan
5. Urutkan biaya parkir
6. Ringkasan pendapatan
0. Keluar
""")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan()

        elif pilihan == "2":
            try:
                tambah()
            except ValueError as e:
                print("Error:", e)

        elif pilihan == "3":
            plat = input("Plat nomor: ").strip().upper()

            hasil = cari(
                kendaraan,
                lambda x: x["plat"] == plat
            )

            print(hasil or "Kendaraan tidak ditemukan")

        elif pilihan == "4":
            hasil = kelompokkan(
                kendaraan,
                lambda x: x["jenis"]
            )

            for jenis, data in hasil.items():
                print(jenis, "-", len(data), "kendaraan")

        elif pilihan == "5":
            hasil = urutkan(
                kendaraan,
                kunci=biaya,
                terbalik=True
            )

            for x in hasil:
                print(x["plat"], rupiah(biaya(x)))

        elif pilihan == "6":
            print(
                "Total pendapatan:",
                rupiah(jumlahkan(kendaraan, biaya))
            )

            print(
                "Rata-rata biaya:",
                rupiah(rata_rata(kendaraan, biaya))
            )

            motor = saring(
                kendaraan,
                lambda x: x["jenis"] == "Motor"
            )

            print("Jumlah motor:", len(motor))

        elif pilihan == "0":
            break

        else:
            print("Pilihan tidak tersedia")

if __name__ == "__main__":
    menu()
