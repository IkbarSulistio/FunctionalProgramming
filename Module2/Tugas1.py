# Dictionary for storing user data
users = {}  # {code: (code, password)}
profiles = {}  # {code: {'nama': name, 'email': email, 'role': role}}
collection = {}  # {code: [{'item_id': id, 'item': 'keyboard', 'quantity': 1}]}

# Email validation function
def is_valid_email(email):
    # Check if there's exactly one '@' and it has at least one character before and after it
    if email.count('@') != 1:
        return False
    local_part, domain_part = email.split('@')
    if not local_part or not domain_part:
        return False
    
    # Check if domain part has at least one '.' and contains characters before and after '.'
    if '.' not in domain_part or domain_part.startswith('.') or domain_part.endswith('.'):
        return False
    
    return True

# Define main menu as pure functions and mappings
def main_menu():
    menu_actions = {
        "1": register,
        "2": login,
        "3": exit_program
    }
    while True:
        print("\nMain Menu:\n1. Register\n2. Login\n3. Exit")
        action = menu_actions.get(input("Masukkan pilihan: "), invalid_choice)
        action()

def exit_program():
    print("Keluar..."); exit()

def invalid_choice():
    print("Pilihan tidak valid, coba lagi.")

# Register new user
def register():
    code = input("Masukkan Code: ")
    if code in users:
        print("Code sudah terdaftar."); return
    password = input("Masukkan Password: ")
    role = input("Pilih role (admin/collector): ").strip().lower()
    if role not in ['admin', 'collector']:
        print("Role tidak valid. Pilih antara 'admin' atau 'collector'."); return
    users[code] = (code, password)
    profiles[code] = input_profile(code, role)
    collection[code] = input_collection(code)
    print("Pendaftaran Berhasil!")

def input_profile(code, role):
    skip = input("Apakah anda ingin melengkapi profile sekarang? (y/n): ")
    if skip.lower() != 'y':
        return {'nama': '', 'role': role, 'email': ''}
    while True:
        name = input("Masukkan nama: ")
        email = input("Masukkan email: ")
        if is_valid_email(email):
            return {'nama': name, 'role': role, 'email': email}
        else:
            print("Email tidak valid. Mohon masukkan email yang benar.")

def input_collection(code):
    skip = input("Apakah anda ingin menambahkan Collection? (y/n): ")
    if skip.lower() != 'y':
        return []
    items = []
    while True:
        item = input("Masukkan nama item: ")
        quantity = int(input("Masukkan jumlah: "))
        items.append({'item_id': len(items) + 1, 'item': item, 'quantity': quantity})
        if input("Apakah anda ingin menambahkan item lain? (y/n): ").lower() == 'n':
            break
    return items

# Login function
def login():
    code, password = input("Masukkan Code: "), input("Masukkan Password: ")
    if code in users and users[code][1] == password:
        print(f"Selamat datang {profiles[code]['nama']}!")
        user_menu(code)
    else:
        print("Code atau password salah.")

# User Menu with role-based access
def user_menu(code):
    role = profiles[code]['role']
    menu_actions = {
        "1": lambda: view_profile(code),
        "2": lambda: collection_menu(code),
        "3": lambda: list_users() if role == 'admin' else invalid_choice,
        "4": lambda: crud_collectors() if role == 'admin' else print("Hanya admin yang bisa melakukan ini."),
        "5": lambda: print("Logged out.")
    }

    while True:
        print("\nUser Menu:")
        print("1. Profile\n2. Collection")
        if role == 'admin':
            print("3. List Users\n4. Manage Collectors")
        print("5. Logout")
        
        action = menu_actions.get(input("Pilih: "), invalid_choice)
        action()
        if action == menu_actions["5"]:
            break

# Profile and collection management functions
def view_profile(code):
    profile = profiles.get(code, {})
    print(f"\nProfile:\nNama: {profile.get('nama', 'N/A')}\nEmail: {profile.get('email', 'N/A')}\nRole: {profile.get('role', 'N/A')}")

# Admin Function: List All Users and Their Collections
def list_users():
    print("\nDaftar Pengguna dan Koleksi:")
    for user_code, (user_code, _) in users.items():
        profile = profiles[user_code]
        print(f"\nCode: {user_code}, Nama: {profile['nama']}, Role: {profile['role']}")
        list_collection(user_code)

