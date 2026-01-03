def pembayaran(total):
    print("\nMETODE PEMBAYARAN")
    print("1. Cash")
    print("2. Transfer")
    print("3. E-Wallet")
    print("4. Batal")

    pilih = input("Pilih (1-4): ")

    if pilih == "1":
        cash = int(input("Masukan Jumlah Uang Anda:"))
        kembalian = cash - total
        if cash < total:
            print("Maaf Uang Tidak Cukup")
        elif cash > total:
            print("Kembalian Dari Sewa Mobil Anda:", kembalian)
        else:
            print ("Pembayaran Selesai")
        return True 
    else:
        print("Pembayaran Rp", total, "berhasil")
        return True
