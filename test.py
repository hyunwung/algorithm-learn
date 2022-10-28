# def getFinalString(s):
#     for i in range(len(s)):
#         if "AWS" in s:
#             s = s.replace("AWS","")
#         else:
#             if s.isalpha() == False:
#                 s = -1
#             print(s)
#             return s
# getFinalString("AAWSWS")
import re

#
# def findRange(num):
#     string_num = str(num)
#     max_num = ""
#     min_mun = ""
#
#     max_num=string_num.replace("1","9")
#
#     min_mun = re.sub("[2-9]","0",string_num)
#
#     return int(max_num)-int(min_mun)
# findRange(909)

def findRange(num):
    n_list = list(map(int, str(num)))
    list_1 = n_list.copy()
    list_2 = n_list.copy()


    min_mun = min(n_list)
    max_num = max(n_list)
    if min_mun == 0:
        min_mun = min_mun + 1

    for i in range(len(list_1)):
        if list_1[i] == min_mun:
            list_1[i] = max_num


    s = [str(integer) for integer in list_1]
    a_string = "".join(s)
    res1 = int(a_string)

    for i in range(len(list_2)):

        if list_2[i] == max_num:
            list_2[i] = min_mun

    s = [str(integer) for integer in list_2]
    a_string = "".join(s)
    res2 = int(a_string)
    print(res1,res2)
    return res1-res2
findRange(17654)