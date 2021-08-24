# var1 = "'Hello World'"
# var2 = '"Say Hai"'
# print(var1,var2)

# var1 = """
# 'Saya Rizat Sakmir'
# "Mahasiswa UBSI"
# "Program Studi Teknologi Informasi"
# """
# var2 = '''
# Saya Rizat Sakmir
# Mahasiswa UBSI
# Program Studi Teknologi Informasi
# '''
# print(var1)
# print(var2)

# var1 = """
# Bambang Adalah
# Anaknya Tukiyem
# Pas Masih Kecil
# """
# var2 = var1 * 10
# print(var2)

# String adalah Array
var = "Bambang"
print(var[0])
print(var[3])

# Slicing
print(var[0:3])
print(var[2:5])
print(var[2:])
print(var[:5])

# Negativ Slicing
print(var[-2])
print(var[-7:-2]) #Posisi ke 5 dari akhir ke posisi ke 2 dari akhir.

#cek String
var = "Hallo Saya Rizat Mahasiswa BSI"
result = "Rizat" in var
print(result)

result = "Rizat" not in var
print(result)

# length
print(len(var))

# Method dan Operator Format
txt = "Bambang adalah anak anjing no %d di hati %s" % (1,'kita')
print(txt)

hewan = 'anjing'
no = 1
var = 'kita'
txt = "Bambang adalah anak {} no {} di hati {}"
print(txt.format(hewan,no,var))

harga = 90000
satuan = 9
itemNo = 301
txt = "Saya bayar dengan Harga Rp{0}, untuk item nomor {1}, sebanyak {2} item" #{0} mengambil dari format dari index 0
print(txt.format(harga,itemNo,satuan))

txt = "Dasar Anak Haram"
result = "Haram" in txt
if result == True:
    txt = "****"
    print(txt)
else :
    print(txt)

