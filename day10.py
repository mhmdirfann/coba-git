# def ceknama(nama,alphabet):
#     if(alphabet.lower() in name or alphabet.upper() in name):
#         print("True")
#     else:
#         print("False")
    

# def add_even(num):
#     if num%2==0:
#         print(f"angka {num} adalah angka genap!")
#     else:
#         print(f"angka{num} adalah angka ganjil!")

# add_even(90)

# def filter(text):
#     string="".join(i for i in text if i.isdigit())
#     print(filter)

import datetime
def cekplat(platnomor):
    for i in platnomor:
        if(i.isdigit()):
            digit=int(i)
    hari= date.today().day
    if digit%2==0:
        digit_akhir="Genap"
    else:
        digit_akhir="Ganjil"
    if hari%2==0:
        hari_tersebut="Genap"
    else:
        hari_tersebut="Ganjil"
    if digit_akhir== hari_tersebut:
        print(f"hari ini tanggal {hari} PLat nomor ini {platnomor} diperbolehkan")
    else:
        print(f"hari ini tanggal {hari} PLat nomor ini {platnomor} tidak diperbolehkan")
