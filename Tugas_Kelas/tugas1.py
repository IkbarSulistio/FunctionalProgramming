# Data akun
users = {}  # {username: (username, password, role)}

# Data barang
barang = []  # Format [{'item_id': 1, 'item': 'Keyboard', 'stok': 10, 'harga': 100000}]

# Main Menu
def main():
    while True:
        print("\nMain Menu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Pilih: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

# Register
def register():
    print("\nRegistrasi Akun:")
    username = input("Masukkan username: ")
    
    if username in users:
        print("Username sudah terdaftar. Silakan pilih username lain.")
        return
    
    password = input("Masukkan password: ")
    role = input("Masukkan role (penjual/pembeli): ").lower()

    if role not in ['penjual', 'pembeli']:
        print("Role tidak valid! Harus 'penjual' atau 'pembeli'.")
        return

    users[username] = (username, password, role)
    print(f"Akun {role} dengan username '{username}' berhasil didaftarkan!")

# Login
def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in users and users[username][1] == password:
        print(f"Selamat datang, {username}!")
        if users[username][2] == 'penjual':
            seller_menu()
        elif users[username][2] == 'pembeli':
            buyer_menu()
    else:
        print("Username atau password salah!")

# Seller Menu
def seller_menu():
    while True:
        print("\nMenu Penjual:")
        print("1. Tambahkan Barang")
        print("2. Lihat Barang")
        print("3. Update Barang")
        print("4. Hapus Barang")
        print("5. Logout")
        choice = input("Pilih: ")

        if choice == "1":
            tambah_barang()
        elif choice == "2":
            lihat_barang()
        elif choice == "3":
            update_barang()
        elif choice == "4":
            hapus_barang()
        elif choice == "5":
            print("Logout...")
            break
        else:
            print("Pilihan tidak ada. Coba lagi.")

# Buyer Menu
def buyer_menu():
    while True:
        print("\nMenu Pembeli:")
        print("1. Lihat Barang Tersedia")
        print("2. Beli Barang")
        print("3. Logout")
        choice = input("Pilih: ")

        if choice == "1":
            lihat_barang_tersedia()
        elif choice == "2":
            beli_barang()
        elif choice == "3":
            print("Logout...")
            break
        else:
            print("Pilihan tidak ada. Coba lagi.")

# Tambah Barang (Penjual)
def tambah_barang():
    print("\nTambah Barang:")
    item = input("Masukkan nama barang: ")
    stok = int(input("Masukkan jumlah stok: "))
    harga = int(input("Masukkan harga barang: "))
    item_id = len(barang) + 1
    barang.append({'item_id': item_id, 'item': item, 'stok': stok, 'harga': harga})
    print(f"Barang {item} berhasil ditambahkan!")

# Lihat Barang (Penjual)
def lihat_barang():
    print("\nDaftar Barang:")
    if not barang:
        print("Tidak ada barang yang tersedia.")
    else:
        for item in barang:
            print(f"ID: {item['item_id']}, Barang: {item['item']}, Stok: {item['stok']}, Harga: {item['harga']}")

# Update Barang (Penjual)
def update_barang():
    print("\nUpdate Barang:")
    lihat_barang()
    item_id = int(input("Masukkan ID barang yang ingin diupdate: "))
    for item in barang:
        if item['item_id'] == item_id:
            new_item = input(f"Nama baru ({item['item']}): ") or item['item']
            new_stok = int(input(f"Stok baru ({item['stok']}): ")) or item['stok']
            new_harga = int(input(f"Harga baru ({item['harga']}): ")) or item['harga']
            item.update({'item': new_item, 'stok': new_stok, 'harga': new_harga})
            print(f"Barang {item_id} berhasil diupdate!")
            break
    else:
        print("ID barang tidak ditemukan.")

# Hapus Barang (Penjual)
def hapus_barang():
    print("\nHapus Barang:")
    lihat_barang()
    item_id = int(input("Masukkan ID barang yang ingin dihapus: "))
    for item in barang:
        if item['item_id'] == item_id:
            barang.remove(item)
            print(f"Barang {item['item']} berhasil dihapus.")
            break
    else:
        print("ID barang tidak ditemukan.")

# Lihat Barang Tersedia (Pembeli)
def lihat_barang_tersedia():
    print("\nBarang Tersedia:")
    available = [item for item in barang if item['stok'] > 0]
    if not available:
        print("Tidak ada barang yang tersedia.")
    else:
        for item in available:
            print(f"ID: {item['item_id']}, Barang: {item['item']}, Stok: {item['stok']}, Harga: {item['harga']}")

# Beli Barang (Pembeli)
def beli_barang():
    print("\nBeli Barang:")
    lihat_barang_tersedia()
    item_id = int(input("Masukkan ID barang yang ingin dibeli: "))
    for item in barang:
        if item['item_id'] == item_id and item['stok'] > 0:
            item['stok'] -= 1
            print(f"Anda berhasil membeli {item['item']}! Stok sekarang: {item['stok']}")
            break
    else:
        print("ID barang tidak ditemukan atau stok habis.")

# Menjalankan program
main()
