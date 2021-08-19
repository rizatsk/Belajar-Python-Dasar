# Belajar Operasi Komparasi
''' Ada : 
    1. < (Kurang Dari) 
    2. > (Lebih Dari)
    3.<= (Kurang Dari Sama Dengan)
    4.>= (Lebih dari sama dengan)
    5.== (Sama Dengan a = 4)
    6.!= (Tidak Sama Dengan)
    7.is (Sama Nilainya dengan menggunakan a = b)
    8.is not (Tidak sama nilainya dengan menggunakan a = b)
'''
a = 5 
b = 7
c = 10
#Koparasi menggunakan kurang dari <
print('===== < =====')
hasiltreu = a < c
print('Hasil dari',a,'<',c,'=',hasiltreu)

hasilfalse = c < a
print('Hasil dari',c,'<',a,'=',hasilfalse)

#Koparasi menggunakan kurang dari >
print('===== > =====')
hasilfalse = a > b
print('Hasil dari',a,'<',b,'=',hasilfalse)

hasiltrue = c > a
print('Hasil dari',c,'<',a,'=',hasiltrue)

#Koparasi menggunakan kurang dari <=
print('===== <= =====')
hasil = a <= b
print('Hasil dari',c,'<=',b,'=',hasil)

hasil = c <= a
print('Hasil dari',c,'<=',a,'=',hasil)

#Koparasi menggunakan kurang dari >=
print('===== >= =====')
hasil = c >= b
print('Hasil dari',c,'>=',b,'=',hasil)

hasil = a >= c
print('Hasil dari',a,'>=',c,'=',hasil)

#Koparasi menggunakan kurang dari ==
print('===== == =====')
hasil = c == c
print('Hasil dari',c,'==',c,'=',hasil)

hasil = a == b
print('Hasil dari',a,'==',c,'=',hasil)

#Koparasi menggunakan kurang dari !=
print('===== != =====')
hasil = c != b
print('Hasil dari',c,'!=',b,'=',hasil)

hasil = a != a
print('Hasil dari',a,'!=',a,'=',hasil)

#Koparasi menggunakan kurang dari is
print('===== is =====')
hasil = c is b
print('Hasil dari',c,'is',b,'=',hasil)

hasil = a is a
print('Hasil dari',a,'is',a,'=',hasil)

#Koparasi menggunakan kurang dari is not
print('===== is not =====')
hasil = c is not a
print('Hasil dari',c,'is not',b,'=',hasil)

hasil = a is not a
print('Hasil dari',a,'is not',a,'=',hasil)

