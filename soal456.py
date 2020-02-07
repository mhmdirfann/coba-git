print("masukan hari: ")
harisoal= int (input())
tahun = harisoal // 360
sisa_bagi_tahun = harisoal % 360
bulan = sisa_bagi_tahun//30
sisa_bagi_bulan= sisa_bagi_tahun % 30
minggu = sisa_bagi_bulan//7
sisa_bagi_minggu= sisa_bagi_bulan%7
hari = sisa_bagi_minggu 
print(harisoal,'hari adalah:',tahun,'tahun',bulan,'bulan',minggu,'minggu',sisa_bagi_minggu,'hari',"\n Terimakasih sudah menggunakan aplikasi")
# harisoal = int(input("masukkan hari :"))
# tahun=harisoal // 360
# sisatahun=harisoal % 360
# bulan=sisatahun // 30
# sisabulan = sisatahun%30
# ##soal 5
# word = input('kata: ')
# cari = input('karakter yg ingin dicari: ')
# print(len(word.split(cari))-1)

# word = "halo dunia"
# cari = 'o'

# print(len(word.split(cari))-1))
# import math
# jarakdalamkm = int(input("berapa jarak antar kendaraan?: "))
# kecepatanAkmperH = int(input("kecepatan kendaraan a?: "))
# kecepatanBkmperH = int(input('kecepatan kendaraan b?'))
# jamberangkat = int(input("jamberangkat?: "))

# waktu_tabrakan_dalam_menit = (jarakdalamkm/(kecepatanAkmperH+kecepatanBkmperH))*60 
# print(str(waktu_tabrakan_dalam_menit)+ 'menit')
# jam=math.floor(waktu_tabrakan_dalam_menit/60)+ jamberangkat

# print(f'waktu A & B bertabrakan adalah jam',jam)
