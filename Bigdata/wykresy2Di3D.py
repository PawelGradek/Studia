#import matplotlib.pyplot as plt

#aby uruchomić plik można użyć ctr + fn+ shift + f10

"""plt.figure(): stwórz nowy wykres 
plt.plot(): narysuj x i y jako linie i/lub markery
plt.xlabel(): oznacz oś x
plt.ylabel(): oznacz oś y
plt.title(): Dodaj tytuł dla swoich osi
plt.grid(): Skonfiguruj linie siatki
plt.legend(): Umieść odnośniki do legendy na swoich osiach
plt.savefig(): Zapisz wykres na dysku
plt.show(): Wyświetl wykres
plt.clf(): Usuń wykres (może się przydać do narysowania kilku wykresów w tym samym kodzie)


#wykres w 2d
x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]
plt.style.use('seaborn')# styl układu współrzędnych
fig, ax = plt.subplots() # konwencja matpllotlib, wywołanie funkcji subplot, pozwala na wygenerowanie jednego lub więcej wykresów na tym samym rysunku
ax.plot(x_values, y_values, linewidth = 3)# linewidth - grubość lini

ax.set_title("kwadraty liczb", fontsize = 24)
ax.set_xlabel("wartosci", fontsize = 12)
ax.set_ylabel("kwadraty wartosci", fontsize = 12)

ax.tick_params(axis = 'both', labelsize = 14)#zdefiniowanie wielkości etykiet

plt.show()


#---------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

#wykres w 3d jest to ogólna instrukcja dla wykresów punktowych, liniowych, konturowych, szkieletowych wystarczy tylko w kilku miejcach zmienić odpowiednie rzeczy

import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt


#definiujemy 3 osie
# wykres punktowy to np.
''''''
x = 7 * np.random.random(100)
y = np.sin(x) + 0.25 * np.random.random(100)
z = np.cos(x) + 0.25 * np.random.random(100)

# wykres liniowy to np.
'''
x = np.linspace(0, 15, 1000)
y = np.sin(xline)
z = np.cos(xline)
'''
#wykres konturowy, szkieletowy i powierzchniowy to np.
'''
x = np.linspace(-10, 10, 100)
y = np.linspace(-15, 15, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) + np.cos(Y)
'''
# stworzenie 3D kontynera
ax = plt.axes(projection = '3d')

'''To nie jest potrzebne na razie
#fig1 ponieważ nazwa fig jest już zajęta w tym programie, w tym przypadku stworzy puste okno
#fig1 = plt.figure(figsize=(6, 5))#rozmiar okna
#mpl.rcParams['legend.fontsize'] = 10 # wielkość czcionki  ax.plot(x,y,z, label = 'parametric curve')
#ax.plot(xdata,ydata,zdata, label = 'parametric curve') #połączenie punktów na wykresie
'''

# wizualizacja 3D  wykresu punktowego
ax.scatter3D(x, y, z)

# Jeśli chcemy mieć wykres liniowy
#ax.plot3D(x, y, z)

# Jeśli chcemy mieć wykres konturowy
#ax.contour3D(X, Y, Z, 100, cmap = 'viridis')

#Jeśli chcemy mieć wykres szkieletowy postępujemy tak jak w przypadku wykresu konturowego i zmieniamy tylko to:
#ax.plot_wireframe(X, Y, Z, 2, color = 'black', alpha = .2)

#lub powierzchniowy postępjemy tak jak przy tworzeniu wykresu konturowego
#ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = 'inferno')



# dodanie nazw osi
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

#ax.legend()
plt.show()






