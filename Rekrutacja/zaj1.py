'''To jest zadanie demonstracyjne.

Napisz funkcję:

def rozwiązanie(A)

że mając tablicę A składającą się z N liczb całkowitych, zwraca najmniejszą dodatnią liczbę całkowitą (większą niż 0), która nie występuje w A.

Na przykład, gdy A = [1, 3, 6, 4, 1, 2], funkcja powinna zwrócić 5.

Mając A = [1, 2, 3], funkcja powinna zwrócić 4.

Mając A = [−1, −3], funkcja powinna zwrócić 1.

Napisz efektywny algorytm dla następujących założeń:

N jest liczbą całkowitą z zakresu [ 1 .. 100 000 ];
każdy element tablicy A jest liczbą całkowitą z przedziału [ -1 000 000 .. 1 000 000 ].'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

A = [1, 3, 6, 4, 1, 2,-43,213]

def solution(A):
    # write your code in Python 3.6
    output = 1
    if output in A:
        new_A = []
        for i in A:
            if i > 0:
                new_A.append(i)
        flag = True
        minimum = output
        while flag:
            if minimum not in A:
                output = minimum
                flag = False
                print(output)

            else:
                minimum = minimum + 1
    return output

solution(A)
