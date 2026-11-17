
from fplib import (
    pipe, ambil, saring, cari, urutkan,
    kelompokkan, jumlahkan, rata_rata,
    validasi, rupiah
)

data = [10, 20, 30, 40, 50]

print("=== TEST LIBRARY FPLIB ===")

# 1. Test pipe
hasil = pipe(5, lambda x: x + 5, lambda x: x * 2)
assert hasil == 20
print("1. pipe: BERHASIL")

# 2. Test ambil
hasil = ambil(data, 3)
assert hasil == [10, 20, 30]
print("2. ambil: BERHASIL")

# 3. Test saring
hasil = saring(data, lambda x: x >= 30)
assert hasil == [30, 40, 50]
print("3. saring: BERHASIL")

# 4. Test cari
hasil = cari(data, lambda x: x == 30)
assert hasil == 30
print("4. cari: BERHASIL")

# 5. Test urutkan
hasil = urutkan(data, kunci=lambda x: x, terbalik=True)
assert hasil == [50, 40, 30, 20, 10]
print("5. urutkan: BERHASIL")

# 6. Test kelompokkan
hasil = kelompokkan(
    data,
    lambda x: "Genap" if x % 20 == 0 else "Lainnya"
)
assert hasil["Genap"] == [20, 40]
print("6. kelompokkan: BERHASIL")

# 7. Test jumlahkan
hasil = jumlahkan(data)
assert hasil == 150
print("7. jumlahkan: BERHASIL")

# 8. Test rata_rata
hasil = rata_rata(data)
assert hasil == 30
print("8. rata_rata: BERHASIL")

# 9. Test validasi
hasil = validasi(10, lambda x: x > 0)
assert hasil == 10
print("9. validasi: BERHASIL")

# 10. Test rupiah
hasil = rupiah(10000)
assert hasil == "Rp10.000"
print("10. rupiah: BERHASIL")

print("\nSEMUA TEST BERHASIL!")
