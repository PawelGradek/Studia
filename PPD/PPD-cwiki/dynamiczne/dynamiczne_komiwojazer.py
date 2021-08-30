macierz = [[0, 3, 5, 0, 0, 0, 0, 0, 0],  # numer wiersza to numer wierchołka, numer kolumny to numer wiercholka
           [0, 0, 0, 4, 8, 7, 0, 0, 0],  # jezeli w pierwszym wierszu w drugiej kolumnie jest 3 to to znaczy że odległoość od 1 wierzcholka do 2 wiercholka wynosi 3
           [0, 0, 0, 9, 6, 5, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 15, 10, 0],
           [0, 0, 0, 0, 0, 0, 0, 12, 0],
           [0, 0, 0, 0, 0, 0, 10, 12, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 4],
           [0, 0, 0, 0, 0, 0, 0, 0, 3],
           [0, 0, 0, 0, 0, 0, 0, 0, 0]
           ]# te liczby w macierzy to odległości

polaczenia_wierzcholkow = [[(1, 2), (1, 3)],
                           [(2,4), (2,5), (2,6), (3,4), (3,5), (3,6)],
                           [(4,7), (4,8), (5,8), (6,7), (6,8)],
                           [(7,9), (8,9)]]  # lista wierzcholkow polaczonych ze sobą

koszt_trasy = {1: 0}
n = 1

for polaczenia in polaczenia_wierzcholkow:
    print(f'\n Etap numer {n}')
    for polaczenie in polaczenia:
        print(polaczenie)
        try:
            print(f'{koszt_trasy[polaczenie[1]]}---{macierz[polaczenie[0] - 1][polaczenie[1] - 1] + koszt_trasy[polaczenie[0]]}')
            koszt_trasy[polaczenie[1]] = min(koszt_trasy[polaczenie[1]], macierz[polaczenie[0] - 1][polaczenie[1] - 1] + koszt_trasy[polaczenie[0]])
        except KeyError:
            print(f'null---{macierz[polaczenie[0] - 1][polaczenie[1] - 1] + koszt_trasy[polaczenie[0]]}')
            koszt_trasy[polaczenie[1]] = macierz[polaczenie[0] - 1][polaczenie[1] - 1] + koszt_trasy[polaczenie[0]]

    print()
    n += 1
    print(koszt_trasy)

print(f'\n Najmniejszy dystans to: {koszt_trasy[9]}')