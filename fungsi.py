import datetime

# Data mobil yang tersedia (Nama: [Harga_Per_Hari, Status])
daftar_mobil = {
    "Toyota Avanza": [350000, "Tersedia"],
    "Honda Brio": [300000, "Tersedia"],
    "Mitsubishi Pajero": [800000, "Tersedia"],
    "Suzuki Ertiga": [400000, "Tersedia"]
}

def tampilkan_mobil():
    print("\n=== Daftar Mobil Tersedia ===")
    print(f"{'No'} {'Model Mobil'} {'Harga/Hari'} {'Status':}")
    print("-" * 50)
    for i, (mobil, info) in enumerate(daftar_mobil.items(), 1):
        print(f"{i:} {mobil:} Rp {info[0]} {info[1]}")

def main():
    print("Selamat Datang di Sistem Rental Mobil")
    
    nama_pelanggan = input("Masukkan Nama Anda: ")
    
    while True:
        tampilkan_mobil()
        pilihan = input("\nPilih nomor mobil (atau ketik 'keluar'): ")
        
        if pilihan.lower() == 'keluar':
            break
            
        try:
            index = int(pilihan) - 1
            nama_mobil = list(daftar_mobil.keys())[index]
            harga_per_hari = daftar_mobil[nama_mobil][0]
            
            if daftar_mobil[nama_mobil][1] == "Disewa":
                print("Maaf, mobil ini sedang tidak tersedia.")
                continue
                
            hari = int(input(f"Berapa hari ingin menyewa {nama_mobil}? "))
            total_biaya = harga_per_hari * hari
            
            # Update Status
            daftar_mobil[nama_mobil][1] = "Disewa"
            
            # Cetak Struk Sederhana
            print("\n" + "="*30)
            print("      STRUK PENYEWAAN")
            print("="*30)
            print(f"Pelanggan : {nama_pelanggan}")
            print(f"Mobil     : {nama_mobil}")
            print(f"Durasi    : {hari} hari")
            print(f"Total     : Rp {total_biaya:,}")
            print("="*30)
            print("Terima kasih telah menyewa!")
            break
            
        except (ValueError, IndexError):
            print("Input tidak valid. Silakan pilih nomor yang tertera.")

if __name__ == "__main__":
    main()