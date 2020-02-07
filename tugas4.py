# #Soal1
# def duplicate_string(parameter):
#     word = ''
#     n=1
#     lowers=parameter.lower()
#     for char in (lowers):
#         word += char * n
#         n+= 1
#     print(word)

# duplicate_string('anuGeRah')
# duplicate_string('GrIzly')
# #Soal2
# def duplicate_string_strip(parameter):
#     word = ''
#     n=1
#     for char in (parameter):
#         word += "-" + (char* n).capitalize()
#         n+=1  
#     print(word)
# duplicate_string_strip("anya")
# duplicate_string_strip("anugerah")
#Soal3
def fungsi_sort_ascending(parameter):
    for item1 in range(0,4):
        for item2 in range(item1+1,len(parameter)):
            if parameter[item1]> parameter[item2]:
               parameter[item1],parameter[item2] = parameter[item2],parameter[item1]
        print(parameter)

(fungsi_sort_ascending([1,10,2,6,1,2,5,6,10]))

# def fungsi_sort_descending(parameter):
#     for item1 in range(0,len(parameter)-1):
#         for item2 in range (item1+1,len(parameter)):
#             if parameter[item1]< parameter[item2]:
#                 parameter [item1],parameter [item2]= parameter [item2], parameter [item1]
#     return(parameter)

# print(fungsi_sort_descending([1,10,2,6,1,2,5,6,10]))
