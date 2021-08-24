#Operasi Arhitmatika
# Prioritas Perhitungan Aritmatika

''' 1.()
    2.Eksponen **
    3.Perkalian/Pembagian *,/,%,//
    4.Pertambahan/Pengurangan +,-
'''
from ctypes import c_double

a = 10
b = 8
c = 6
d = 19
# print("=====PENJUMLAHAN======")
# hasil = a + b
# print('Hasil',a,'+',b,'=',hasil)

# print("=====PENGURANGAN======")
# hasil = c - a
# print('Hasil',c,'-',a,'=',hasil)
# print("Type Bilangan Adalah : ",type(hasil))

# print("=====PERKALIAN=======")
# hasil = a * c
# print('Hasil',a,'*',c,'=',hasil)

# print("=====PEMBAGIAN=======")
# hasil = (a / c)
# print('Hasil',a,'/',c,'=',hasil)
# print("Type Bilangan Adalah : ",type(hasil))

# print("=====PANGKAT/EKSPONEN=======")
# print('')
# hasil = b ** c
# print('Hasil',c,'**',b,'=',hasil)
# print('')
# print("===========================")
# print('')
# 
# print("=====MODULUS=======")
# print('')
# hasil = a % c
# print('Hasil',a,'%',c,'=',hasil)
# print('')
# print("===========================")
# print('')

# print("=====FLOOR DIVISION=======")
# print('')
# hasil = b // c
# hasilBagi = b / c
# print('Hasil Bagi',b,'/',c,'=',hasilBagi)
# print('Hasil',b,'//',c,'=',hasil)
# print('')
# print("==========================")
# print('')


print("=====CEK KODE CEK=======")
print(100000006)
hasil_cek_bagian1 = int((a ** b) + c - ( ( ( (d / b) % c)  // d) * a) )
print('Hasil',a,'**',b,'+',c,'-',d,'/',b,'%',c,'//',d,'*',a,'=',hasil_cek_bagian1)
print("Type Bilangan Adalah : ",type(hasil_cek_bagian1))

# print("======CEK BAGIAN 2 ======")
# hasil_cek_bagian2 =int(a ** (b + c) - d / b % c // (d * a))
# print('Hasil',a,'**(',b,'+',c,')-',d,'/',b,'%',c,'//(',d,'*',a,')=',hasil_cek_bagian2)
# print("Type Bilangan Adalah : ",type(hasil_cek_bagian2))

# print("======CEK BAGIAN 3 ======")
# hasil = (a ** b + (d - c)/ b % c // d * a)/14
# print('Hasil (',a,'**',b,'+(',d,'-',c,')/',b,'%',c,'//',d,'*',a,')/14=',hasil)
# print("Type Bilangan Adalah : ",type(hasil))