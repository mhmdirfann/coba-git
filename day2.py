# # import math
# # angka1 = 5
# # angka2 = 10

# # print(math.ceil(angka2/angka1))
# # print(math.pow(angka1,angka2))

# nama = 'irfan'
# # print(nama.index('r'))
# print(len(nama))
# import math

# a = 5
# b = 6

# temp = a
# a = b
# b = temp
# print(a)
# print(b)
# # ini teh ceritanya dibolak balik
# a,b = b,a

# nama = "i'm muhammad irfan"
# print(nama[:5])
# print(nama[6:])

# x=4
# y=3
# z=2
# w=((x+y*z/x*y)**z)
# print(w)

# angka = int(input("masukkan angkaa: "))
# print(f"kuadrat dari" + str(angka)+'='+str (angka**2))
angka1 = int(input("masukkan angka 1:"))
angka2 = int(input("masukkan angka 2:"))
text = input("mau melakukan apa?:")
if text == '*':
    print(angka1*angka2)
elif text == '+':
    print(angka1+angka2)
elif text == '-':
    print(angka1-angka2)
elif text == '/':
    print(angka1/angka2)
else:
    print("input salah")
