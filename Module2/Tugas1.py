# Data storage
users = {}  # {code: (code, password)}
profiles = {}  # {code: {'nama': name, 'email': email, 'role': role}}
collection = {}  # {code: [{'item_id': id, 'item': 'keyboard', 'quantity': 1}]}

# Pure function to validate email
def is_valid_email(email):
    return "@" in email and "." in email.split("@")[-1]

# Pure function to create a profile
def create_profile(name, role, email):
    return {'nama': name, 'role': role, 'email': email}

# Pure function to register a user
def register(code, password, name, role, email):
    if code in users:
        return "Code sudah terdaftar."
    
    if not is_valid_email(email):
        return "Email tidak valid."
    
    users[code] = (code, password)
    profiles[code] = create_profile(name, role, email)
    collection[code] = []
    return "Pendaftaran Berhasil!"

# Pure function for login
def login(code, password):
    if code in users and users[code][1] == password:
        return f"Selamat datang {profiles[code]['nama']}!"
    return "Code atau password salah."

# Pure function to view user profiles
def view_profiles():
    return profiles

# Pure function to add collection
def add_collection(code, item, quantity):
    item_id = len(collection[code]) + 1
    collection[code].append({'item_id': item_id, 'item': item, 'quantity': quantity})
    return f"Item '{item}' berhasil ditambahkan ke koleksi!"

# Pure function to list collection
def list_collection(code):
    return collection.get(code, [])

# Pure function to update collection
def update_collection(code, item_id, new_item, new_quantity):
    for item in collection[code]:
        if item['item_id'] == item_id:
            item['item'] = new_item
            item['quantity'] = new_quantity
            return f"Koleksi '{new_item}' berhasil diperbarui!"
    return "Item tidak ditemukan."

# Pure function to delete from collection
def delete_collection(code, item_id):
    for item in collection[code]:
        if item['item_id'] == item_id:
            collection[code].remove(item)
            return f"Koleksi '{item['item']}' berhasil dihapus!"
    return "Item tidak ditemukan."

# Declarative function to display the menu
def display_menu(options, title="Menu"):
    print(f"\n{title}:")
    for key, value in options.items():
        print(f"{key}. {value}")
    return input("Pilih: ")

# Function for admin to manage collectors
def manage_collectors():
    while True:
        choice = display_menu({
            "1": "View Collectors",
            "2": "Update Collector",
            "3": "Delete Collector",
            "4": "Exit"
        }, "Admin Menu")

        if choice == "1":
            for code, profile in view_profiles().items():
                print(f"Code: {code}, Nama: {profile['nama']}, Role: {profile['role']}")

        elif choice == "2":
            code = input("Masukkan Code Collector yang ingin diupdate: ")
            if code in users:
                new_password = input("Masukkan Password Baru: ")
                new_name = input("Masukkan Nama Baru: ")
                new_email = input("Masukkan Email Baru: ")
                users[code] = (code, new_password)
                profiles[code]['nama'] = new_name
                profiles[code]['email'] = new_email
                print("Collector berhasil diupdate!")
            else:
                print("Code tidak ditemukan.")

        elif choice == "3":
            code = input("Masukkan Code Collector yang ingin dihapus: ")
            if code in users:
                del users[code]
                del profiles[code]
                del collection[code]
                print("Collector berhasil dihapus!")
            else:
                print("Code tidak ditemukan.")

        elif choice == "4":
            break

        else:
            print("Pilihan tidak valid.")

# Function for collectors
def collector_menu(code):
    while True:
        choice = display_menu({
            "1": "Add to Collection",
            "2": "View Collection",
            "3": "Update Collection",
            "4": "Delete from Collection",
            "5": "Logout"
        }, "Collector Menu")

        if choice == "1":
            item = input("Masukkan nama item: ")
            quantity = int(input("Masukkan jumlah: "))
            result = add_collection(code, item, quantity)
            print(result)

        elif choice == "2":
            collections = list_collection(code)
            if not collections:
                print("Koleksi kosong.")
            else:
                for item in collections:
                    print(f"ID: {item['item_id']}, Item: {item['item']} - Jumlah: {item['quantity']}")

        elif choice == "3":
            item_id = int(input("Masukkan ID item yang ingin diupdate: "))
            new_item = input("Masukkan nama item baru: ")
            new_quantity = int(input("Masukkan jumlah baru: "))
            result = update_collection(code, item_id, new_item, new_quantity)
            print(result)

        elif choice == "4":
            item_id = int(input("Masukkan ID item yang ingin dihapus: "))
            result = delete_collection(code, item_id)
            print(result)

        elif choice == "5":
            print("Logged out.")
            break

        else:
            print("Pilihan tidak valid.")

# Main function
def main():
    while True:
        choice = display_menu({
            "1": "Register",
            "2": "Login",
            "3": "Exit"
        }, "Main Menu")

        if choice == "1":
            code = input("Masukkan Code: ")
            password = input("Masukkan Password: ")
            name = input("Masukkan Nama: ")
            role = input("Pilih role (admin/collector): ").strip().lower()
            email = input("Masukkan Email: ")
            result = register(code, password, name, role, email)
            print(result)

        elif choice == "2":
            code = input("Masukkan Code: ")
            password = input("Masukkan Password: ")
            result = login(code, password)
            print(result)
            if "Selamat datang" in result:
                if profiles[code]['role'] == 'admin':
                    manage_collectors()
                else:
                    collector_menu(code)

        elif choice == "3":
            print("Keluar...")
            break

        else:
            print("Pilihan tidak valid.")

# Run the program
main()
