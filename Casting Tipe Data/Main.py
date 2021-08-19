# Belajar Casting
# Merubah data dari satu data ke data lainya

print("=====INTEGER======")
tipe_data_integer = 10;
print("Data :",tipe_data_integer,", tipe data",type(tipe_data_integer))

tipe_data_float = float(tipe_data_integer)
tipe_data_str = str(tipe_data_integer)
tipe_data_bool = bool(tipe_data_integer)#akan false jika isi integernya angka 0
print("Data :",tipe_data_float,", tipe data",type(tipe_data_float))
print("Data :",tipe_data_str,", tipe data",type(tipe_data_str))
print("Data :",tipe_data_bool,", tipe data",type(tipe_data_bool))

print("=====FLOAT======")
tipe_data_float = 10.9;
print("Data :",tipe_data_float,", tipe data",type(tipe_data_float))

tipe_data_integer = int(tipe_data_float)
tipe_data_str = str(tipe_data_float)
tipe_data_bool = bool(tipe_data_float)#akan false jika isi floatnya angak 0
print("Data :",tipe_data_integer,", tipe data",type(tipe_data_integer))
print("Data :",tipe_data_str,", tipe data",type(tipe_data_str))
print("Data :",tipe_data_bool,", tipe data",type(tipe_data_bool))

print("=====STRING======")
tipe_data_str = "10";
print("Data :",tipe_data_str,", tipe data",type(tipe_data_str))

tipe_data_integer = int(tipe_data_str)
tipe_data_float = float(tipe_data_str)
tipe_data_bool = bool(tipe_data_str)#akan false jika tipe data stringnya kosong, 0 value
print("Data :",tipe_data_integer,", tipe data",type(tipe_data_integer))
print("Data :",tipe_data_float,", tipe data",type(tipe_data_float))
print("Data :",tipe_data_bool,", tipe data",type(tipe_data_bool))

print("=====BOOL======")
tipe_data_bool = True;
print("Data :",tipe_data_bool,", tipe data",type(tipe_data_bool))

tipe_data_integer = int(tipe_data_bool)
tipe_data_float = float(tipe_data_bool)
tipe_data_str = str(tipe_data_bool)
print("Data :",tipe_data_integer,", tipe data",type(tipe_data_integer))
print("Data :",tipe_data_float,", tipe data",type(tipe_data_float))
print("Data :",tipe_data_str,", tipe data",type(tipe_data_str))
