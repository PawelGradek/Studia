import os


with open('afryka','r') as plik:
    linia = plik.readline()#.rstrip()
    #for linia in plik:
        #print(linia.replace(',',':'))
        #print(linia.join(''))
        #print(tuple(linia.strip().replace('(','').replace(')','').split(',')))
    lista_polaczona = [tuple(linia.strip().replace(':',',').split(',')) for linia in plik]
    print(lista_polaczona)


for i in lista_polaczona:
    if len(i)==2:
        print(f'({i[0]},{i[1]})')
    if len(i)==3:
        print(f'({i[0]},{i[1]})')
        print(f'({i[0]},{i[2]})')
    if len(i)==4:
        print(f'({i[0]},{i[1]})')
        print(f'({i[0]},{i[2]})')
        print(f'({i[0]},{i[3]})')
    if len(i)==5:
        print(f'({i[0]},{i[1]})')
        print(f'({i[0]},{i[2]})')
        print(f'({i[0]},{i[3]})')
        print(f'({i[0]},{i[4]})')
    if len(i)==6:
        print(f'({i[0]},{i[1]})')
        print(f'({i[0]},{i[2]})')
        print(f'({i[0]},{i[3]})')
        print(f'({i[0]},{i[4]})')
        print(f'({i[0]},{i[5]})')
    if len(i)==7:
        print(f'({i[0]},{i[1]})')
        print(f'({i[0]},{i[2]})')
        print(f'({i[0]},{i[3]})')
        print(f'({i[0]},{i[4]})')
        print(f'({i[0]},{i[5]})')
        print(f'({i[0]},{i[6]})')
    if len(i)==8:
        print(f'({i[0]},{i[1]})')
        print(f'({i[0]},{i[2]})')
        print(f'({i[0]},{i[3]})')
        print(f'({i[0]},{i[4]})')
        print(f'({i[0]},{i[5]})')
        print(f'({i[0]},{i[6]})')
        print(f'({i[0]},{i[7]})')

    if len(i)==9:
        print(f'({i[0]},{i[1]})')
        print(f'({i[0]},{i[2]})')
        print(f'({i[0]},{i[3]})')
        print(f'({i[0]},{i[4]})')
        print(f'({i[0]},{i[5]})')
        print(f'({i[0]},{i[6]})')
        print(f'({i[0]},{i[7]})')
        print(f'({i[0]},{i[8]})')

    if len(i)==10:
        print(f'({i[0]},{i[1]})')
        print(f'({i[0]},{i[2]})')
        print(f'({i[0]},{i[3]})')
        print(f'({i[0]},{i[4]})')
        print(f'({i[0]},{i[5]})')
        print(f'({i[0]},{i[6]})')
        print(f'({i[0]},{i[7]})')
        print(f'({i[0]},{i[8]})')
        print(f'({i[0]},{i[9]})')



