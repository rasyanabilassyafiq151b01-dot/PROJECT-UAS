print("    Selamat Datang di Aplikasi Rental Mobil")
print("=========================================")
from Pembeli import main as pembeli_main
pembeli_main()
from pembayaran import pembayaran as pembayaran_metode
pembayaran_metode()
print("=========================================")
print("    Terima Kasih Telah Menggunakan Layanan Kami")