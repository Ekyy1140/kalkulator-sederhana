import os
os.system("cls")

def menu ():
    print ('_____________________________')
    print ('_____pilih opsi operator_____')
    print ('1. tambah                    ')
    print ('2. kurang                    ')
    print ('3. kali                      ')
    print ('4. bagi                      ')
    print ('_____________________________')
menu()   
print(20*"=")
print("KALKULATOR SEDERHANA")
print(20*"=")
angka1 = float(input("Masukan Angka Pertama ="))
operator = input(f"Pilih Operator(+, - ,*, /)=")
angka2 = float(input("Masukan Angka Kedua ="))
if operator == 1:
     hasil = angka1 + angka2
     print(hasil)
elif operator == 2:
    hasil = angka1 - angka2
    print(hasil)
elif operator == 3:
    hasil = angka1 * angka2
    print(hasil)
elif operator == 4:
    hasil = angka1 / angka2
    print(hasil)
elif operator==0:
    exit()
print("opsi tidak ditemukan")




print(26*"=")
print("Terima Kasih Telah Mencoba")
print(26*"=")

