# # #Pilih menu
# # #1.Show Dictionary
# # #2. Add Dictionary
# # #3. Search Dictionary
# # #4. Exit

# # firstdictionary = {}

# # def menudictionary(input):
# #     print("|    Key     |    Value   |")
# #     hasil = ""
# #     i=0
# #     for key,value in input.items():
# #         i+=1
# #         hasil+= f"({i}. {key}               {value} )\n"
# #     return hasil

# # def showDictionary ():
# #     print(menudictionary(firstdictionary))

# # def addDictionary():
# #     inputloop=input("berapa kali akan memasukkan dictionary? \n >>")
# #     for i in range(int(inputloop)):
# #         print ("Pilih tipe dictionary: \n1. String \n2. Number")
# #         pilihdictionary=input('pilih: ')
# #         if pilihdictionary =="1":
# #             key = input("Key:")
# #             val= input("Value:")
# #             firstdictionary[key]=val
# #         elif pilihdictionary=="2":
# #             keyA =input("Key:")
# #             valB =input("Value:")
# #             firstdictionary[keyA]=int(valB)
# #         print()
# # def searchDictionary():
# #     search=input("cari kata:")
# #     filterdict=filter(lambda item : search.lower() in item.lower(),firstdictionary.keys())
# #     newdict={}
# #     for item in filterdict:
# #         newdict[item]=firstdictionary[item]
# #     print(menudictionary(newdict))
# # def outt():
# #     print("terimakasih telah menggunakan layanan kami")
# #     exit()
# # backtomenu=False
# # while(backtomenu==False):
# #     pilihmenu=input("Pilih menu \n1.Menu dictionary \n2.Add Dictionary \n3.Search Dictionary \n4.Exit \n Pilih nomor:")
# #     index=int(pilihmenu)-1
# #     menu=[showDictionary,addDictionary,searchDictionary,outt]
# #     menu[index]()
# #     ask_keluar=input("mau ke menu awal atau tidak? (y/n): ")
# #     if ask_keluar =="n":
# #         print()
# #         print("Terimakasih sudah menggunakan aplikasi")
# #         backtomenu=True
# #     else:
# #         backtomenu=False
# #contoh baca print diction
# # diction= {"nama":"budi","umur":20}

# # for i in diction:
# #     print(diction.values())

# import math 
# def bubblesort(list):
#     for i in range(len(list)-1,0,-1):
#         for j in range(i):
#             if list[j]> list[j+1]:
#                 list[j],list[j+1]=list[j+1],list[j]
#     return list

# def mean_list(list):
#     return sum(list/len(list))
# def median_list(list):
#     list = bubblesort(list)
#     if len(list) %2==0:
#         return (list([len(list))//2-1])
#     else:
#         return list[floor(len(list)/2)]

# def mode_list(list):
#     ind = set(list)
#     counter={}
#     modus=[]
#     for i in ind:
#         z=0
#         for j in list:
#             if i ==j:
#                 z+=1
#         counter[i]=z
#     max_count=max(counter.values())
#     for k in counter:
#         if counter[k]==max_count:
#             return modus
# def variance_list(list):
#     z=0
#     mean=mean_list(list)
#     for i in list:
#         z+= pow((i-mean),2)
#         return (z/(len(list)-1))
# def stdev(list):
#     z=0
#     mean=mean_list(list)
#     for i in list:
#         z+= pow((i-mean),2)
#         return sqrt(z/(len(list)-1))
# def sample_statistic(list,type):
#     if type == "mean":
#         return mean_list(list)
#     if type == "median":
#         return median_list(list)
#     if type == "stdev":
#         return stdev(list)
#     if type == "mode":
#         return mode_list(list)
#     if type == "variance":
#         return variance_list(list)
#     else:
#         return "INPUT TIDAK SESUAI"

# from math import pow
# def getsquare(num):
#     num1=str(num)
#     out=""
#     for i in list(num1):
#         out+= str(int(pow(int(i),2))
#     print(out)

domainName('http://github.com/anugrahnurhamid/apapun')
domainName1("http://www.zombie-bites.com")

def domainName(input):
    list 