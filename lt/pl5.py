# l1 = [5, 10, 11, 13, 14, 21, 28, 31, 35, 37, 41, 42, 52, 54, 61, 63, 64, 67, 68, 79]
# l2 = [1, 2, 15, 19, 20, 22, 25, 31, 34, 35, 37, 39, 43, 51, 58, 59, 61, 69, 73, 75]
# l3 = [2, 4, 6, 8, 12, 18, 22, 23, 26, 31, 34, 35, 36, 40, 46, 47, 54, 63, 70, 80]
# l4 = [1, 4, 7, 15, 16, 22, 33, 35, 37, 38, 45, 50, 51, 56, 64, 67, 70, 74, 75, 79]
# l5 = [5, 6, 11, 12, 21, 27, 32, 43, 44, 45, 46, 48, 52, 59, 62, 65, 68, 76, 78, 80]
# l6 = [2, 6, 9, 25, 30, 32, 35, 37, 38, 48, 50, 53, 54, 55, 58, 60, 74, 75, 76, 77]
# l7 = [1, 2, 8, 21, 22, 25, 27, 33, 36, 38, 40, 45, 48, 49, 53, 60, 63, 76, 77, 80]

l1 = [2,11,20,23,24,26,33,36,39,42,43,55,57,59,62,65,73,77,78,79]

l2 = [5,11,13,16,17,19,23,34,35,36,43,54,60,61,63,64,66,72,76,80]

l3 = [8,12,14,17,21,22,26,27,45,46,51,52,55,57,62,65,66,75,77,79	]

l4 = [1,6,12,14,15,20,21,25,29,30,32,34,37,39,41,43,45,47,64,70]

l5 = [1,12,13,20,25,26,28,29,31,34,38,42,43,45,51,54,55,57,62,70]




l0 = []
for i in range(1, 81):
    l0.append(i)

l1_17 = [l1, l2, l3, l4, l5]

###  FRAGMENT DO KOPII ###
przedzial = l1_17
poczatek = l1

padly_w_5_losowaniach = []  # liczby które padły w ostatnich 5 losowaniach
for i in przedzial:
    for j in i:
        if j not in padly_w_5_losowaniach:
            padly_w_5_losowaniach.append(j)
# print(padly_w_5_losowaniach)
nie_padly_w_5_loso = []  # liczby które nie padły w ostatnich 5 losowaniach
for i in l0:
    if i not in padly_w_5_losowaniach:
        nie_padly_w_5_loso.append(i)
print('lista liczb ktore nie wystapily w ostatnich pieciu losowaniach nie_padly_w_5_loso : ', nie_padly_w_5_loso)
print('liczba elementów które nie padły w ostatnich 5 losowaniach', len(nie_padly_w_5_loso))
# print('liczba elementow ktore wpadly_w_5_losowaniach', len(padly_w_5_losowaniach))

# to służy sprawdzeniu ile liczb wylosowano z tych liczb które wypadływ  ostatnich 5 losowaniach
wypadly_teraz_i_w_pieciu_poprz = []  # lczby ktore padły w ostatnim losowaniu i wypadły w ostatnich pięciu losowaniach
for i in poczatek:
    if i in padly_w_5_losowaniach:
        wypadly_teraz_i_w_pieciu_poprz.append(i)
# print('to sa liczby ktore padly wypadly_teraz_i_w_pieciu_poprz', wypadly_teraz_i_w_pieciu_poprz)
wypadly_teraz_ale_nie_w_poprz_pieciu = []  # lczby ktore padły w ostatnim losowaniu ale nie wypadły w ostatnich pięciu losowaniach
for i in poczatek:
    if i in nie_padly_w_5_loso:
        wypadly_teraz_ale_nie_w_poprz_pieciu.append(i)
# print('lczby ktore padły w ostatnim losowaniu ale nie wypadły w ostatnich pięciu losowaniach: ', wypadly_teraz_ale_nie_w_poprz_pieciu)

# wybieramy te liczby które nie wypadły w dwóch ostatnich losowaniach i które wypadły w ostatnich 5 losowaniach (jest ich około25)

lista_po_srodku = []
for i in l0:
    if i not in l1 and i not in l2 and i not in nie_padly_w_5_loso:
        lista_po_srodku.append(i)
