kalimat = "UNIVERSITAS NUSA PUTRA SUKABUMI"

#soal a
pengecil = kalimat.lower()
print(pengecil[-14:-9], pengecil[12:16])

#soal b
pembesar = kalimat.upper()
print(pembesar[1:12] + pembesar[12] + pembesar[14:17] + pembesar[17] + pembesar[19:23] + pembesar[23] + pembesar[25:27] + pembesar[27] + pembesar[29:])

#soal c
pemisah = kalimat.split()
print("{} {} {} {}".format(pemisah[3], pemisah[2], pemisah [1], pemisah[0]))

#soal d 
print(pembesar[0] + pembesar[12] + pembesar[17] + pembesar[23])

#soal e
print(pembesar[8:12] + pembesar[14:16] + pembesar[17:19] + " " + pembesar[-4:])