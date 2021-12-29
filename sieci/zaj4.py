
with open('do_list_polaczonych','r') as plik:
    linia = plik.readline()#.rstrip()
    #for linia in plik:
        #print(linia.replace(',',':'))
        #print(linia.join(''))
        #print(tuple(linia.strip().replace('(','').replace(')','').split(',')))
    lista_polaczona = [tuple(linia.strip().replace('(','').replace(')','').split(',')) for linia in plik]
    print(lista_polaczona)
print('To jest lista polaczona:',lista_polaczona)

slo1 = {}
for (wA,wB) in lista_polaczona:
    if wA in slo1:
        slo1[wA].append(wB)
    else:
        slo1[wA] = [wB]
print(slo1)
