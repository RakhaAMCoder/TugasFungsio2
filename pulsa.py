
from fplib import (
    ambil, saring, cari, urutkan,
    kelompokkan, jumlahkan, rata_rata,
    validasi, rupiah
)

transaksi = [
    {"nomor": "081234567890", "operator": "Telkomsel", "nominal": 10000},
    {"nomor": "082345678901", "operator": "Indosat", "nominal": 20000},
    {"nomor": "085678901234", "operator": "XL", "nominal": 50000},
    {"nomor": "081298765432", "operator": "Telkomsel", "nominal": 25000}
]

BIAYA_ADMIN = 2000


def tampilkan(data):
    print("\n--- DAFTAR TRANSAKSI ---")

    for t in data:
        total = t["nominal"] + BIAYA_ADMIN

        print(
            f"Nomor: {t['nomor']} | "
            f"Operator: {t['operator']} | "
            f"Pulsa: {rupiah(t['nominal'])} | "
            f"Total: {rupiah(total)}"
        )


def tambah_transaksi():
    nomor = input("Nomor HP: ")
    operator = input("Operator: ")
    nominal = int(input("Nominal pulsa: "))

    validasi(
        nomor,
        lambda x: x.isdigit() and len(x) >= 10,
        "Nomor HP tidak valid"
    )

    validasi(
        nominal,
        lambda x: x > 0,
        "Nominal harus lebih dari 0"
    )

    transaksi.append({
        "nomor": nomor,
        "operator": operator,
        "nominal": nominal
    })

    print("Transaksi berhasil ditambahkan!")


def cari_transaksi():
    nomor = input("Masukkan nomor HP: ")

    hasil = cari(
        transaksi,
        lambda t: t["nomor"] == nomor
    )

    if hasil:
        tampilkan([hasil])
    else:
        print("Transaksi tidak ditemukan")


def kelompok_operator():
    hasil = kelompokkan(
        transaksi,
        lambda t: t["operator"]
    )

    for operator, daftar in hasil.items():
        print(f"\nOperator: {operator}")
        tampilkan(daftar)


def urut_nominal():
    hasil = urutkan(
        transaksi,
        key=lambda t: t["nominal"],
        terbalik=True
    )

    tampilkan(hasil)


def pulsa_besar():
    hasil = saring(
        transaksi,
        lambda t: t["nominal"] >= 20000
    )

    print("\nPulsa nominal 20.000 ke atas:")
    tampilkan(hasil)


def statistik():
    total = jumlahkan(
        transaksi,
        lambda t: t["nominal"] + BIAYA_ADMIN
    )

    rata = rata_rata(
        transaksi,
        lambda t: t["nominal"]
    )

    print("\n--- STATISTIK PENJUALAN ---")
    print(f"Jumlah transaksi: {len(transaksi)}")
    print(f"Total pemasukan: {rupiah(total)}")
    print(f"Rata-rata nominal pulsa: {rupiah(rata)}")


def menu():
    while True:
        print("\n=== PENJUALAN PULSA ===")
        print("1. Tampilkan transaksi")
        print("2. Tambah transaksi")
        print("3. Cari transaksi")
        print("4. Kelompokkan operator")
        print("5. Urutkan nominal pulsa")
        print("6. Filter pulsa besar")
        print("7. Statistik penjualan")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan(ambil(transaksi, 100))

        elif pilihan == "2":
            tambah_transaksi()

        elif pilihan == "3":
            cari_transaksi()

        elif pilihan == "4":
            kelompok_operator()

        elif pilihan == "5":
            urut_nominal()

        elif pilihan == "6":
            pulsa_besar()

        elif pilihan == "7":
            statistik()

        elif pilihan == "0":
            break

        else:
            print("Pilihan tidak valid")


menu()
