# #Dictionary
# same as list but have key value
# x = {
# "key1":"item1",
# "key2":"item2",
# "hewan":["gajah","rusa","harimau"]
# }

# print(x["hewan"][2])
# for key,val in x.items():
#     print(b)
#fungsi zip
# buah=["mangga","pisang","jambu"]
# harga=[1000,3000,3000]
# for item in zip(buah,harga):
#     print(item) ##hilangin dalam kurung,bisa ga zip ditambah

#LAMBDA
# def function(parameter):
#     return parameter+10

# x=lambda a: a+10
# print(x(5))

# number1 = [1,2,3]
# number2 = [4,5,6]
# z=0
# for a in range(len(number1)):
#     z+=number1[a]+number2[a]
# print(z)
## Duplication MAP
# list_nama=["uga","elga","anya"]

# def duplicationMAP(function,listaja):
#     hasil = []
#     for item in listaja:
#         hasil.append(function(item))
#     return hasil

# test = duplicationMAP(list,list_nama)
# print(list(test))
    

# result = map(lambda x,y : x+y,number1,number2)
# print(list(result))

#filter
#dia akan membuat kondisi tersebut betul atau tidak

tahun=[1993,1995,1997,2000]
# test= filter(lambda tahun: tahun % 2== 0,tahun)
# print(list(test))
def duplicatefiler(function,lista):
    hasil=[]
    for item in lista:
        if function(item):
            hasil.append(item)
    return hasil

test=duplicatefiler(lambda x:x%2==0,tahun)
print(list(test))