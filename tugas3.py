keluar = False
while keluar == False:
    check = False
    while check == False:
        menu = input ("Pilihan menu: \n 1) Segitiga siku-siku \n 2) Segitiga sama-kaki \n 3) Persegi \n 4) Exit \n Pilih menu 1/2/3/4:")
        if (menu.isdigit()== True):
            if int(menu)>0 and int(menu)<=4:
                check = True
            else:
                print("Pilihan nomor tidak ada, silahkan masukkan angka 1/2/3/4")
                print("------------------------------------------------------")
        else:
            print("Mohon maaf input salah, silahkan masukkan angka 1/2/3/4")
            print("-------------------------------------------------------")
    if menu == "1":
        check = False
        while(check==False):
            JenisSiku=input("Pilihlah jenis segitiga siku-siku: \n 1. siku bawah \n 2. siku atas \n Masukkan nomor:")
            if (JenisSiku.isdigit()==True):
                if(int(JenisSiku)>0 and int(JenisSiku)<=2):
                    check = True
                else:
                    print("Pilihan nomor tidak ada, silahkan masukkan angka 1/2")
                    print("------------------------------------------------------")
            else:
                print("Input, silahkan masukkan angka 1/2/")
                print("------------------------------------------------------")
        if JenisSiku == "1":
            jumlahrow=int(input("masukkan jumlah baris yang anda inginkan(1-10):"))
            for a in range (0,jumlahrow):
                for b in range (0,a+1):
                    print("*",end="")
                print()
                check = False
            while(check==False):
                ask1 =  input("apakah ingin kembali? \n 1.Ya \n 2.Tidak \n masukkan nomor:")
                if ask1 == "1":
                    check = True
                if ask1 == "2":
                    check= True
                    keluar = True
        elif JenisSiku == "2":
            jumlahrow=int(input("masukkan jumlah baris yang anda inginkan(1-10):"))
            for a in range (0,jumlahrow):
                for b in range (jumlahrow,a,-1):
                    print("*",end="")
                print()
                check = False
            while(check==False):
                ask1 =  input("apakah ingin kembali? \n 1.Ya \n 2.Tidak \n masukkan nomor:")
                if ask1 == "1":
                    check = True
                if ask1 == "2":
                    check= True
                    keluar = True
    if menu == "2":
        check = False
        while(check==False):
            out=""
            n= int(input("masukkan size:"))
            for i in range (0,n+1):
                for j in range (0,n):
                    if j >= n-i and j<=n+i:
                        out+= "* "
                    else:
                        out += " "
                out += "\n"
            print(out)
            check = False
            while(check==False):
                ask1 =  input("apakah ingin kembali? \n 1.Ya \n 2.Tidak \n Masukkan nomor:")
                if ask1 == "1":
                    check = True
                elif ask1 == "2":
                    check = True
                    keluar = True
    if menu =="3":
        check = False
        while(check==False):
            jumlahrow=int(input("masukkan jumlah baris yang anda inginkan(1-10):"))
            for a in range (0,jumlahrow):
                for b in range (0,jumlahrow):
                    print("*",end="")
                print()
            check = False # varibale check yang isinya adalah False
            while(check==False):
                ask1 =  input("apakah ingin kembali? \n 1.Ya \n 2.Tidak \n masukkan nomor:")
                if ask1 == "1":
                    check = True
                if ask1 == "2":
                    check= True
                    keluar = True
    else:  
        keluar = True
print ("terima kasih sudah menggunakan layanan kami")        

