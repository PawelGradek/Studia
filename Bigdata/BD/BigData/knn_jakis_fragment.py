import pandas as pd
dane = {
    'A': [(12, 3), (4, 5), (3, 8), (6, 4), (4, 9)],
    'B': [(2, 7), (3, 6), (2, 11), (7, 1), (8, 7)]
}
df = pd.DataFrame(dane)

treningowe = df[:4].to_dict(orient="list") #80% = 4
dane_testowe = df[4:].to_dict(orient="list") #10% = 1
dane_do_testu = sum(list(dane_testowe.values()), [])  # potrzebujemy jedynie elementów do klasyfikacji
print(dane_testowe)
print(treningowe)
print(dane_do_testu)

print(int(False))


1