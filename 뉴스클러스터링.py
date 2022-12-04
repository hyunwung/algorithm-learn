def solution(str1, str2):
    list1 = []
    list2 = []
    same = []
    for i in range(len(str1)):
        if str1[i] == str1[-1]:
            break
        if str1[i].isalpha() and str1[i+1].isalpha():
            list1.append(str1[i].lower() + str1[i + 1].lower())

    for i in range(len(str2)):
        if str1[i] == str1[-1]:
            break
        if str2[i].isalpha() and str2[i + 1].isalpha():
            list2.append(str2[i].lower() + str2[i + 1].lower())

    list1_c = list1.copy()
    all = list1.copy()
    for i in list2:
        if i not in list1_c:
            all.append(i)
        else:
            list1_c.remove(i)
    for i in list2:
        if i in list1:
            list1.remove(i)
            same.append(i)
    print(all)
    print(same)
    if len(all) == 0 and len(same) == 0:
        return 65536
    else:
        print(int(len(same)/len(all) * 65536))
        return int(len(same)/len(all) * 65536)

solution("handshake", "shake hands")
