mobil = [
    {"kode": "M001", "nama": "Avanza", "harga": 350000, "tersedia": True},
    {"kode": "M002", "nama": "Xenia", "harga": 330000, "tersedia": True},
    {"kode": "M003", "nama": "Innova", "harga": 450000, "tersedia": True},
    {"kode": "M004", "nama": "Fortuner", "harga": 650000, "tersedia": True}
]
   

def tampilan():
    print("""
  ===========================
      DAFTAR MOBIL BAROKAH 
  ===========================
""")
    for kode in mobil:
       m = print(kode, mobil[kode]["nama"], mobil[kode]["harga"])
       for i in range(m):
            print(f"Mobil" + mobil[kode]["nama"], "Harga" + mobli[kode][harga])


