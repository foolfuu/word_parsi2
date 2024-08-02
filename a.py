f = open("pars_words.txt" , "r" , encoding = "utf8")
word = f.readlines()
f.close()
hor = {"ا":1 , "ی":2 , "ن":3 , "ر":4 , "د":5 , "م":6 , "ه":7 , "و":8 , "ت":9 , "ب":10 , "س":11 , "ش":12 , "ک":13 , "ز":14 , "ل":15 , "گ":16 , "ق":17 , "ف":18 , "خ":19 , "ع":20 , "ح":21 , "ج":22 , "آ":23 , "پ":24 , "چ":25 , "ض":26 , "ط":27 , "ص":28 , "غ":29 , "ظ":30 , "ث":31 , "ذ":32 , "ء":33 ,"ژ":34}
for i in range(len(word)): word[i] = word[i].strip()
f_list = list()
for i in word:
    if len(i) == 5: f_list.append(i)
f_list2 = list()
for i in f_list:
    temp = 0
    for d in i:
        if d in hor: temp += hor[d]
    if temp <= 14: f_list2.append(i)

print(len(f_list2))
print("\n\n\n")
for i in f_list2:
    print(i , end = " --> ")
    temp = 0
    for d in i:
        if d in hor: temp += hor[d]
    print(temp)
