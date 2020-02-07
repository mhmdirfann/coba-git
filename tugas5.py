buah = [["Jeruk",1000],["Apel",3000],["Semangka",3000]]
keluar = False
def menu():
    while keluar == False:
        check = False
        while check == False:
            menu=input("Menu \n 1) Show Produk \n 2) Update Produk \n 3) Update Harga \n 4) Hapus Produk \n Silahkan pilih nomor:")
            if (menu.isdigit()==True):
                if int(menu)>0 and int(menu)<=4:
                    check=True
                else:
                    print("Pilihan nomor tidak ada, silahkan masukkan angka 1/2/3/4")
                    print("------------------------------------------------------")
            else:
                print("Input salah, silahkan masukkan angka 1/2/3/4")
                print("------------------------------------------------------")
        if menu == "1":
            ShowProduk()
        elif menu =="2":
            UpdateProduk()
        elif menu =="3":
            UpdateHarga()
        elif menu =="4":
            HapusProduk()
        else:
            print("inputan salah,masukkan angka 1/2/3/4")
def ShowProduk():
    hitung = 1
    for item in buah:
        print(str(hitung) + "."+ str(item[0])+" "+"Rp."+str(item[1]))
        hitung+=1
    kembali = input("Kembali ke menu awal?(y/n)\n")
    if kembali == "y":
        menu()
    elif kembali =="n":
        print("Terimakasih telah menggunakan layanan kami")
    else:
        print(kembali)
def UpdateProduk():
    produkbaru = input("Nama produk yang akan ditambahkan:")
    harga=input("harga produknya:")
    masukkan=[produkbaru,harga]
    buah.append(masukkan)
def UpdateHarga():
    update=input("masukkan item yang akan diupdate:")
    itemditemukan=False
    while itemditemukan==False:
        for i in range(len(buah)):
            if buah[i][0].lower()==update.lower():
                itemditemukan=True
                break
        if itemditemukan==False:
            update=input("Input gagal \n masukkan item:")
    hargaupdate=input("masukkan harga yang terbaru:")
    while(True):
        if hargaupdate.isdigit():
            break
        else:
            input("input salah \n masukkan harga:")
    buah[i][1]=int(hargaupdate)
    print("data berhasil diupdate")
def HapusProduk():
    hapus=input("hapus produk:")
    itemditemukan=False
    delbuah=0
    while itemditemukan==False:
        for i in range(len(buah)):
            if buah[i][0].lower()==hapus.lower():
                itemditemukan=True
                delbuah=i
                break
        else:
            hapus=input("Input gagal \n masukkan item:")
    del buah[delbuah]
    print("data berhasil dihapus")
menu()
    



