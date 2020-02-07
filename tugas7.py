# #Funtion for check name 
# def check_name(name,alphabet):

def check_name(name,alphabet):
    print (alphabet.lower() in name or alphabet.upper() in name)

check_name("bayu","Y")

# # Function for check number (ganjil or genap)
# # # def add_even(number):
# # def ganjilgenap(number):
# #     if int(number) % 2==0:
# #         print("Genap")
# #     else:
# #         print("Ganjil") 

# # ganjilgenap(911)
# # #Function for check maximum number
# # def max_number(num1, num2, num3, num4):
# # def maxnumber(num1,num2,num3,num4):
# #     kelompokangka=[num1,num2,num3,num4]
# #     for angka in range(len(kelompokangka),0,-1):
# #         for j in range(0,angka-1):
# #             if kelompokangka[j]>kelompokangka[j+1]:
# #                 kelompokangka[j],kelompokangka[j+1]=kelompokangka[j+1],kelompokangka[j]
# #     return kelompokangka [3]
# # print(maxnumber(7,100,290,22))

# #FungsiFilter
# # def filter_text(text):
# #     listnama=list(text)
# #     out=""
# #     for item in listnama:
# #         if item.isdigit()==True:
# #             out+=item
# #     return out
# # print(filter_text("87anya"))

#Fungsicheckplat
# import datetime
# def check_plat(plat):
#     noplat= int(plat.split(" ")[1])
#     date=datetime.datetime.now()
#     dateD=date.strftime("%d")
#     date2=(list(dateD))
#     if int(date2[0])<1:
#         dateD=date2[1]
#     else:
#         pass
#     if int(dateD)%2==0:
#         if noplat%2==0:
#             print(f"untuk plat {plat} boleh lewat")
#         elif noplat%2!=0:
#             print(f"untuk plat {plat} tidak boleh lewat") 
#     elif int(dateD)%2!=0:
#         if noplat%2!=0:
#             print(f"untuk plat {plat} boleh lewat")
#         if noplat%2==0:
#             print(f"untuk plat {plat} tidak boleh lewat")
# check_plat("D 8975 JI")