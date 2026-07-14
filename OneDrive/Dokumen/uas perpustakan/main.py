def login():
    print("=== LOGIN SISTEM PERPUSTAKAAN ===")
    username = input("Username: ")
    password = input("Password: ")
    if username == "admin" and password == "admin":
        print("Login Berhasil!\n")
        return True
    else:
        print("Login Gagal! Coba lagi.\n")
        return False

# Database sederhana (List of Dictionary)
data_buku = [
    {"id": 1, "judul": "Belajar Python Dasar", "penulis": "Budi Santoso"},
    {"id": 2, "judul": "Algoritma dan Struktur Data", "penulis": "Siti Aminah"}
]

def tampilkan_buku():
    print("\n--- Daftar Buku ---")
    if not data_buku:
        print("Data buku kosong.")
    for buku in data_buku:
        print(f"ID: {buku['id']} | Judul: {buku['judul']} | Penulis: {buku['penulis']}")

def tambah_buku():
    id_buku = len(data_buku) + 1
    judul = input("Masukkan Judul Buku: ")
    penulis = input("Masukkan Nama Penulis: ")
    data_buku.append({"id": id_buku, "judul": judul, "penulis": penulis})
    print("Buku berhasil ditambahkan!")

def edit_buku():
    tampilkan_buku()
    try:
        id_edit = int(input("Masukkan ID buku yang ingin diedit: "))
        for buku in data_buku:
            if buku['id'] == id_edit:
                buku['judul'] = input("Judul Baru: ")
                buku['penulis'] = input("Penulis Baru: ")
                print("Data buku berhasil diupdate!")
                return
        print("Buku tidak ditemukan.")
    except ValueError:
        print("Harap masukkan angka ID yang valid!")

def hapus_buku():
    tampilkan_buku()
    try:
        id_hapus = int(input("Masukkan ID buku yang ingin dihapus: "))
        for i, buku in enumerate(data_buku):
            if buku['id'] == id_hapus:
                del data_buku[i]
                print("Buku berhasil dihapus!")
                return
        print("Buku tidak ditemukan.")
    except ValueError:
        print("Harap masukkan angka ID yang valid!")

def cari_buku():
    keyword = input("Masukkan kata kunci (judul/penulis): ").lower()
    hasil = [buku for buku in data_buku if keyword in buku['judul'].lower() or keyword in buku['penulis'].lower()]
    print("\n--- Hasil Pencarian ---")
    if hasil:
        for buku in hasil:
            print(f"ID: {buku['id']} | Judul: {buku['judul']} | Penulis: {buku['penulis']}")
    else:
        print("Buku tidak ditemukan.")

def main_menu():
    if not login():
        return
    
    while True:
        print("\n=== MENU PERPUSTAKAAN KAMPUS ===")
        print("1. Lihat Data Buku")
        print("2. Tambah Data Buku")
        print("3. Edit Data Buku")
        print("4. Hapus Data Buku")
        print("5. Cari Data Buku")
        print("6. Keluar")
        
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == '1': tampilkan_buku()
        elif pilihan == '2': tambah_buku()
        elif pilihan == '3': edit_buku()
        elif pilihan == '4': hapus_buku()
        elif pilihan == '5': cari_buku()
        elif pilihan == '6': 
            print("Terima kasih telah menggunakan sistem.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main_menu()