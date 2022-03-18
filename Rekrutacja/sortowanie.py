lista =[90, 45, 67, 23,24, 67.5,34,78]

lista_skopiowana = lista.copy()
lisa_pomocnicza = []

while lista_skopiowana !=[]:
    max_wartosc = lista_skopiowana[0]
    for i in lista_skopiowana:
        if i > max_wartosc:
            max_wartosc = i
    lisa_pomocnicza.append(max_wartosc)
    lista_skopiowana.remove(max_wartosc)

print(lisa_pomocnicza)



