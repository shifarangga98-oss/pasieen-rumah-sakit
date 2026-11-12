
# PROGRAM ADMINISTRASI PASIEN RAWAT INAP RUMAH SAKIT

print("======================================")
print("     SISTEM RAWAT INAP RUMAH SAKIT")
print("======================================")

# Input data pasien
nama = input("Masukkan Nama Pasien       : ")
umur = int(input("Masukkan Umur Pasien       : "))

print("\nPilihan Kelas Rawat Inap:")
print("1. Kelas VIP")
print("2. Kelas 1")
print("3. Kelas 2")
print("4. Kelas 3")

pilihan = int(input("\nPilih Kelas Rawat Inap (1-4): "))
lama = int(input("Lama Menginap (hari)       : "))

# Menentukan biaya berdasarkan kelas
if pilihan == 1:
    kelas = "VIP"
    biaya_kamar = 1000000
    biaya_perawatan = 500000

elif pilihan == 2:
    kelas = "Kelas 1"
    biaya_kamar = 750000
    biaya_perawatan = 400000

elif pilihan == 3:
    kelas = "Kelas 2"
    biaya_kamar = 500000
    biaya_perawatan = 300000

elif pilihan == 4:
    kelas = "Kelas 3"
    biaya_kamar = 300000
    biaya_perawatan = 200000

else:
    kelas = "Tidak tersedia"
    biaya_kamar = 0
    biaya_perawatan = 0

# Proses perhitungan
if pilihan >= 1 and pilihan <= 4 and lama > 0:
    total_kamar = biaya_kamar * lama
    total_perawatan = biaya_perawatan * lama
    total_biaya = total_kamar + total_perawatan

    # Menampilkan hasil
    print("\n======================================")
    print("       STRUK PASIEN RAWAT INAP")
    print("======================================")
    print("Nama Pasien       :", nama)
    print("Umur Pasien       :", umur, "tahun")
    print("Kelas Rawat Inap  :", kelas)
    print("Lama Menginap     :", lama, "hari")
    print("--------------------------------------")
    print("Biaya Kamar       : Rp", total_kamar)
    print("Biaya Perawatan   : Rp", total_perawatan)
    print("--------------------------------------")
    print("TOTAL BIAYA       : Rp", total_biaya)
    print("======================================")

elif pilihan < 1 or pilihan > 4:
    print("\nMaaf, pilihan kelas tidak tersedia.")

else:
    print("\nMaaf, lama menginap harus lebih dari 0 hari.")
