print("\n",25*"=")
inputuser=int(input('Masukan angka lebih dari 0,kurang dari 5,lebih dari 8,dan kurang dari 11  : '))
lebih_dari0 = inputuser >0
kurang_dari5 = inputuser <5
lebih_dari8 = inputuser >8
kurang_dari11 = inputuser <11
print('Hasil yang anda masukan',inputuser, 'lebih dari 0 adalah',lebih_dari0)
print('Hasil yang anda masukan',inputuser, 'kurang dari 5 adalah',kurang_dari5)
print('Hasil yang anda masukan',inputuser, 'lebih dari 8 adalah',lebih_dari8)
print('Hasil yang anda masukan',inputuser, 'kurang dari 11 adalah',kurang_dari11)
print('Hasil logika dari OR adalah',lebih_dari0 or kurang_dari5 or lebih_dari8 or kurang_dari11)
print('Hasil logika dari AND adalah',lebih_dari0 and kurang_dari5 and lebih_dari8 and kurang_dari11)
print('Hasil logika dari XOR adalah',lebih_dari0 ^ kurang_dari5 ^ lebih_dari8 ^ kurang_dari11)

print("\n",25*"=")
inputuser=int(input('Masukan angka Kurang dari 0,Lebih dari 5,Kurang dari 8,dan Lebih dari 11  : '))
kurang_dari0 = inputuser <0
lebih_dari5 = inputuser >5
kurang_dari8 = inputuser <8
lebih_dari11 = inputuser >11
print('Hasil yang anda masukan',inputuser, 'Kurang dari 0 adalah',kurang_dari0)
print('Hasil yang anda masukan',inputuser, 'Lebih dari 5 adalah',lebih_dari5)
print('Hasil yang anda masukan',inputuser, 'Kurang dari 8 adalah',kurang_dari8)
print('Hasil yang anda masukan',inputuser, 'Lebih dari 11 adalah',lebih_dari11)
print('Hasil logika dari OR adalah',kurang_dari0 or lebih_dari5 or kurang_dari8 or lebih_dari11)
print('Hasil logika dari AND adalah',kurang_dari0 and lebih_dari5 and kurang_dari8 and lebih_dari11)
print('Hasil logika dari XOR adalah',kurang_dari0 ^ lebih_dari5 ^ kurang_dari8 ^ lebih_dari11)

print("\n",25*"=")
inputuser=int(input('Masukan angka lebih dari 0,kurang dari 5,lebih dari 8,dan kurang dari 11  : '))
lebih_dari0 = inputuser <0
kurang_dari5 = inputuser >5
lebih_dari8 = inputuser >8
kurang_dari11 = inputuser <11
print('Hasil yang anda masukan',inputuser, 'lebih dari 0 adalah',lebih_dari0)
print('Hasil yang anda masukan',inputuser, 'kurang dari 5 adalah',kurang_dari5)
print('Hasil yang anda masukan',inputuser, 'lebih dari 8 adalah',lebih_dari8)
print('Hasil yang anda masukan',inputuser, 'kurang dari 11 adalah',kurang_dari11)
print('Hasil logika dari OR adalah',lebih_dari0 or kurang_dari5 or lebih_dari8 or kurang_dari11)
print('Hasil logika dari AND adalah',lebih_dari0 and kurang_dari5 and lebih_dari8 and kurang_dari11)
print('Hasil logika dari XOR adalah',lebih_dari0 ^ kurang_dari5 ^ lebih_dari8 ^ kurang_dari11)
print("\n",30*"=")
print('OR yaitu dia akan True jika salah satu logika hasilnya True\ndan dia akan menjadi False jika semua logikanya itu False ')
print('AND yaitu dia akan True Jika semua logika hasilnya itu True\ndan dia akan menjadi False jika salah satu logika itu hasilnya False')
print('XOR yaitu True Ketemu False = True\nTrue Ketemu True = False\nFalse ketemu False = False')