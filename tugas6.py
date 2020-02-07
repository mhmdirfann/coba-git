
dictionary={"item1":"jam","item2":"handphone"}
def printmenu():
    print("key | value")
    print()
    
    for val,key in dictionary.items():
        print(val+" "+key)
def AddDictionary():
    # tipedict=input("masukkan tipe dictionary: \n 1.string \n 2.number")
    a=input("masukkan key:")
    b=input("masukkan val:")
    dictionary[a]=b
    print('dictionary berhasil ditambahkan!')
    print()
def SearchDictionary():
    cari=input("Masukkan kata yang anda cari:")
    pencarian=list(filter(lambda kata:cari.lower() in kata.lower(),dictionary))
    pencarian1=""
    for i in pencarian:
        pencarian1+= i + dictionary[i]
    print(pencarian1)
    print("terimakasih")
    

backtomenu=False
while(backtomenu==False):
    pilihmenu=input("Pilih menu \n1.Menu dictionary \n2.Add Dictionary \n3.Search Dictionary \n4.Exit \n Pilih nomor:")
    index=int(pilihmenu)-1
    menu=[printmenu,AddDictionary,SearchDictionary]
    menu[index]()
    ask_keluar=input("mau ke menu awal atau tidak? (y/n): ")
    if ask_keluar =="n":
        print()
        print("Terimakasih sudah menggunakan aplikasi")
        backtomenu=True
    else:
        backtomenu=False
    