print('lista po srodku:', lista_po_srodku)
print('liczba elementów w liscie po srodku', len(lista_po_srodku))

lista_z_poczatku = []
for i in l1:
    lista_z_poczatku.append(i)
for i in l2:
    if i not in lista_z_poczatku:
        lista_z_poczatku.append(i)
print('lista z poczatku', lista_z_poczatku)
print('dlugosc listy z poczatku', len(lista_z_poczatku))


# wszystko działa poprawnie teraz tylko stworzyć funkcje z systemami na 20 i 30 liczb


def funkcja1(a1, b2, c3, d4, e5, f6, g7, h8, i9, j10, k11, l12, m13, n14, o15, p16, r17, s18, t19, u20, w21, y22, x23,
             z24, a25, b26, c27, d28, e29, f30, g31, h32, i33, j34, k35, l36):
    print('Wyniki z pierwszej funkcji')
    print(a1, b2, c3, d4, e5, f6, i9, k11, o15,)
    print(a1, b2, c3, d4, f6, g7, l12, p16, r17,)
    print(a1, b2, c3, e5, g7, i9, k11, l12, r17,)
    print(a1, b2, c3, g7, h8, i9, m13, o15, p16,)
    print(a1, b2, c3, i9, j10, k11, n14, o15, r17,)
    print(a1, b2, d4, g7, i9, j10, k11, p16, r17,)
    print(a1, b2, d4, h8, i9, j10, l12, m13, n14,)
    print(a1, b2, e5, f6, g7, i9, k11, n14, p16,)
    print(a1, b2, e5, f6, h8, i9, j10, m13, r17,)
    print(a1, b2, f6, i9, j10, k11, l12, o15, p16,)
    print(a1, c3, d4, f6, g7, i9, j10, l12, n14,)
    print(a1, c3, d4, h8, j10, l12, m13, o15, r17,)
    print(a1, c3, f6, h8, k11, m13, n14, p16, r17,)
    print(a1, d4, e5, f6, g7, h8, l12, m13, p16,)
    print(a1, d4, e5, i9, l12, n14, o15, p16, r17,)
    print(a1, e5, g7, h8, j10, k11, m13, n14, o15,)
    print(b2, c3, d4, e5, i9, j10, l12, o15, p16,)
    print(b2, c3, d4, f6, g7, h8, j10, k11, m13,)
    print(b2, c3, d4, g7, k11, l12, n14, o15, p16,)
    print(b2, c3, e5, f6, h8, l12, m13, n14, o15,)
    print(b2, d4, e5, f6, j10, k11, l12, n14, r17,)
    print(b2, d4, e5, h8, k11, m13, o15, p16, r17,)
    print(b2, g7, h8, j10, l12, m13, n14, p16, r17,)
    print(c3, d4, e5, g7, h8, i9, m13, n14, r17,)
    print(c3, e5, f6, g7, j10, n14, o15, p16, r17,)
    print(c3, e5, h8, i9, j10, k11, l12, m13, p16,)
    print(d4, f6, h8, i9, j10, m13, n14, o15, p16,)
    print(f6, g7, h8, i9, k11, l12, m13, o15, r17,)
    print(s18, t19, u20, w21, y22, e29, f30, k35, l36,)
    print(s18, t19, w21, y22, x23, d28, e29, f30, k35,)
    print(s18, t19, w21, z24, a25, e29, f30, g31, i33,)
    print(s18, t19, w21, b26, c27, e29, f30, h32, j34,)
    print(s18, u20, w21, x23, z24, c27, h32, i33, k35,)
    print(s18, u20, w21, x23, a25, b26, g31, j34, k35,)
    print(s18, w21, y22, z24, b26, d28, i33, j34, l36,)
    print(s18, w21, y22, a25, c27, d28, g31, h32, l36,)
    print(t19, u20, y22, x23, z24, b26, e29, g31, h32,)
    print(t19, u20, y22, x23, a25, c27, e29, i33, j34,)
    print(t19, u20, d28, e29, g31, h32, i33, j34, k35,)
    print(t19, x23, z24, a25, b26, c27, e29, f30, l36,)
    print(t19, z24, c27, d28, e29, g31, j34, k35, l36,)
    print(t19, a25, b26, d28, e29, h32, i33, k35, l36,)
    print(u20, y22, z24, a25, b26, c27, d28, f30, k35,)
    print(u20, y22, a25, b26, f30, g31, h32, i33, j34,)
    print(u20, x23, z24, a25, d28, f30, h32, j34, l36,)
    print(u20, x23, b26, c27, d28, f30, g31, i33, l36,)
    print(y22, x23, z24, a25, b26, c27, h32, j34, k35,)
    print(y22, x23, f30, g31, h32, i33, j34, k35, l36,)
    print(y22, z24, a25, c27, f30, g31, i33, j34, k35,)
    print(y22, z24, b26, c27, f30, g31, h32, i33, k35)



