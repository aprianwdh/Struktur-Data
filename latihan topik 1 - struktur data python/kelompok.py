DATA_BASE = []

jumlah_mahasiswa = int(input("masukkan jumlah mahasiswa = "))
for mahasiswa in range(jumlah_mahasiswa):
    while True:
        nama = input("Masukkan Nama = ")
        try:
            int(nama)   
            print("Input nama harus berupa huruf!")
        except:
            if nama != "":
                break
            else:
                print("Nama tidak boleh kosong!")

    
    while True:
        nim = input("Masukkan NIM = ")
        try:
            int(nim)   
            break
        except:
            print("Input NIM harus berupa angka!")

    mahasiswa = {nama: nim}
    DATA_BASE.append(mahasiswa)
print("\nData berhasil disimpan!")
       

while True:
    print("\nMenu:")
    print("1. Cari Data Mahasiswa")
    print("2. Hapus Data Mahasiswa")
    print("3. Tampilkan Semua Data")
    print("4. Keluar")

    menu = input("Masukkan pilihan (1/2/3/4) = ")

#CARI DATA
    if menu == "1":
        cari = input("Masukkan nama yang ingin dicari = ")
        ditemukan = False

        for data in DATA_BASE:
            if cari in data:
                print("Data ditemukan, NIM:", data[cari])
                ditemukan = True
                break

        if not ditemukan:
            print("Data tidak ditemukan.")

#HAPUS DATA
    elif menu == "2":
        hapus = input("Masukkan nama mahasiswa yang ingin dihapus = ")
        ditemukan = False

        for data in DATA_BASE:
            if hapus in data:
                DATA_BASE.remove(data)
                print("Data berhasil dihapus.")
                ditemukan = True
                break

        if not ditemukan:
            print("Nama tidak ditemukan.")

#TAMPILKA DATA
    elif menu == "3":
        if len(DATA_BASE) == 0:
            print("Data kosong.")
        else:
            print("\nDaftar Mahasiswa:")
            for data in DATA_BASE:
                for nama, nim in data.items():
                    print("Nama:", nama, " NIM:", nim)

#KELUAR
    elif menu == "4":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid, silakan coba lagi.")
