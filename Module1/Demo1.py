users = {}  # {code: (code, password)} -> Primary Key: code
profiles = {}  # {code: {'nama': name, 'email': email, 'role': role}} -> Foreign Key: code
collection = {}  # {code: [{'item_id': id, 'item': 'keyboard', 'quantity': 1}]} -> Foreign Key: code

# Main Menu
def main():
    while True:
        print("\nMain Menu:")
        print("1. Register")
        print("2. Login")
        print("3. User")
        print("4. Exit")
        choice = input("Masukkan pilihan: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            user()
        elif choice == "4":
            print("Keluar...")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")
            
# Register
def register():
    code = input("Masukkan Code: ")
    if code in users:
        print("Code sudah terdaftar.")
        return

    password = input("Masukkan Password: ")
    users[code] = (code, password)
    print("Pendaftaran Berhasil!")

    # Create profile
    skip = input("Apakah anda ingin melengkapi profile sekarang? (y/n): ")
    if skip.lower() == 'y':
        name = input("Masukkan nama: ")
        role = input("Pilih role (Hobbyist/Collector): ")
        email = input("Masukkan email: ")
        profiles[code] = {'nama': name, 'role': role, 'email': email}
    else:
        profiles[code] = {'nama': '', 'role': '', 'email': ''}

    collection[code] = []

    skip_collection = input("Apakah anda ingin menambahkan Collection? (y/n): ")
    if skip_collection.lower() == 'y':
        while True:
            item = input("Masukkan nama item: ")
            quantity = int(input("Masukkan jumlah: "))
            item_id = len(collection[code]) + 1
            collection[code].append({'item_id': item_id, 'item': item, 'quantity': quantity})
            another = input("Apakah anda ingin menambahkan item lain? (y/n): ")
            if another.lower() == 'n':
                break

    print("Pendaftaran Berhasil!")
    
# Login
def login():
    code = input("Masukkan Code: ")
    password = input("Masukkan Password: ")

    if code in users and users[code][1] == password:
        print(f"Selamat datang {profiles[code]['nama']}!")
        user_menu(code)
    else:
        print("Code atau password salah.")

# User Menu
def user_menu(code):
    while True:
        print("\nUser Menu:")
        print("1. Profile")
        print("2. Collection")
        print("3. Logout")
        choice = input("Pilih: ")

        if choice == "1":
            profile_menu(code)
        elif choice == "2":
            collection_menu(code)
        elif choice == "3":
            print("Logged out.")
            break
        else:
            print("Pilihan tidak ada. Coba lagi.")
            
# Menu user
def user():
    while True:
        print("\nMenu:")
        print("1. Daftar Pengguna")
        print("2. User Update")
        print("3. Delete User")
        print("4. Exit")
        choice = input("Pilih: ")

        if choice == "1":
            daftar_pengguna()
        elif choice == "2":
            user_update()
        elif choice == "3":
            user_delete()
        elif choice == "4":
            break
        else:
            print("Pilihan tidak ada. Coba lagi.")

# List User
def daftar_pengguna():
    print("\nDaftar Pengguna:")
    for user_code, (user_code, _) in users.items():
        print(f"Code: {user_code}")

#Update User
def user_update():
    print("\nUpdate User:")
    update_code = input("Masukkan code pengguna yang ingin diupdate: ")
    if update_code in users:
        new_password = input("Masukkan password baru: ")
        users[update_code] = (update_code, new_password)
        print("Password berhasil diupdate!")
    else:
        print("Code tidak ditemukan.")

# User Delete
def user_delete():
    print("\nCRUD pada Users - Delete:")
    delete_code = input("Masukkan code pengguna yang ingin dihapus: ")
    if delete_code in users:
        del users[delete_code]
        print("Pengguna berhasil dihapus!")
    else:
        print("Code tidak ditemukan.")
        
# Profile Menu
def profile_menu(code):
    while True:
        print("\nUser Menu:")
        print("1. View Profile")
        print("2. Edit Profile")
        print("4. Exit")
        choice = input("Pilih: ")

        if choice == "1":
            view_profile(code)
        elif choice == "2":
            edit_profile(code)
        elif choice == "4":
            break
        else:
            print("Pilihan tidak ada. Coba lagi.")

# View Profile
def view_profile(code):
    profile = profiles.get(code, {})
    print("\nProfile Details:")
    print(f"Nama: {profile.get('nama', 'N/A')}")
    print(f"Email: {profile.get('email', 'N/A')}")
    print(f"Role: {profile.get('role', 'N/A')}")

# Edit Profile
def edit_profile(code):
    print("\nEdit Profile:")
    name = input("Masukkan Nama baru: ")
    email = input("Masukkan Email baru: ")
    role = input("Masukkan Role baru: ")
    profiles[code] = {'nama': name, 'email': email, 'role': role}
    print("Profile berhasil diupdate!")
    
# Collection Menu
def collection_menu(code):
    while True:
        print("\nUser Menu:")
        print("1. Tambahkan Koleksi")
        print("2. List Koleksi")
        print("3. Update Koleksi")
        print("4. Hapus Koleksi")
        print("5. Exit")
        choice = input("Pilih: ")

        if choice == "1":
            collection_create(code)
        elif choice == "2":
            collection_read(code)
        elif choice == "3":
            collection_update(code)
        elif choice == "4":
            collection_delete(code)
        elif choice == "5":
            break
        else:
            print("Pilihan tidak ada. Coba lagi.")

# Collection Create
def collection_create(code):
    print("\nCreate Koleksi:")
    item = input("Masukkan nama item: ")
    quantity = int(input("Masukkan jumlah: "))
    item_id = len(collection[code]) + 1
    collection[code].append({'item_id': item_id, 'item': item, 'quantity': quantity})
    print("Item berhasil ditambahkan ke koleksi!")

# Collection Read
def collection_read(code):
    print("\nList Koleksi:")
    collection_list = collection.get(code, [])
    if not collection_list:
        print("Tidak ada Koleksi.")
        return
    else:
        for i, trans in enumerate(collection_list, start=1):
            print(f"{i}. ID Barang: {trans['item_id']}, Item: {trans['item']} - Jumlah: {trans['quantity']}")

# Collection Update
def collection_update(code):
    print("\nUpdate Koleksi:")
    collection_list = collection.get(code, [])
    if not collection_list:
        print("Tidak ada Koleksi untuk diupdate.")
        return

    for i, trans in enumerate(collection_list, start=1):
        print(f"{i}. ID Barang: {trans['item_id']}, Item: {trans['item']} - Jumlah: {trans['quantity']}")

    choice = int(input("Pilih nomor Koleksi yang ingin diupdate: "))
    if 1 <= choice <= len(collection_list):
        new_item = input("Masukkan nama item baru: ")
        new_quantity = int(input("Masukkan jumlah baru: "))
        collection[code][choice - 1] = {'item_id': collection[code][choice - 1]['item_id'], 'item': new_item, 'quantity': new_quantity}
        print("Koleksi berhasil diupdate!")
    else:
        print("Pilihan tidak valid.")

# Collection Delete
def collection_delete(code):
    print("\nDelete Koleksi:")
    collection_list = collection.get(code, [])
    if not collection_list:
        print("Tidak ada Koleksi untuk dihapus.")
        return

    for i, trans in enumerate(collection_list, start=1):
        print(f"{i}. ID Barang: {trans['item_id']}, Item: {trans['item']} - Jumlah: {trans['quantity']}")

    choice = int(input("Pilih nomor Koleksi yang ingin dihapus: "))
    if 1 <= choice <= len(collection_list):
        removed_trans = collection_list.pop(choice - 1)
        print(f"Koleksi {removed_trans['item']} telah dihapus.")
    else:
        print("Pilihan tidak valid.")
        
main()