import random
from datetime import datetime

# 1. Daftar data_penjualan
data_penjualan = [
    {"id": f"GN{random.randint(100, 999)}", "nama": "Baju Tidur", "harga": 50000, "quantity": 2, "tanggal": "2024-08-05"},
    {"id": f"GN{random.randint(100, 999)}", "nama": "Dress", "harga": 85000, "quantity": 3, "tanggal": "2024-08-05"},
    {"id": f"GN{random.randint(100, 999)}", "nama": "Kaos", "harga": 60000, "quantity": 1, "tanggal": "2024-08-05"},
    {"id": f"GN{random.randint(100, 999)}", "nama": "Jacket", "harga": 120000, "quantity": 4, "tanggal": "2024-08-06"},
    {"id": f"GN{random.randint(100, 999)}", "nama": "Hoodie", "harga": 95000, "quantity": 2, "tanggal": "2024-08-06"},
    {"id": f"GN{random.randint(100, 999)}", "nama": "Sepatu", "harga": 300000, "quantity": 1, "tanggal": "2024-08-06"},
    {"id": f"GN{random.randint(100, 999)}", "nama": "Topi", "harga": 30000, "quantity": 5, "tanggal": "2024-08-07"},
    {"id": f"GN{random.randint(100, 999)}", "nama": "Sandal", "harga": 45000, "quantity": 3, "tanggal": "2024-08-07"},
    {"id": f"GN{random.randint(100, 999)}", "nama": "Celana Pendek", "harga": 70000, "quantity": 2, "tanggal": "2024-08-07"},
    {"id": f"GN{random.randint(100, 999)}", "nama": "Kemeja", "harga": 90000, "quantity": 3, "tanggal": "2024-08-08"},
    {"id": f"GN{random.randint(100, 999)}", "nama": "Rok", "harga": 80000, "quantity": 4, "tanggal": "2024-08-08"},
    {"id": f"GN{random.randint(100, 999)}", "nama": "Tas", "harga": 150000, "quantity": 1, "tanggal": "2024-08-08"},
]

# 2. Fungsi untuk menghitung pendapatan
def hitung_pendapatan(data):
    result = []
    for item in data:
        total_pendapatan = item["harga"] * item["quantity"]
        item_info = {
            "Product ID": item["id"],
            "Nama Produk": item["nama"],
            "Harga": item["harga"],
            "Jumlah": item["quantity"],
            "Tanggal": item["tanggal"],
            "Pendapatan": total_pendapatan
        }
        result.append(item_info)
        print(f"Product ID: {item_info['Product ID']}")
        print(f"Nama Produk: {item_info['Nama Produk']}")
        print(f"Harga: {item_info['Harga']}")
        print(f"Jumlah: {item_info['Jumlah']}")
        print(f"Tanggal: {item_info['Tanggal']}")
        print(f"Pendapatan: {item_info['Pendapatan']}")
        print("-" * 40)  # Separator for better readability
    return result

# 3. Fungsi untuk menghitung rata-rata penjualan
def average_penjualan(data, tanggal):
    total_penjualan = 0
    total_quantity = 0
    found = False
    
    for item in data:
        if item["tanggal"] == tanggal:
            found = True
            total_penjualan += item["harga"] * item["quantity"]
            total_quantity += item["quantity"]

    if not found:
        print("Tidak ada penjualan pada tanggal tersebut.")
        return

    try:
        rata_rata = total_penjualan / total_quantity
        print(f"Rata-rata penjualan pada tanggal {tanggal}: {rata_rata:.2f}")
    except ZeroDivisionError:
        print("Tidak ada penjualan untuk menghitung rata-rata.")

# 4. Fungsi generator untuk total penjualan per tanggal
def total_penjualan(data):
    total_per_tanggal = {}
    
    for item in data:
        if item["tanggal"] not in total_per_tanggal:
            total_per_tanggal[item["tanggal"]] = 0
        total_per_tanggal[item["tanggal"]] += item["harga"] * item["quantity"]

    for tanggal, total in total_per_tanggal.items():
        yield f"Tanggal: {tanggal}, Total Penjualan: {total}"

# Memanggil fungsi
print("Hitung Pendapatan:")
hitung_pendapatan(data_penjualan)

print("\nMasukkan tanggal yang ingin dicari (YYYY-MM-DD): ", end="")
input_tanggal = input()
average_penjualan(data_penjualan, input_tanggal)

print("\nTotal Penjualan per Tanggal:")
for hasil in total_penjualan(data_penjualan):
    print(hasil)
