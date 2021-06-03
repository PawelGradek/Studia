import matplotlib.pyplot as plt

fig, gnt = plt.subplots()

# # Setting Y-axis limits
# gnt.set_ylim(0, 50)
#
# # Setting X-axis limits
# gnt.set_xlim(0, 160)


gnt.set_xlabel('Czas')
gnt.set_ylabel('Ilosc zasobów')

# Setting ticks on y-axis
gnt.set_yticks([10, 20, 30])
# Labelling tickes of y-axis
gnt.set_yticklabels(['1', '2', '3'])

# Setting graph attribute
gnt.grid(True)

# Declaring a bar in schedule
#1 od kiedy i długość 2 wysokosc-wspołrzędne i grubość
gnt.broken_barh([(40, 50)], (30, 9), facecolors=('tab:orange'))

# Declaring multiple bars in at same level and same width
gnt.broken_barh([(110, 10), (140, 10)], (10, 9),
                facecolors='tab:blue')

gnt.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9),
                facecolors=('tab:red'))
plt.show()