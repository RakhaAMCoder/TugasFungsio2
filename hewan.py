
from fplib import (
    ambil, saring, cari, urutkan,
    kelompokkan, rata_rata, validasi
)

hewan = [
    {"nama": "Milo", "jenis": "Kucing", "umur": 2, "berat": 4},
    {"nama": "Bruno", "jenis": "Anjing", "umur": 5, "berat": 12},
    {"nama": "Luna", "jenis": "Kucing", "umur": 3, "berat": 3},
    {"nama": "Max", "jenis": "Anjing", "umur": 7, "berat": 20}
]


def tampilkan(data):
    print("\n--- DAFTAR HEWAN ---")

    for h in data:
        print(
            f"Nama: {h['nama']} | "
            f"Jenis: {h['jenis']} | "
            f"Umur: {h['umur']} tahun | "
            f"Berat: {h['berat']} kg"
        )


def tambah_hewan():
    nama = input("Nama hewan: ")
    jenis = input("Jenis hewan: ")
    umur = int(input("Umur hewan: "))
    berat = float(input("Berat hewan (kg): "))

    validasi(umur, lambda x: x >= 0, "Umur tidak valid")
    validasi(berat, lambda x: x > 0, "Berat tidak valid")

    hewan.append({
        "nama": nama,
        "jenis": jenis,
        "umur": umur,
        "berat": berat
    })

    print("Hewan berhasil ditambahkan!")


def cari_hewan():
    nama = input("Masukkan nama hewan: ")

    hasil = cari(
        hewan,
        lambda h: h["nama"].lower() == nama.lower()
    )

    if hasil:
        tampilkan([hasil])
    else:
        print("Hewan tidak ditemukan")


def kelompok_jenis():
    hasil = kelompokkan(
        hewan,
        lambda h: h["jenis"]
    )

    for jenis, daftar in hasil.items():
        print(f"\nJenis: {jenis}")
        tampilkan(daftar)


def urut_berat():
    hasil = urutkan(
        hewan,
        key=lambda h: h["berat"]
    )

    tampilkan(hasil)


def hewan_tua():
    hasil = saring(
        hewan,
        lambda h: h["umur"] >= 5
    )

    print("\nHewan berumur 5 tahun ke atas:")
    tampilkan(hasil)


def statistik():
    rata = rata_rata(
        hewan,
        lambda h: h["umur"]
    )

    print(f"Rata-rata umur hewan: {rata:.1f} tahun")


def menu():
    while True:
        print("\n=== MANAJEMEN HEWAN ===")
        print("1. Tampilkan hewan")
        print("2. Tambah hewan")
        print("3. Cari hewan")
        print("4. Kelompokkan berdasarkan jenis")
        print("5. Urutkan berdasarkan berat")
        print("6. Tampilkan hewan tua")
        print("7. Statistik umur")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan(ambil(hewan, 100))

        elif pilihan == "2":
            tambah_hewan()

        elif pilihan == "3":
            cari_hewan()

        elif pilihan == "4":
            kelompok_jenis()

        elif pilihan == "5":
            urut_berat()

        elif pilihan == "6":
            hewan_tua()

        elif pilihan == "7":
            statistik()

        elif pilihan == "0":
            break

        else:
            print("Pilihan tidak valid")


menu()
