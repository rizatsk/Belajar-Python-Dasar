#Operator Bitwase yaitu artinya bitwase itu masing masing bit

a = 9
b = 2

print('============OR============')
c = a | b
print('Nilai',a,'Binary =',format(a,'08b'))
print('Nilai',b,'Binary =',format(b,'08b'))
print('-----------------------------------OR')
print('Hasil',a,'|',b,'   =',format(c,'08b'))

print('============AND============')
c = a & b
print('Nilai',a,'Binary =',format(a,'08b'))
print('Nilai',b,'Binary =',format(b,'08b'))
print('-----------------------------------AND')
print('Hasil',a,'&',b,'   =',format(c,'08b'))

print('===========XOR=============')
c = a ^ b
print('Nilai',a,'Binary =',format(a,'08b'))
print('Nilai',b,'Binary =',format(b,'08b'))
print('-----------------------------------XOR')
print('Hasil',a,'^',b,'   =',format(c,'08b'))

print('===========NOT=============')
c = ~a 
print('Nilai',a,'Binary =',format(a,'08b'))
print('-----------------------------------NOT')
print('Nilai',c,'Binary =',format(c,'08b'))
c = ~b 
print('Nilai',b,'Binary =',format(b,'08b'))
print('-----------------------------------NOT')
print('Nilai',c,'Binary =',format(c,'08b'))

print('===========SHIFTRIGHT=============')
c = a >> 1 
print('Nilai',a,'Binary =',format(a,'08b'))
print('----------------------------------->>')
print('Nilai',c,'Binary =',format(c,'08b'))

print('===========SHIFLEFT=============')
c = b << 3 
print('Nilai',b,'Binary =',format(b,'08b'))
print('-----------------------------------<<')
print('Nilai',c,'Binary =',format(c,'08b'))
