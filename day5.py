# cekout = False
# while cekout == False:
#     cek = False
#     while cek == False:
#         menu = input("pilihan menu \n 1.segitiga siku-siku \n 2.segitiga sama kaki \n 3.persegi\n pilih nomor:")
#         if(menu.isalpha()) == True or (menu.isdecimal())==False:
#             print("input harus berupa angka")
#         else :
#             if (0<int(menu)<4):
#                 cek = True
#             else:
#                 print("masukkan angka 1 sampai 3")
#     if(menu=="1"):
#         print("segitiga siku-siku")
#     elif (menu=="2"):
#         print("segitiga sama kaki")
#     elif (menu=="3"):
#         print("persegi")
#     cekout = input("mau ke menu awal? \n y/n:")

for i in range(3):
    for j in range(3):
        print(i,end=' ')
    print() 