
def menu ():
    print("menu pilihan")
    print()
    print("1.Belajar")
    print("2.Belanja")
    print("3.exit")
def belanja ():
    print("Pilih makanan yang ingin dibeli")
    print("1.Sate Ayam")
    print("2.Kupat Tahu")
    pilih = input("masukkan pilihanmu: ")
    if (pilih =="1"):
        SateAyam()
    if (pilih =="2"):
        KupatTahu()
    else:
        print("error")    
def belajar():
    print("1.Luas segitiga")
    print("2.Luas trapesium")
    pilih = input("Ketikkan nomor pilihanmu: ")
    if (pilih=="1"):
        segitiga()
    elif (pilih =="2"):
        trapesium()
def segitiga():
    a = int(input("1.Masukkan tinggi segitiga"))
    b = int(input("2.Masukkan alas segitiga"))
    hasil = a*b/2 
    print(hasil)
    pilih = input("kembali ke menu? \n 1.ya \n 2.tidak \n ketikkan nomor:")
    if pilih == "1":
        menu()
        pilih = input ("masukkan pilihan anda: ")
        if pilih =="1":
            belajar()
        elif pilih =="2":
            belanja()
        elif pilih == "3":
            exit
    elif pilih == "2":
        exit
def trapesium():
    atas =int(input("masukkan lebar atas trapesium: "))
    bawah =int(input("masukkan lebar bawah trapesium: "))
    tinggi = int(input("masukkan tinggi trapesium: "))
    LuasTrapesium = (atas+bawah)*tinggi/2
    print(LuasTrapesium)
    pilih = input("kembali ke menu? \n 1.ya \n 2.tidak \n ketikkan nomor:")
    if pilih == "1":
        menu()
        pilih = input ("masukkan pilihan anda: ")
        if pilih =="1":
            belajar()
        elif pilih =="2":
            belanja()
        elif pilih == "3":
            exit
    elif pilih == "2":
        exit
def SateAyam ():
    sate = int(input("berapa tusuk yang mau dibeli?: "))
    jumlahS = (sate*2000)
    print("jumlah tagihan anda sebanyak",jumlahS,"Rupiah")
    pilih = input("kembali ke menu? \n 1.ya \n 2.tidak \n ketikkan nomor:")
    if pilih == "1":
        menu()
        pilih = input ("masukkan pilihan anda: ")
        if pilih =="1":
            belajar()
        elif pilih =="2":
            belanja()
        elif pilih == "3":
            exit
    elif pilih == "2":
        exit
def KupatTahu ():
    kupat = int(input("berapa porsi yang ingin anda pesan?: "))
    jumlahK = (kupat*15000)
    print("jumlah tagihan anda sebanyak",jumlahK,"Rupiah")
    pilih = input("kembali ke menu? \n 1.ya \n 2.tidak \n ketikkan nomor:")
    if pilih == "1":
        menu()
        pilih = input ("masukkan pilihan anda: ")
        if pilih =="1":
            belajar()
        elif pilih =="2":
            belanja()
        elif pilih == "3":
            exit
    elif pilih == "2":
        exit
print ("silahkan memilih: ")
menu()
pilih = (input("masukkan pilihan anda:"))
if pilih == "1":
    belajar()
elif pilih =="2":
    belanja()
elif pilih =="3":
    exit    


