
from fplib import ambil, saring, cari, urutkan, kelompokkan, jumlahkan, validasi, rupiah

# Data menu makanan
menu_harga = {
    "Nasi Goreng": 15000,
    "Mie Ayam": 12000,
    "Es Teh": 5000
}

# Data pesanan awal
pesanan = [
    {"nama": "Ayu", "menu": "Nasi Goreng", "jumlah": 2},
    {"nama": "Doni", "menu": "Es Teh", "jumlah": 3}
]

# Menghitung total harga pesanan
def total(x):
    return menu_harga[x["menu"]] * x["jumlah"]

# Menampilkan pesanan
def tampilkan():
    print("\n=== DAFTAR PESANAN ===")

    for x in ambil(pesanan, 100):
        print(
            x["nama"],
            "|", x["menu"],
            "|", x["jumlah"], "porsi",
            "|", rupiah(total(x))
        )

# Menambahkan pesanan
def tambah():
    nama = input("Nama pelanggan: ").strip()

    print("Menu tersedia:", ", ".join(menu_harga))

    makanan = input("Nama makanan: ").strip().title()

    validasi(
        makanan,
        lambda x: x in menu_harga,
        "Menu tidak tersedia"
    )

    jumlah = validasi(
        int(input("Jumlah porsi: ")),
        lambda x: x > 0,
        "Jumlah harus lebih dari 0"
    )

    pesanan.append({
        "nama": nama,
        "menu": makanan,
        "jumlah": jumlah
    })

    print("Pesanan berhasil ditambahkan!")

# Menu utama
def menu():
    while True:
        print("""
=== PEMESANAN MAKANAN ===
1. Lihat menu makanan
2. Tampilkan pesanan
3. Tambah pesanan
4. Cari pelanggan
5. Kelompokkan menu
6. Urutkan pesanan
7. Total penjualan
0. Keluar
""")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            for makanan, harga in menu_harga.items():
                print(makanan, "-", rupiah(harga))

        elif pilihan == "2":
            tampilkan()

        elif pilihan == "3":
            try:
                tambah()
            except ValueError as e:
                print("Error:", e)

        elif pilihan == "4":
            nama = input("Nama pelanggan: ").lower()

            hasil = saring(
                pesanan,
                lambda x: x["nama"].lower() == nama
            )

            print(hasil or "Pesanan tidak ditemukan")

        elif pilihan == "5":
            hasil = kelompokkan(
                pesanan,
                lambda x: x["menu"]
            )

            for makanan, data in hasil.items():
                print(
                    makanan,
                    "-",
                    jumlahkan(data, lambda x: x["jumlah"]),
                    "porsi"
                )

        elif pilihan == "6":
            hasil = urutkan(
                pesanan,
                kunci=total,
                terbalik=True
            )

            for x in hasil:
                print(x["nama"], rupiah(total(x)))

        elif pilihan == "7":
            print(
                "Total penjualan:",
                rupiah(jumlahkan(pesanan, total))
            )

        elif pilihan == "0":
            break

        else:
            print("Pilihan tidak tersedia")

if __name__ == "__main__":
    menu()
