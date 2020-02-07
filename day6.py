# kapital huruf awal
# def kata(string):
#     word = ''
#     for char in range(0,len(string)):
#          word+= "-"
#          for j in range(0,char+1):
#              if j == 0:
#               word += string[char].upper()
#              else:
#               word += string[char].lower()
#     print(word)

# kata("maju")

# def urut(parameter):
#     for item1 in range(0,len(parameter)-1):
#         for item2 in range (item1+1,len(parameter)):
#             if parameter[item1]>parameter[item2]:
#                 parameter[item1],parameter[item2]=parameter[item2],parameter[item1]
#     print(parameter)

# urut([40,100,1,5,25,10])
# def urut (parameter):
#     for item1 in range (0,len(parameter)-1):
#         for item2 in range (item1+1,len(parameter)):
#             if parameter[item1]<parameter[item2]:
#                 parameter[item1],parameter[item2]=parameter[item2],parameter[item1]
#     print(parameter)
# urut([40,100,1,5,25,10])
# jumlah=int(input("masukkan jumlah:"))

# z=""
# for item1 in range (0,jumlah):
#     for item2 in range (jumlah,item1,-1):
#         z+="* "
#     z+="\n"
# print(z)
# out = ""
# n= int(input("masukkan size:"))
# for i in range (0,n+1):
#     for j in range (0,n):
#         if j >= n-i and j<=n+i:
#             out+= "* "
#         else:
#             out += " "
#     out += "\n"
# print(out)

#function
# blocks of code (kumpulan beberapa kode)
# named (apapun) dan reused (bisa digunakan kapanpun)
# def blender(buah):
#     print("jus "+buah)
# blender("jeruk")
# def bayarparkir(masuk,keluar):
#     totaljam=abs(keluar-masuk)
#     biaya=totaljam*3000
#     print(biaya)
# # bayarparkir(7,10)

# def hilang():
#     kata=input("masukkan kata:")
#     hilang=input("masukkan karakter yg ingin dihilangkan:")
#     ilang=kata.replace(hilang,"")
#     print(ilang)


# def hilang(kata,hilang):
#     lowert=kata.lower()
#     rmv=lowert.replace(hilang,"")
#     print(rmv)

# hilang("buahbatu","b")
#versi biasa
# def mainsuit(player1,player2):
#     if player1== "gunting" and player2=="batu":
#         print("player1 menang")
#     elif player1== "gunting" and player2=="kertas":
#         print("player2 menang")
#     elif player1== "gunting" and player2=="gunting":
#         print("seri")
#     elif player1== "batu" and player2=="batu":
#         print("seri")
#     elif player1== "batu" and player2=="kertas":
#         print("player2 menang")
#     elif player1== "batu" and player2=="gunting":
#         print("player1 menang")
#     elif player1== "kertas" and player2=="batu":
#         print("player1 menang")
#     elif player1== "kertas" and player2=="gunting":
#         print("player2 menang")
#     elif player1== "kertas" and player2=="kertas":
#         print("seri")
#     else:
#         print("kode salah")

# mainsuit("batu","batu")

#Default parameter
# def perkalian(angka1=5,angka2=3):
#     return angka1*angka2
# print(perkalian(7,7))

#def return
# def perkalian2(x):
#     if x<3:
#         return 4
#     else:
#         return (x*tujuh())

# def tujuh():
#     return 7

# print (perkalian2(2))


# def hapusvowel(nama):
#     vowels=["a","i","u","e","o","A","I","U","E","O"]
#     for a in vowels:
#         nama=nama.replace(a,"")
#     print(nama)
# hapusvowel("muhammad irfan")

# List
# container isiniya values holding berapapun values
# buah_buah = ["jeruk","apel","semangka"]
# buah_buah.insert(2,"koran")
# for i in buah_buah:
#     print
# buah = ['Jeruk Rp.1000', 'Nanas', 'Apel']
# for item in buah : print(item)

# def nama (nama,huruf):
#     if huruf == "A":
#         nama=True
#         print("benar")
#     else:
#         nama=False
#         print("salah")

# nama("Muhammad Irfan","V")
#true or false
# def check_nama(name,alphabet):
#     print(alphabet.lower() in name or alphabet.upper() in name)

# check_nama("Muhammad Irfan","B")
buah = ["apel","ayam","kelapa"]
baru=["nila",'jagung']
buah.append(baru)
print (buah)