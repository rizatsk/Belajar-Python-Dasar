# a = 10 , a adalah variable dengan nilai 10
# tipe data : angka satuan (interger)
data_interger = 9
print("data :",data_interger, ", bertipe :",type(data_interger))

data_float = 0.2
print("data :",data_float, ", bertipe :",type(data_float))

data_string = "oncom"
print("data :",data_string, ", bertipe :",type(data_string))

data_bool = True
print("data :",data_bool, ",bertipe :",type(data_bool))

data_complex = 8j
print("data :",data_complex, ",bertipe :",type(data_complex),",Complex :",complex(data_interger))

data_list = [1,2,3,4,5]
print("data :",data_list, ",bertipe :",type(data_list))

data_tuple = ((1,2,3,4,5))
print("data :",data_tuple, ",bertipe :",type(data_tuple))

data_dictionary = ({"Nama" : "Bambang","Umur" : "42 tahun"})
print("data :",data_dictionary, ",bertipe :",type(data_dictionary))

data_dictionary = [
    {"Nama" : "Bambang","Umur" : "42 tahun"},
    {"Nama" : "Oncom","umur" : "21 Tahun"}
    ]
print("data :",data_dictionary, ",bertipe :",type(data_dictionary))

#tipe data dari bahasa c

from ctypes import c_double, c_char

data_c_double = c_double(10.9)
print("data :",data_c_double, ",bertipe :",type(data_c_double))

