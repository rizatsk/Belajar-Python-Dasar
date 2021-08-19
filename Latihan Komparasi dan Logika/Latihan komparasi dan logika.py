#Latihan komparasi dan logika
print('Kurang dari 3 dan lebih dari 10')
inputuser=float(input('Masukan angka kurang dari 3 dan lebih dari 10 :'))
kurang_dari = inputuser <3
lebih_dari = inputuser >10
print('Hasil yang anda masukan kurang dari 3 adalah',kurang_dari)
print('Hasil yang anda masukan lebih dari 10 adalah',lebih_dari)
print('Hasil logika dari OR adalah',kurang_dari or lebih_dari)
print('Hasil logika dari AND adalah',kurang_dari and lebih_dari)
print("\n",25*"=")
inputuser=float(input('Masukan angka lebih dari 3 dan kurang dari 10 :'))
kurang_dari = inputuser >3
lebih_dari = inputuser <10
print('Hasil yang anda masukan lebih dari 3 adalah',kurang_dari)
print('Hasil yang anda masukan kurang dari 10 adalah',lebih_dari)
print('Hasil logika dari OR adalah',kurang_dari or lebih_dari)
print('Hasil logika dari AND adalah',kurang_dari and lebih_dari)
print("\n",25*"=")
inputuser=float(input('Masukan angka lebih dari 3 dan lebih dari 10 :'))
kurang_dari = inputuser >3
lebih_dari = inputuser >10
print('Hasil yang anda masukan lebih dari 3 adalah',kurang_dari)
print('Hasil yang anda masukan lebih dari 10 adalah',lebih_dari)
print('Hasil logika dari OR adalah',kurang_dari or lebih_dari)
print('Hasil logika dari AND adalah',kurang_dari and lebih_dari)
print('Hasil logika dari XOR adalah',kurang_dari ^ lebih_dari)

print("/n",25*"=")
inputuser=float(input('Masukan angka lebih dari 0,kurang dari 5,lebih dari 8,dan kurang dari 11  : '))
lebih_dari0 = inputuser >0
kurang_dari5 = inputuser <5
lebih_dari8 = inputuser >8
kurang_dari11 = inputuser <11
print('Hasil yang anda masukan lebih dari 0 adalah',lebih_dari0)
print('Hasil yang anda masukan kurang dari 5 adalah',kurang_dari5)
print('Hasil yang anda masukan lebih dari 8 adalah',lebih_dari8)
print('Hasil yang anda masukan kurang dari 11 adalah',kurang_dari11)
print('Hasil logika dari OR adalah',lebih_dari0 or kurang_dari5 or lebih_dari8 or kurang_dari11)


