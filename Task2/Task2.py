def task21(a):
    txt: str=str(a)
    if txt == "11":
        return " рублей"
    elif txt == "13":
        return " рублей"
    elif txt == "14":
        return " рублей"
    elif txt == "10":
        return " рублей"
    elif txt[int(len(txt)) - 1] == '1':
        return " рубль"
    elif txt[int(len(txt)) - 1] == '2':
        if txt[int(len(txt)) - 2] == '1':
            return " рублей"
        return " рубля"
    elif txt[int(len(txt)) - 1] == '3':
        return " рубля"
    elif txt[int(len(txt)) - 1] == '4':
        return " рубля"
    elif txt[int(len(txt)) - 1] == '5':
        return " рублей"
    elif txt[int(len(txt)) - 1] == '6':
        return " рублей"
    elif txt[int(len(txt)) - 1] == '7':
        return " рублей"
    elif txt[int(len(txt)) - 1] == '8':
        return " рублей"
    elif txt[int(len(txt)) - 1] == '9':
        return " рублей"
    elif txt[int(len(txt)) - 1] == '0':
        return " рублей"


def task22(a):
    a=str(a)
    if a == "11":
        return " копеек"
    elif a == "13":
        return " копеек"
    elif a == "14":
        return " копеек"
    elif a == "10":
        return " копеек"
    elif a[int(len(a)) - 1] == '1':
        return " копейка"
    elif a[int(len(a)) - 1] == '2':
        if a[int(len(a)) - 2] == '1':
            return " копеек"
        return " копейки"
    elif a[int(len(a)) - 1] == '3':
        return " копейки"
    elif a[int(len(a)) - 1] == '4':
        return " копейки"
    elif a[int(len(a)) - 1] == '5':
        return " копеек"
    elif a[int(len(a)) - 1] == '6':
        return " копеек"
    elif a[int(len(a)) - 1] == '7':
        return " копеек"
    elif a[int(len(a)) - 1] == '8':
        return " копеек"
    elif a[int(len(a)) - 1] == '9':
        return " копеек"
    elif a[int(len(a)) - 1] == '0':
        return " копеек"


def Task23(a):
    a=str(a)
    lst = ["0", " ноль", "1", " один", "2", " два", "3", " три", "4", " четыри", "5", " пять", "6", " шесть",
           "7", " семь", "8", " восемь", "9", " девять",
           "10", " десять", "20", " двадцать", "30", " тридтать", "40", " сорок", "50", " пятьдесят", "60", " шестьдесят",
           "70", " семьдесят", "80", " восемьдесят", "90", " девяносто",
           "100", " сто", "200", " двести", "300", " триста", "400", " четыриста", "500", " пятьсот", "600", " шестьсот",
           "700", " семьсот", "800", " восемьсот", "900", " девятсот" ]
    strata: str=""
    if 0 == int(len(a)) - 1:
        strata = lst[lst.index(a) + 1]
        return strata
    elif 1 == int(len(a)) - 1:
        if a[int(len(a)) - 1] == "0":
            strata = lst[lst.index(str(int(a[0]) * 10)) + 1]
        else:
            strata = lst[lst.index(str(int(a[0]) * 10)) + 1]
            strata += lst[lst.index(a[1]) + 1]
        return strata
    elif 2 == int(len(a)) - 1:
        if a[int(len(a)) - 2] == "0" and a[int(len(a)) - 1] == "0":
            strata = lst[lst.index(str(int(a[0]) * 100)) + 1]
        elif a[int(len(a)) - 2] == "0" and a[int(len(a)) - 1] != "0":
            strata = lst[lst.index(str(int(a[0]) * 100)) + 1]
            strata += lst[lst.index(a[2]) + 1]
        elif a[int(len(a)) - 2] != "0" and a[int(len(a)) - 1] == "0":
            strata = lst[lst.index(str(int(a[0]) * 100)) + 1]
            strata += lst[lst.index(str(int(a[1]) * 10)) + 1]
        else:
            strata = lst[lst.index(str(int(a[0]) * 100)) + 1]
            strata += lst[lst.index(str(int(a[1]) * 10)) + 1]
            strata += lst[lst.index(a[2]) + 1]
        return strata
    else:
        return "Ввели неверное число"

def Task24(a):
    a=str(a)
    lst = ["0", " ноль", "1", " одна", "2", " две", "3", " три", "4", " четыри", "5", " пять", "6", " шесть",
           "7", " семь", "8", " восемь", "9", " девять",
           "10", " десять", "20", " двадцать", "30", " тридтать", "40", " сорок", "50", " пятьдесят", "60", " шестьдесят",
           "70", " семьдесят", "80", " восемьдесят", "90", " девяносто",
           "100", " сто", "200", " двесте", "300", " триста", "400", " четыриста", "500", " пятьсот", "600", " шестьсот",
           "700", " семьсот", "800", " восемьсот", "900", " девятсот" ]
    strata: str=""
    if 0 == int(len(a)) - 1:
        strata = lst[lst.index(a) + 1]
        return strata
    elif 1 == int(len(a)) - 1:
        if a[int(len(a)) - 1]=="0":
            strata = lst[lst.index(str(int(a[0])*10)) + 1]
        else:
            strata = lst[lst.index(str(int(a[0]) * 10)) + 1]
            strata+= lst[lst.index(a[1]) + 1]
        return  strata
    elif 2 == int(len(a)) - 1:
        if a[int(len(a)) - 2]=="0" and a[int(len(a)) - 1]=="0":
            strata = lst[lst.index(str(int(a[0]) * 100)) + 1]
        elif   a[int(len(a)) - 2]=="0" and a[int(len(a)) - 1]!="0":
            strata = lst[lst.index(str(int(a[0]) * 100)) + 1]
            strata += lst[lst.index(a[2]) + 1]
        elif a[int(len(a)) - 2]!="0" and a[int(len(a)) - 1]=="0":
            strata = lst[lst.index(str(int(a[0]) * 100)) + 1]
            strata += lst[lst.index(str(int(a[1]) * 10)) + 1]
        else:
            strata = lst[lst.index(str(int(a[0])*100)) + 1]
            strata += lst[lst.index(str(int(a[1])*10)) + 1]
            strata += lst[lst.index(a[2]) + 1]
        return strata
    else:
        return "Ввели неверное число"




def Task25(a):
     s=str(a)
     str1=s.split('.')
     s=Task24(str1[0])
     s+=task21(str1[0])
     s+="  "
     s+=Task24(str1[1])
     s+=task22(str1[1])
     return s


a=int(input("Task21 Введите число:"))
s = task21(a)
print(s)
a=int(input("Task22 Введите число:"))
s = task22(a)
print(s)
a=int(input("Task23 Введите число:"))
s=Task23(a)
print(s)
a=int(input("Task24 Введите число:"))
s=Task24(a)
print(s)
a=float(input("Task25 Введите число:"))
s=Task25(a)
print(s)
