# Soal 1
data1 =input("masukkan empat digit angka:")
print((data1[2:4])+(data1[0:2]))

# Soal 2
import math
r= int(input("masukkan jari-jari:"))
lingkaran = ((math.pi)*r**2)
print(round(lingkaran))

# Soal 3
data1 =input("masukkan dua digit angkaA:")
data2 = input("masukkan dua digit angkaB:")
print(data1[0]+data2[0]+data1[1]+data2[1])

# Soal 4
Kata = input("masukkan kata:")
Karakter = input("masukkan karakter/huruf yang ingin dihilangkan: ")
print(Kata.replace(Karakter,' '))

#Soal 5
kata = input("masukkan dua kata:")
katadipisah = kata.split(" ")
katadipisah.reverse()
hasil =" ".join(katadipisah)
print(hasil)