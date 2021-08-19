#Operasi logika atau Boolean
print(' Operasi logika Boolean NOT,OR,AND, XOR')

print('===== NOT =====')
a = True
hasil = not a
print('Logikanya adalah a =',a)
print('Lalu dirubah menjadi False Menggunakan not(variable)')
print('Hasil dari not yaitu merubah dari True menjadi =',hasil)
a = False
hasil = not a
print('Logikanya adalah a =',a)
print('Lalu dirubah menjadi True Menggunakan not(variable)')
print('Hasil dari not yaitu merubah dari False menjadi =',hasil)

print('===== OR =====')
#OR ITU ADALAH UNTUK MEMBANDINGKAN KEDUA NILAI JIKA FALSE DAN TRUE AKAN MENJADI TRUE
#KECUALI FALSE DAN FALSE AKAN MENJADI FALSE
a = False
b = False
hasil = a or b
print('Hasil dari',a, 'or',b,'=',hasil)
a = False
b = True
hasil = a or  b
print('Hasil dari',a, 'or',b,'=',hasil)
a = True
b = False
hasil = a or b
print('Hasil dari',a, 'or',b,'=',hasil)
a = True
b = True
hasil = a or b
print('Hasil dari',a, 'or',b,'=',hasil)

print('====== AND =======')
#AND ITU ADALAH UNTUK MEMBANDINGKAN KEDUA NILAI JIKA FALSE DAN TRUE AKAN MENJADI FALSE
#KECUALI TRUE DAN TRUE AKAN MENJADI TRUE
a = True
b = False
hasil = a and b
print('Hasil dari',a, 'and',b,'=',hasil)
a = False
b = True
hasil = a and b
print('Hasil dari',a, 'and',b,'=',hasil)
a = False
b = False
hasil = a and b
print('Hasil dari',a, 'and',b,'=',hasil)
a = True
b = True
hasil = a and b
print('Hasil dari',a, 'and',b,'=',hasil)

print('====== XOR =======')
#XOR ITU ADALAH UNTUK MEMBANDINGKAN KEDUA NILAI JIKA FALSE DAN TRUE AKAN MENJADI TRUE
#KECUALI TRUE DAN TRUE AKAN MENJADI FALSE
# FALSE DAN FALSE MENJADI FALSE
a = True
b = False
hasil = a ^ b
print('Hasil dari',a, 'XOR',b,'=',hasil)
a = False
b = True
hasil = a ^ b
print('Hasil dari',a, 'XOR',b,'=',hasil)
a = False
b = False
hasil = a ^ b
print('Hasil dari',a, 'XOR',b,'=',hasil)
a = True
b = True
hasil = a ^ b
print('Hasil dari',a, 'XOR',b,'=',hasil)
