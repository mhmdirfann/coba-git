
# def menu ():
#     print("menu pilihan")
#     print()
#     print("1.Belajar")
#     print("2.Belanja")
#     print("3.exit")
#     pilih = input("masukkan pilihanmu:")
#     if pilih == "1":
#         belajar()
#     elif pilih == "2":
#         belanja()
# def belanja ():
#     print("Pilih makanan yang ingin dibeli")
#     print("1.Sate Ayam")
#     print("2.Kupat Tahu")
#     pilih = input("masukkan pilihanmu: ")
#     if (pilih =="1"):
#         SateAyam()
#     if (pilih =="2"):
#         KupatTahu()
#     else:
#         print("error")    
# def belajar():
#     print("1.Luas segitiga")
#     print("2.Luas trapesium")
#     pilih = input("Ketikkan nomor pilihanmu: ")
#     if (pilih=="1"):
#         segitiga()
#     elif (pilih =="2"):
#         trapesium()
# def segitiga():
#     a = int(input("1.Masukkan tinggi segitiga"))
#     b = int(input("2.Masukkan alas segitiga"))
#     hasil = a*b/2 
#     print(hasil)
#     pilih = input("kembali ke menu? \n 1.ya \n 2.tidak \n ketikkan nomor:")
#     if pilih == "1":
#         menu()
#     elif pilih == "2":
#         exit
# def trapesium():
#     atas =int(input("masukkan lebar atas trapesium: "))
#     bawah =int(input("masukkan lebar bawah trapesium: "))
#     tinggi = int(input("masukkan tinggi trapesium: "))
#     LuasTrapesium = (atas+bawah)*tinggi/2
#     print(LuasTrapesium)
#     pilih = input("kembali ke menu? \n 1.ya \n 2.tidak \n ketikkan nomor:")
#     if pilih == "1":
#         menu()
#     elif pilih == "2":
#         exit
# def SateAyam ():
#     sate = int(input("berapa tusuk yang mau dibeli?: "))
#     jumlahS = (sate*2000)
#     print("jumlah tagihan anda sebanyak",jumlahS,"Rupiah")
#     pilih = input("kembali ke menu? \n 1.ya \n 2.tidak \n ketikkan nomor:")
#     if pilih == "1":
#         menu()
#     elif pilih == "2":
#         exit
# def KupatTahu ():
#     kupat = int(input("berapa porsi yang ingin anda pesan?: "))
#     jumlahK = (kupat*15000)
#     print("jumlah tagihan anda sebanyak",jumlahK,"Rupiah")
#     pilih = input("kembali ke menu? \n 1.ya \n 2.tidak \n ketikkan nomor:")
#     if pilih == "1":
#         menu()
#     elif pilih == "2":
#         exit
# print ("silahkan memilih: ")
# menu()
# pilih = (input("masukkan pilihan anda:"))
# if pilih == "1":
#     belajar()
# elif pilih =="2":
#     belanja()
# elif pilih =="3":
#     exit    
# pilihan = "a"
# while (pilihan):
#     menu = (input('Pilih menu yng diinginkan: \n \n 1. Belajar \n 2. Belanja \n 3. Exit \n \n Pilih menu nomor: '))
#     if (menu.isdigit()==True):
#         if (int(menu) == 1):
#             belajar= (input ('Pilih perhitungan luas (segitiga/trapesium): '))
#             if belajar == ('segitiga'):
#                 tinggi = (input('Masukkan tinggi (cm): '))
#                 alas = (input('Masukkan alas (cm): '))
#                 luassegitiga= (float(alas)*float(tinggi))/2
#                 print('Luas segitiga adalah: ',luassegitiga, 'cm')
#                 pilihan = (input("Kembali ke menu (y/n)?"))
#                 if pilihan == 'n' or pilihan == 'no' or pilihan == 'tidak':
#                     print ("Good Luck")
#                     break
#             elif belajar == ("trapesium"):
#                 tinggi= (input('Masukkan tinggi (cm): '))
#                 alas1= (input('Masukkan alas1 (cm): '))
#                 alas2= (input('Masukkan alas2 (cm): '))
#                 luastrapesium= ((float(alas1)+float(alas2))*float(tinggi))/2
#                 print('Luas trapesium adalah: ',luastrapesium, 'cm')
#                 pilihan = (input("Kembali ke menu (y/n)?"))
#                 if pilihan == 'n' or pilihan == 'no' or pilihan == 'tidak':
#                     print ("Good Luck")
#                     break
#             else:
#                 print('-----------Input salah------------')
#                 print('----------------------------------') 
#                 pilihan = (input("Kembali ke menu (y/n)?"))
#                 if pilihan == 'n' or pilihan == 'no' or pilihan == 'tidak':
#                     print ("Terima Kasih")
#                     break
#         elif (int (menu) == 2):
#             belanja= int(input('Menu Makanan: \n 1. Ayam Bakar (Rp 20000) \n 2. Ayam Geprek (Rp 30000) \n 3. Ikan Bakar (Rp 40000) \n Menu nomor berapa yg ingin dipesan (1/2/3) ? : '))
#             harga1 = 20000
#             harga2 = 30000
#             harga3 = 40000
#             kuantitas = int(input('Berapa Banyak? '))
#             if belanja == 1:
#                 harga= kuantitas*harga1
#                 print('Harga yg harus dibayarkan adalah sebesar: Rp',harga)
#                 pilihan = (input("Kembali ke menu (y/n)?"))
#                 if pilihan == 'n' or pilihan == 'no' or pilihan == 'tidak':
#                     print ("Terima Kasih")
#                     break
#             elif belanja == 2:
#                 harga = kuantitas*harga2
#                 print('Harga yg harus dibayarkan adalah sebesar: Rp',harga)
#                 pilihan = (input("Kembali ke menu (y/n)?"))
#                 if pilihan == 'n' or pilihan == 'no' or pilihan == 'tidak':
#                     print ("Terima Kasih")
#                     break
#             elif belanja == 3:
#                 harga = kuantitas*harga3
#                 print('Harga yg harus dibayarkan adalah sebesar: Rp',harga)
#                 pilihan = (input("Kembali ke menu (y/n)?"))
#                 if pilihan == 'n' or pilihan == 'no' or pilihan == 'tidak':
#                     print ("Terima Kasih")
#                     break
#             else:
#                 print('     Menu makanan tidak ada       ')
#                 print('----------------------------------') 
#                 pilihan = (input("Kembali ke menu (y/n)?"))
#                 if pilihan == 'n' or pilihan == 'no' or pilihan == 'tidak':
#                     print ("Terima Kasih") 
#                     break  
#         elif (int(menu) == 3):
#             print ('Terima Kasih')
#             break
#         else:
#             print('Input salah, masukan pilihan 1 -3 ')
#             print('----------------------------------')
#             pilihan = (input("Kembali ke menu (y/n)?"))
#             if pilihan == 'n' or pilihan == 'no' or pilihan == 'tidak':
#                 print ("Terima Kasih")
#                 break
#     else:
#         print('Input salah, masukan pilihan 1 -3 ')
#         print('----------------------------------')

