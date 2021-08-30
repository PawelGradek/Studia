l1 = [5, 10, 11, 13, 14, 21, 28, 31, 35, 37, 41, 42, 52, 54, 61, 63, 64, 67, 68, 79]
l2 = [1, 2, 15, 19, 20, 22, 25, 31, 34, 35, 37, 39, 43, 51, 58, 59, 61, 69, 73, 75]
l3 = [2, 4, 6, 8, 12, 18, 22, 23, 26, 31, 34, 35, 36, 40, 46, 47, 54, 63, 70, 80]
l4 = [1, 4, 7, 15, 16, 22, 33, 35, 37, 38, 45, 50, 51, 56, 64, 67, 70, 74, 75, 79]
l5 = [5, 6, 11, 12, 21, 27, 32, 43, 44, 45, 46, 48, 52, 59, 62, 65, 68, 76, 78, 80]
l6 = [2, 6, 9, 25, 30, 32, 35, 37, 38, 48, 50, 53, 54, 55, 58, 60, 74, 75, 76, 77]
l7 = [1, 2, 8, 21, 22, 25, 27, 33, 36, 38, 40, 45, 48, 49, 53, 60, 63, 76, 77, 80]
l8 = [3, 6, 12, 19, 20, 23, 24, 25, 27, 29, 35, 37, 39, 54, 56, 67, 68, 69, 74, 76]
l9 = [2, 10, 12, 17, 20, 21, 25, 26, 29, 38, 40, 53, 55, 56, 57, 58, 64, 70, 71, 73]
l10 = [2, 10, 13, 17, 22, 24, 26, 27, 34, 36, 39, 46, 47, 50, 54, 56, 60, 62, 63, 73]
l11 = [4, 7, 13, 20, 22, 24, 32, 36, 39, 40, 42, 48, 50, 56, 57, 65, 67, 70, 77, 79]
l12 = [4, 5, 6, 7, 8, 9, 10, 13, 18, 30, 42, 48, 53, 56, 60, 64, 69, 75, 77, 80]
l13 = [1, 2, 12, 19, 20, 22, 24, 31, 33, 36, 42, 51, 54, 55, 68, 71, 73, 76, 77, 79]
l14 = [1, 10, 19, 20, 22, 24, 26, 27, 30, 34, 43, 45, 56, 58, 60, 62, 63, 64, 72, 80]
l15 = [10, 14, 15, 22, 23, 24, 25, 26, 28, 29, 32, 41, 50, 56, 59, 60, 67, 72, 75, 77]
l16 = [5, 7, 11, 14, 19, 20, 24, 30, 32, 33, 39, 45, 53, 54, 56, 62, 65, 68, 72, 75]
l17 = [3, 4, 7, 10, 11, 12, 15, 19, 20, 30, 33, 38, 43, 47, 48, 50, 54, 61, 69, 78]

l0 = []
for i in range(1, 81):
    l0.append(i)
# print(l0)

l1_17 = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16, l17]

##############################

l15koncowa = []
for i in l1_17[0:5]:
    for j in i:
        if j not in l15koncowa:
            l15koncowa.append(j)
# print(l15koncowa)

###########################hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# to kopiujemy
###  FRAGMENT DO KOPII ###
l26koncowa = []  # liczby które padły w ostatnich 5 losowaniach

przedzial = l1_17[11:16]
poczatek = l11
for i in przedzial:
    for j in i:
        if j not in l26koncowa:
            l26koncowa.append(j)
# print(padly_w_5_losowaniach)
b = []  # liczby które nie padły w ostatnich 5 losowaniach
for i in l0:
    if i not in l26koncowa:
        b.append(i)
# print('lista liczb ktore nie wystapily w ostatnich pieciu losowaniach nie_padly_w_5_loso : ',nie_padly_w_5_loso)
print('liczba elementow w padly_w_5_losowaniach', len(l26koncowa))
a = []  # lczby ktore padły w ostatnim losowaniu i wypadły w ostatnich pięciu losowaniach
for i in poczatek:
    if i in l26koncowa:
        a.append(i)
# print('to sa liczby ktore padly wypadly_teraz_i_w_pieciu_poprz', wypadly_teraz_i_w_pieciu_poprz)
c = []  # lczby ktore padły w ostatnim losowaniu ale nie wypadły w ostatnich pięciu losowaniach
for i in poczatek:
    if i in b:
        c.append(i)
print('lczby ktore padły w ostatnim losowaniu ale nie wypadły w ostatnich pięciu losowaniach: ', c)
