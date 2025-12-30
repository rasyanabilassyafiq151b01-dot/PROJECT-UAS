def pembayaran():
    print("""

===========================
  PILIH METODE PEMBAYARAN
===========================

 DEBIT      |         TUNAI

""")

    bayar = input("PILIH METODE DIATAS:").lower()

while True:
    no_debit = input("Masukkan nomor debit 16 digit: ")

    if len(no_debit) == 16:
        print("Nomor debit diterima")
        break
    else:
        print("Nomor debit tidak valid")
        print("Harus 16 karakter")
        print("Silakan ulangi")
    