# Manage collectors for admin
def crud_collectors():
    while True:
        print("\nManage Collectors:")
        print("1. Tambah Collector")
        print("2. List Collectors")
        print("3. Update Collector")
        print("4. Delete Collector")
        print("5. Kembali")
        
        action = input("Pilih: ")
        if action == "1":
            add_collector()
        elif action == "2":
            list_collectors()
        elif action == "3":
            update_collector()
        elif action == "4":
            delete_collector()
        elif action == "5":
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

# Function to add a new collector
def add_collector():
    code = input("Masukkan Code Collector: ")
    if code in users:
        print("Collector sudah terdaftar."); return
    password = input("Masukkan Password: ")
    users[code] = (code, password)
    profiles[code] = input_profile(code, 'collector')
    collection[code] = []
    print("Collector berhasil ditambahkan!")

# Function to list all collectors
def list_collectors():
    print("\nDaftar Collectors:")
    for user_code, (user_code, _) in users.items():
        if profiles[user_code]['role'] == 'collector':
            profile = profiles[user_code]
            print(f"Code: {user_code}, Nama: {profile['nama']}, Email: {profile['email']}")

# Function to update a collector's information
def update_collector():
    code = input("Masukkan Code Collector yang ingin diupdate: ")
    if code not in users:
        print("Collector tidak ditemukan."); return
    print("Masukkan data baru:")
    new_password = input("Masukkan Password baru: ")
    profiles[code] = input_profile(code, profiles[code]['role'])
    users[code] = (code, new_password)
    print("Collector berhasil diupdate!")

# Function to delete a collector
def delete_collector():
    code = input("Masukkan Code Collector yang ingin dihapus: ")
    if code in users:
        del users[code]
        del profiles[code]
        del collection[code]
        print("Collector berhasil dihapus!")
    else:
        print("Collector tidak ditemukan.")

# Collection menu with role-based access
def collection_menu(code):
    role = profiles[code]['role']
    menu_actions = {
        "1": lambda: add_collection(code),
        "2": lambda: list_collection(code),
        "3": lambda: update_collection(code),
        "4": lambda: delete_collection(code),
        "5": lambda: print("Returning to main menu...")
    }

    while True:
        print("\nCollection Menu:")
        if role == 'collector':
            print("1. Tambah Koleksi\n2. Lihat Koleksi\n3. Update Koleksi\n4. Hapus Koleksi\n5. Exit")
        else:
            print("2. Lihat Koleksi\n5. Exit")
        action_key = input("Pilih: ")
        action = menu_actions.get(action_key, invalid_choice)
        
        if role == 'admin' and action_key in ['1', '3', '4']:
            print("Admin hanya bisa melihat koleksi, tidak bisa menambah atau mengedit.")
            continue
        
        action()
        if action == menu_actions["5"]:
            break

# Collection functions for collectors
def add_collection(code):
    item = input("Masukkan nama item: ")
    quantity = int(input("Masukkan jumlah: "))
    collection[code].append({'item_id': len(collection[code]) + 1, 'item': item, 'quantity': quantity})
    print("Item berhasil ditambahkan ke koleksi!")

def list_collection(code):
    items = collection.get(code, [])
    if not items:
        print("Tidak ada Koleksi.")
        return
    for item in items:
        print(f"ID: {item['item_id']}, Item: {item['item']}, Jumlah: {item['quantity']}")

def update_collection(code):
    items = collection.get(code, [])
    for i, item in enumerate(items, start=1):
        print(f"{i}. ID: {item['item_id']}, Item: {item['item']}, Jumlah: {item['quantity']}")
    idx = int(input("Pilih nomor item untuk diupdate: ")) - 1
    if 0 <= idx < len(items):
        items[idx].update(item=input("Item baru: "), quantity=int(input("Jumlah baru: ")))
        print("Koleksi diperbarui!")
    else:
        print("Pilihan tidak valid.")

def delete_collection(code):
    items = collection.get(code, [])
    for i, item in enumerate(items, start=1):
        print(f"{i}. ID: {item['item_id']}, Item: {item['item']}, Jumlah: {item['quantity']}")
    idx = int(input("Pilih nomor item untuk dihapus: ")) - 1
    if 0 <= idx < len(items):
        removed = items.pop(idx)
        print(f"Item {removed['item']} dihapus dari koleksi.")
    else:
        print("Pilihan tidak valid.")

# Start the program
main_menu()
