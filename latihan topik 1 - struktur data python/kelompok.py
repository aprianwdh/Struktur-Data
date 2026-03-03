DATA_BASE = []

jumlah_mahasiswa = int(input("masukkan jumlah mahasiswa = "))

for mahasiswa in range(jumlah_mahasiswa):
    nama = input("Masukkan Nama =")
    nim = input("Masukkan Nim =")

    mahasiswa = {nama: nim}
    DATA_BASE.append(mahasiswa)

print(DATA_BASE)