# pilihan = "iya" 
# while pilihan:
#     menu = int(input("Ada yang bisa dibantu? \n 1.hitung uang yg dimiliki \n 2.belanja \n 3.exit \n silahkan masukkan nomor:"))
#     if menu == 1:
#         uangi = int(input("Masukkan uang istri:"))
#         uangs = int(input("Masukkan uang suami:"))
#         print (uangi+uangs)
#         pilihan = input("kembali ke awal?: y/n")
#         if pilihan == "n" or pilihan == "tidak" or pilihan == "no":
#             print("terimakasih")
#             break
#         else:
#             print("salah bro")
#             pilihan =int(input("mau ke awal lagi aja ga?:"))
#             if pilihan == "no" or pilihan =="engga ah":
#                 print("yowes")
#                 break

# PiramidDenganAngka
i = 0
out = ""
num = 1
while(i<5):
    j = 0
    while(j<(5-i)):
        out += str(num) + " "
        if (i == 0):
            out+= " "
        num += 2
        j+=1
    i+=1
    out += '\n'
print(out)


keluar = False
while keluar == False:
    check = False
    while check == False:
        menu = input("anda mau ngapain? \n 1.Nonton 2.Bacabuku 3.Exit \n JAWABBB: ")
        if(menu.isdigit()== True):
            if int(menu) >0 and int(menu )<= 3:
                check = True
            else:
                print("NGISINYA ANGKA 1 SAMPE 3")
        else:
            print("NGISI ANGKA DONGGG")
    if menu == "1":
        print("yuk")  
    if menu =="2":
        print("yakali")  
    elif menu =="3":
        print("oke tq")
        keluar = True 
        



