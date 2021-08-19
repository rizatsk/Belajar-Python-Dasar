#Membuat rumus rumus yang pernah ada 
#1 Rumus Konversi Suhu

print('\nRumus Rumus Konversi Suhu')
print('Suhu Celcius,Reamur,Fahrenhit,Kelvin\n')

#Perubahan suhu Celcius
print( 35*"=")
print('Perubahan Suhu Celcius ke Reamur')
inputcelcius = float(input('Masukan derajat Celcius : '))
rumus_Celcius = (4/5) *inputcelcius
print('Hasil Dari Celcius ke Reamur adalah :',rumus_Celcius,'R')
print("\n",35*"=")
print('Perubahan Suhu Celcius ke Fahrenhit')
inputcelcius = float(input('Masukan derajat Celcius : '))
rumus_Celcius = (9/5) *inputcelcius + 32
print('Hasil Dari Celcius ke Fahrenhit adalah :',rumus_Celcius,'F')
print("\n",35*"=")
print('Perubahan Suhu Celcius ke Kelvin')
inputcelcius = float(input('Masukan derajat Celcius : '))
rumus_Celcius = inputcelcius + 273
print('Hasil Dari Celcius ke Kelvin adalah :',rumus_Celcius,'K')

#Perubahan suhu Reamur
print("\n",35*"=")
print('Perubahan Suhu Reamur ke Celcius')
inputreamur = float(input('Masukan derajat Reamur : '))
rumus_reamur = (5/4) *inputreamur
print('Hasil Dari Reamur ke Celcius adalah :',rumus_reamur,'C')
print("\n",35*"=")
print('Perubahan Suhu Reamur ke Fahrenhit')
inputreamur = float(input('Masukan derajat Reamur : '))
rumus_reamur = (9/4) *inputreamur + 32
print('Hasil Dari Reamur ke Fahrenhit adalah :',rumus_reamur,'F')
print("\n",35*"=")
print('Perubahan Suhu Reamur ke Kelvin')
inputreamur = float(input('Masukan derajat Reamur : '))
rumus_reamur = (5/4) *inputreamur + 273
print('Hasil Dari Reamur ke Kelvin adalah :',rumus_reamur,'K')

#Perubahan suhu Fahrenhit
print("\n",35*"=")
print('Perubahan Suhu Fahrenhit ke Celcius')
inputFahrenhit = float(input('Masukan derajat Fahrenhit : '))
rumus_fahrenhit = (5/9) *(inputFahrenhit - 32)
print('Hasil Dari Fahrenhit ke Celcius adalah :',rumus_fahrenhit,'C')
print("\n",35*"=")
print('Perubahan Suhu Fahrenhit ke Reamur')
inputFahrenhit = float(input('Masukan derajat Fahrenhit : '))
rumus_fahrenhit = (4/9) *(inputFahrenhit - 32)
print('Hasil Dari Fahrenhit ke Reamur adalah :',rumus_fahrenhit,'R')
print("\n",35*"=")
print('Perubahan Suhu Fahrenhit ke Kelvin')
inputFahrenhit = float(input('Masukan derajat Fahrenhit : '))
rumus_fahrenhit = (inputFahrenhit + 459.67)*5/9
print('Hasil Dari Fahrenhit ke Kelvin adalah :',rumus_fahrenhit,'K')
print("\n",35*"=")

#Perubahan suhu Kelvin
print('Perubahan Suhu Kelvin ke Celcius')
inputKelvin = float(input('Masukan derajat Kelvin : '))
rumus_Kelvin = inputKelvin - 273
print('Hasil Dari Kelvin ke Celcius adalah :',rumus_Kelvin,'C')
print("\n",35*"=")
print('Perubahan Suhu Kelvin ke Reamur')
inputKelvin = float(input('Masukan derajat Kelvin : '))
rumus_Kelvin = 4/5*(inputKelvin - 273)
print('Hasil Dari Kelvin ke Reamur adalah :',rumus_Kelvin,'R')
print("\n",35*"=")
print('Perubahan Suhu Kelvin ke Fahrenhit')
inputKelvin = float(input('Masukan derajat Kelvin : '))
rumus_Kelvin = (1.8*(inputKelvin - 273))+32
print('Hasil Dari Kelvin ke Fahrenhit adalah :',rumus_Kelvin,'F')
