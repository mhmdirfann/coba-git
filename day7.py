# Tugas6
# PilihanMenu
# Show produk
# Add produk
# Ubah harga
# Delete harga

# produk=["Jeruk","Semangka","Mangga"]
# harga = [1000,3000,2500]

# def printmenu():
#     hasil=""
#     for item in range(len(produk)):
#         hasil+=str(item+1)+"."+produk[item]+" "+"Rp."+str(harga[item])+"\n"
#     return (hasil)
# (printmenu())
# def showproduk():
#     (printmenu())
# def inputdata():
#         newprod=input("masukkan data:")
#         newprice=int(input("masukkan harga dari {} :".format(newprod)))
#         produk.append(newprod)
#         harga.append(newprice)
#         print("produk berhasil ditambahkan!\n")
#         printmenu()

# def updateharga():
#     pilihprod=input("pilih produk yang ingin ditambahkan\n"+printmenu()+"\npilih salah satu")
#     pilih=int(pilihprod)
#     newharga=("Harga"+[pilih]+"akan dirubah berapa harganya:?")
#     harga[pilih]=newharga
#     print("harga produk berhasil berubah\n"+printmenu())


# def deletedata():
#     pilihprod=input("pilih produk yang ingin ditambahkan\n"+printmenu()+"\npilih salah satu")
#     index=int(pilihprod)-1
#     produk.pop(index)
#     harga.pop(index)
#     print("produk berhasil dihapus!\n"+printmenu())
# backtomenu=False
# while(backtomenu==False):
#     pilihmenu=input("Pilih menu \n1.Show Produk \n2.Add Produk \n3.Update Harga \n4.Delete Produk \n Pilih nomor:")
#     index=int(pilihmenu)-1
#     menu=[showproduk,inputdata,updateharga,deletedata]
#     menu[index]()
#     ask_keluar=input("mau ke menu awal atau tidak? (y/n): ")
#     if ask_keluar =="n":
#         print()
#         print("Terimakasih sudah menggunakan aplikasi")
#         backtomenu=True
#     else:
#         backtomenu=False

# def hello():
#     print("hello")
# def function():
#     return [1,2,hello]
    
# Important from list
# Cara ambil dari sebuah list,cara mengganti list,setelah diganti lalu diambil

# produk = [["jeruk",2000],["Apel",3000],["Manggis",5000]]
# cart = [[0,3],[1,2],[2,3]]
# out=""
# for item in range(len(cart)):
#     index = cart[item][0]
#     out+= str(item+1)+"."+str(produk[index][0])+"x"+str(cart[item][1])+"= Rp. " +str(produk[index][1]*cart[index][1]) + "\n"
# print(out)

#Dictionary
# nama={
#     "depan":"Anugerah"
#     "belakang":"Nurhamid"
# }
# nama["depan"]="uga"
# print(nama["depan"])

# variable_tuple=(1,2,3,4,5,6,9,8)

# print(type(variable_tuple))
# list comprehension
# listNum = [ 1, 2, 3, 4, 5]; listNum = [item * 2 for item in listNum]; print(listNum)
# def perkalian(num):
#     return num*2

# listnum = [1,2,3,4,5,6]
# listnum = [perkalian(item) for item in listnum]
# print (listnum)
# def times2(num) : 
#     return num * 2
# x=lambda num: num * 2
# print(x(5))

# def function(n):
#     return lambda a : a*n

# dikali2=function(2)

# print(dikali2[11])
# def fizzBuzz(num) :
#      for i in range(1,num+1) :
#         if (i % 15 == 0) :
#             print('FizzBuzz')
#         elif (i % 3 == 0) : 
#             print('Fizz')
#         elif (i % 5 == 0) :
#              print('Buzz')
#         else :
#             print(i)
# fizzBuzz(20)
# def fibo(urut) : 
#     listData = [1,1]
#     for i in range(2,urut): 
#         listData.append(listData[i-2] + listData[i-1])
#     return listData[urut-1]
# print(fibo(8))