# # APLIKASI BELAJAR DAN BELANJA
Keluar = False
while(Keluar==False):
    # Pemilihan menu include validasi (digit only dengan range 1-3)
    check = False
    while(check==False):
        menu = input('Pilih Menu \n 1.Belanja \n 2.Belajar \n 3.Exit \n Pilih Menu nomor : ')
        if (menu.isdigit()==True):
            if(int(menu)>0 and int(menu)<=3):
                check=True
            else:
                print('input salah, masukan pilihan 1-3')
                print('-----------------------------------')
        else:
            print('input salah, masukan pilihan 1-3')
            print('-----------------------------------')
    # Proses bila menu 1 terpilih
    if (menu=='1'):
        # Pemilihan menu belanja include validasi (digit only dengan range 1-3)
        check = False
        while(check==False):
            menuBelanja = input('Pilih Makanan \n 1.Ayam Rp.20.000 \n 2.Sapi Rp.40.000 \n 3.Salmon Rp.50.000 \n Pilih makanan nomor : ')
            if (menuBelanja.isdigit()==True):
                if(int(menuBelanja)>0 and int(menuBelanja)<=3):
                    check = True
                else:
                    print('input salah, masukan pilihan 1-3')
                    print('-----------------------------------')
            else:
                print('input salah, masukan pilihan 1-3')
                print('-----------------------------------')
        # Pembuatan variabel harga untuk masing-masing pilihan menu belanja
        harga=''
        if(menuBelanja=='1'):
            harga = 20000
        elif(menuBelanja=='2'):
            harga = 40000
        elif(menuBelanja=='3'):
            harga = 50000
        # input kuantitas untuk pembelian menu belanja include validasi (kuantitas digit only dan harus lebih dari 0)
        check = False
        while(check==False):
            kuantitas = input ('Masukan Kuantitas = ')
            if (kuantitas.isdigit()==True):
                if(int(kuantitas)>0):
                    check=True
                else:
                    print('input salah, masukan kuantitas > 0 ')
                    print('-----------------------------------')
            else:
                print('input salah, masukan angka ')
                print('-----------------------------------')
        # perhitungan total harga (harga*kuantitas)
        totalHarga = harga * int(kuantitas)
        print('Pembelian BERHASIL! Total Belanjaan Anda Adalah : ' + 'Rp.' + str(totalHarga))
        print('------------------------------------------------------------------------------')  
        # pertanyaan ingin kembali ke menu awal atau exit include validasi (digit only dengan range 1-2)
        check=False
        while(check==False):
            Ask1 = input('Apakah anda ingin kembali ke \n 1.Menu Awal \n 2.Exit \n Pilih Menu nomor : ')
            if(Ask1.isdigit()==True):
                if(int(int(Ask1)>0 and int(Ask1)<3)):
                    check = True
                else:
                    print('input salah, masukan 1 atau 2 ')
                    print('-----------------------------------')
            else:
                print('input salah, masukan 1 atau 2 ')
                print('-----------------------------------')
            # Pengkondisian agar pilihan Ask1=1 bernilai false dan looping, sedangkan bila pilih Ask1=2 akan bernilai True dan keluar aplikasi
            if(Ask1=='2'):
                Keluar=True
    # Proses bila menu 2 terpilih    
    elif(menu=='2'):
        # Pemilihan menu belajar 2 include validasi (digit only dengan range 1-2)
        check=False
        while(check==False):
            menuBelajar = input ('Pilih Perhitungan Matematika \n 1. Hitung Segitiga \n 2. Hitung Trapesium \n Pilih perhitungan nomor :  ')
            if (menuBelajar.isdigit()==True):
                if(int(menuBelajar)>0 and int(menuBelajar)<=2):
                    check = True
                else:
                    print('input salah, masukan pilihan 1-2')
                    print('-----------------------------------')
            else:
                print('input salah, masukan pilihan 1-2')
                print('-----------------------------------')
        # Pengkondisian bila menu belajar 1 terpilih       
        if(menuBelajar=='1'):
            # input alas segitigas iclude validasi (float data dengan nilai lebih dari 0)
            check = False
            while(check==False):
                alasSegitiga = input ("Masukan alas segitiga = ")
                if (alasSegitiga.isalpha()==False):
                    if(float(alasSegitiga)>0):
                        check=True
                    else:
                        print('input salah, hanya bisa masukan angka lebih dari 0 ')
                        print('----------------------------------------------------')
                else:
                    print('input salah, hanya bisa masukan angka lebih dari 0 ')
                    print('----------------------------------------------------')
            # input tinggi segitiga include validasi (float data dengan nilai lebih dari 0)
            check = False
            while(check==False):
                tinggiSegitiga = input ("Masukan tinggi segitiga = ")
                if (tinggiSegitiga.isalpha()==False):
                    if(float(tinggiSegitiga)>0):
                        check=True
                    else:
                        print('input salah, hanya bisa masukan angka lebih dari 0 ')
                        print('----------------------------------------------------')
                else:
                    print('input salah, hanya bisa masukan angka lebih dari 0 ')
                    print('----------------------------------------------------')
            # Perhitungan luas segitiga
            luasSegitiga = (float(alasSegitiga)*float(tinggiSegitiga))/2
            print('Luas Segitiga = '+str(luasSegitiga) + 'cm2')
            print('-----------------------------------')
            # pertanyaan ingin kembali ke menu awal atau exit include validasi (digit only dengan range 1-2)
            check=False
            while(check==False):
                Ask1 = input('Apakah anda ingin kembali ke \n 1.Menu Awal \n 2.Exit \n Pilih Menu nomor : ')
                if(Ask1.isdigit()==True):
                    if(int(Ask1)>0 and int(Ask1)<3):
                        check=True
                    else:
                        print('input salah, masukan 1 atau 2 ')
                        print('-----------------------------------')
                else:
                    print('input salah, masukan 1 atau 2 ')
                    print('-----------------------------------')
                # Pengkondisian agar pilihan Ask1=1 bernilai false dan looping, sedangkan bila pilih Ask1=2 akan bernilai True dan keluar aplikasi
                if(Ask1=='2'):
                    Keluar=True
        # Pengkondisian bila menu belajar 2 terpilih     
        if(menuBelajar=='2'):
            # input sisi1trapesium include validasi (float data dan lebih besar dari 0)
            check = False
            while (check==False):
                sisi1trapesium = input ('Masukan sisi 1 trapesium = ')
                if (sisi1trapesium.isalpha()==False):
                    if(float(sisi1trapesium)>0):
                        check=True
                    else:
                        print('input salah, masukan hanya angka lebih dari 0')
                        print('---------------------------------------------')
                else:
                    print('input salah, masukan hanya angka lebih dari 0')
                    print('---------------------------------------------')
            # input sisi2trapesium include validasi (float data dan lebih besar dari 0)
            check = False
            while(check==False):
                sisi2trapesium = input ('Masukan sisi 2 trapesium = ')
                if(sisi2trapesium.isalpha()==False):
                    if(float(sisi2trapesium)>0):
                        check=True
                    else:
                        print('input salah, masukan hanya angka lebih dari 0')
                        print('---------------------------------------------')
                else:
                    print('input salah, masukan hanya angka lebih dari 0')
                    print('---------------------------------------------')
            # input tinggiTrapesium include validasi (float data dan lebih besar dari 0)
            check=False
            while(check==False):
                tinggiTrapesium = input ('Masukan tinggi trapesium = ')
                if(tinggiTrapesium.isalpha()==False):
                    if(float(tinggiTrapesium)>0):
                        check=True
                    else:
                        print('input salah, masukan hanya angka lebih dari 0')
                        print('---------------------------------------------')
                else:
                    print('input salah, masukan hanya angka lebih dari 0')
                    print('---------------------------------------------')
            # Perhitungan luas trapesium
            LuasTrapesium = ((float(sisi1trapesium)+float(sisi2trapesium))*float(tinggiTrapesium))*0.5
            print('Luas Trapesium = '+str(LuasTrapesium) + 'cm2')
            print('-----------------------------------')
            # pertanyaan ingin kembali ke menu awal atau exit include validasi (digit only dengan range 1-2)
            check=False
            while(check==False):
                Ask1 = input('Apakah anda ingin kembali \n  1.Menu Awal \n  2.Exit \n Pilih Menu nomor : ')
                if(Ask1.isdigit()==True):
                    if(int(Ask1)>0):
                        check=True
                    else:
                        print('input salah, masukan 1 atau 2')
                        print('-------------------------------')
                else:
                    print('input salah, masukan 1 atau 2')
                    print('-------------------------------')
            # Pengkondisian agar pilihan Ask1=1 bernilai false dan looping, sedangkan bila pilih Ask1=2 akan bernilai True dan keluar aplikasi
            if(Ask1=='2'):
                Keluar=True
    # Pengkondisian agar langsung keluar bila menu 3 terpilih            
    else:
        Keluar=True
# Hasil bila looping berhenti / menu exit dipilih 
print('Terimakasih sudah menggunakan layanan kami!')

