nama = input("Masukkan nama Anda : ")
tgl = input("Masukkan tanggal lahir anda (dd/month/yyyy) : ")
status = input("Status (pelajar/pekerja/mahasiswa) : ")
kota = input("Masukkan kota tempat tinggal : ")

print("===== B i o d a t a =====")
print("Nama \t\t\t: {}".format(nama))
pemisah = tgl.split("/")
print("Tanggal lahir \t: {} {} {}".format(pemisah[0], pemisah[1], pemisah[2]))
print("Status \t\t\t: {}".format(status))
print("Tempat tinggal \t: {}".format(kota))