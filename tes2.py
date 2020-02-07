# UsiaAndi_dan_UsiaBudi = 49
# rasioAndiBudi = 0.4
# y=2

# UsiaAndi = UsiaAndi_dan_UsiaBudi * rasioAndiBudi/((1+rasioAndiBudi))
# UsiaBudi = UsiaAndi_dan_UsiaBudi - UsiaAndi

# print('usia andi adalah:',UsiaAndi,'dan usia budi adalah:',UsiaBudi)

# text = input("masukkan kata: ")
# print(text.split("a"))
# x = 'Halo Dunia';
# print(len(x)); print(x.split('D'))
# s="This is New York"
# # split first
# a=s.split()
# # reverse list
# a.reverse()
# # now join them
# result = " ".join(a)
# # print it
# print(result)
# s = "-"
# seq = ("a", "b", "c"); # This is sequence of strings.
# print(s.join(seq))

# logical operatos
# x = 5; y = '5'; z = 6;
# print(x==int(y) and int(y)<z); 
# print(x==int(y) or int(y)>z);
# print(not(x==int(y) or int(y)<z));
# #PembedaGanjilGenap
# import math
# angka = int(input("masukkan angka:"))
# if angka % 2 == 0:
#   (print(f"angka",angka,"adalah angka genap"))
# else:
#     (print(f"angka",angka,"adalah angka ganjil"))

# nilai = int(input("masukkan nilai anda:"))
# if (nilai>= 70 and nilai <80):
#     print("B")
# elif (nilai>=60 and nilai <70):
#     print("C")
# elif (nilai>=80):
#     print("A")
# import math
# TinggiBadan = int(input("masukkan tinggi badan:"))
# BeratBadan = int(input("masukkan berat badan:"))
# IMT = BeratBadan/((TinggiBadan/100)**2)
# if IMT < (18.5):
#     print("berat badan kurang")
# elif IMT   >= 18.5 and IMT <=24.9:
#     print("berat badan ideal")
# elif IMT  >= 25 and IMT <= 29.9:
#     print("berat badan berlebih")
# elif IMT  >= 30 and IMT <= 39.9:
#     print("berat badan sangat berlebih")
# elif IMT > 39.9:
#     print("obesitas")

# angka = 1
# while(angka <=10):
#     angka+= 1
#     print(angka)
#jangan lupa dikasih exit condition

# Listitem = list(range(1,13,2))
# print(Listitem)
# tes=""
# for tes in range(1,11):
#     tes +="a"
#     print(tes)
# for nomor in range(0,22,2):
#     print("Nomor urut",nomor)
# for a in range (5):
#     for b in range(5):
#         print(a)
# for a in range(3):
#     for b in range(3):
#      print(a)
# rumus bintang part1
# z=7
# for a in range (0,6,1):
#     print(" * "*z)
#     z-=1
# z=1
# for a in range (0,7,1):
#     print(" * "*z)
#     z+=1

# out= ''
# for i in range (5,0,-1):
#     if (i>1):
# rumus bintang 2 part 2
# z=""
# for a in range (4,-5,-1):
#     print(abs(a)*" * " + " A ")

# for a in range (0,5):
#     for b in range (5,a,-1):
#         z+='* '
#     z+='\n'
# for a in range (1,5):
#     for b in range (0,a+1):
#         z+='* '
#     z+='\n'
# print(z)

# ContohPiramida1
# j = 2
# for i in range (1,6,2):
#     print("   "*j+i*" * ")
#     j-=1
# contoh piramida 2 masukkan ankgka sendiri 1
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
# contoh piramida 2 masukkan angka sendiri 2
# size = input("size?:")
# for i in range(int(size)):
#     for j in range ((int(size)-i)-1):
#         print(end="")
#     for j in range (i+1):
#         print("*",end=" ")
#     print()
# contoh ketupat
# out = ""
# for i in range (0,11):
#     if i<10:
#         for j in range (0,21):
#             if j >= 10-i and j<= 10+i:
#                 out+= " * "
#             else:
#                 out += "   "
#         out += "\n"
#     else:
#         for i in range (10,-1,-1):
#             for j in range (0,21):
#                 if j >= 10-i and j<= 10+i:
#                     out+= " * "
#                 else:
#                     out += "   "
#             out += "\n"
# print(out)

# for a in (range(11)):
#     print('nomor urut'+str(a))

# z = ''
# for item in list(range(5)):
#     z+='*'
#     print(z)

# for i in list(range(5))
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
            # pertanyaan ingin kembali ke menu awal atau exit include validasi (digit only dengan range 1-2)
          
    # Pengkondisian agar langsung keluar bila menu 3 terpilih            
    else:
        Keluar=True
# Hasil bila looping berhenti / menu exit dipilih 
print('Terimakasih sudah menggunakan layanan kami!')