def funkcja2(a1, b2, c3, d4, e5, f6, g7, h8, i9, j10, k11, l12, r13, s14, t15, u16, w17, x18, y19, z20, a21, b22, c23, d24,):
    print('Wyniki z drugij funkcji')
    print('1:--',a1, b2, c3, h8, b22,)
    print('2:--',a1, c3, s14, a21, d24,)
    print('3:--',a1, d4, i9, t15, u16,)
    print('4:--',a1, e5, f6, k11, x18,)
    print('5:--',a1, g7, j10, l12, y19,)
    print('6:--',a1, h8, j10, c23, d24,)
    print('7:--',a1, r13, s14, t15, w17,)
    print('8:--',a1, w17, z20, a21, b22,)
    print('9:--',b2, c3, r13, u16, x18,)
    print('10:--',b2, d4, e5, l12, d24,)
    print('11:--',b2, d4, g7, r13, c23,)
    print('12:--',b2, f6, g7, i9, a21,)
    print('13:--',b2, h8, u16, w17, d24,)
    print('14:--',b2, j10, k11, s14, z20,)
    print('15:--',b2, t15, x18, y19, c23,)
    print('16:--',c3, d4, g7, w17, x18,)
    print('17:--',c3, d4, j10, k11, z20,)
    print('18:--',c3, e5, i9, l12, c23,)
    print('19:--',c3, f6, j10, s14, t15,)
    print('20:--',c3, f6, r13, y19, d24,)
    print('21:--',c3, t15, y19, z20, a21,)
    print('22:--',d4, e5, h8, r13, b22,)
    print('23:--',d4, f6, s14, y19, z20,)
    print('24:--',d4, k11, s14, a21, c23,)
    print('25:--',d4, x18, y19, a21, d24,)
    print('26:--',e5, g7, h8, s14, u16,)
    print('27:--',e5, i9, r13, z20, d24,)
    print('28:--',e5, j10, t15, w17, a21,)
    print('29:--',e5, u16, y19, b22, c23,)
    print('30:--',f6, h8, l12, t15, z20,)
    print('31:--',f6, j10, u16, w17, b22,)
    print('32:--',f6, l12, w17, c23, d24,)
    print('33:--',g7, k11, t15, b22, d24,)
    print('34:--',g7, u16, x18, z20, c23,)
    print('35:--',h8, i9, k11, w17, y19,)
    print('36:--',h8, j10, r13, x18, a21,)
    print('37:--',i9, j10, r13, b22, c23,)
    print('38:--',i9, l12, s14, x18, b22,)
    print('39:--',k11, l12, r13, u16, a21)


# nie padly 3, 4, 7, 9, 10, 18, 40, 44, 48, 49, 50, 53, 56, 58, 67, 68, 69, 71, 74
# po srodku 1, 6, 8, 12, 14, 15, 21, 22, 25, 27, 28, 29, 30, 31, 32, 37, 38, 41, 45, 46, 47, 51, 52, 70, 75
# funkcja1()
# funkcja2()
funkcja2(3, 4, 7, 9, 10, 18, 40, 44, 48, 49, 50, 53, 56, 58, 67, 68, 69, 71, 74, 14, 31, 75, 37, 34)
funkcja2(1, 6, 8, 12,  15, 21, 22, 25, 27, 28, 29, 30, 31, 32, 37, 38, 41, 45, 46, 47, 51, 52, 70, 75)