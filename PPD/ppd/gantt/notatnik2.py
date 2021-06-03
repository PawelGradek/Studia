import matplotlib.pyplot as plt
import numpy as np
import random

def crear_gantt(maquinas, ht):
    # Parámetros:
    hbar = 10
    tticks = 10
    nmaq = len(maquinas)

    # Creación de los objetos del plot:
    fig, gantt = plt.subplots()

    # Diccionario con parámetros:
    diagrama = {
        "fig": fig,
        "ax": gantt,
        "hbar": hbar,
        "tticks": tticks,
        "maquinas": maquinas,
        "ht": ht
    }

    # Etiquetas de los ejes:
    gantt.set_xlabel("Czas")
    gantt.set_ylabel("Maszyna")

    # Límites de los ejes:
    gantt.set_xlim(0, ht)
    gantt.set_ylim(0, nmaq*hbar)

    # Divisiones del eje de tiempo:
    gantt.set_xticks(range(0, ht, 1), minor=True)
    gantt.grid(True, axis='x', which='both')

    # Divisiones del eje de máquinas:
    gantt.set_yticks(range(hbar, nmaq*hbar, hbar), minor=True)
    gantt.grid(True, axis='y', which='minor')

    # Etiquetas de máquinas:
    gantt.set_yticks(np.arange(hbar/2, hbar*nmaq - hbar/2 + hbar,
                            hbar))
    gantt.set_yticklabels(maquinas)

    return diagrama

# Función para armar tareas:
def agregar_tarea(diagrama, t0, d, maq, nombre, color=None):
    maquinas = diagrama["maquinas"]
    hbar = diagrama["hbar"]
    gantt = diagrama["ax"]
    ht = diagrama["ht"]

    # Chequeos:
    assert t0 + d <= ht, "La tarea debe ser menor al horizonte temporal."
    assert t0 >= 0, "El t0 no puede ser negativo."
    assert d > 0, "La duración d debe ser positiva."

    # Color:
    if color == None:
        r = random.random()
        g = random.random()
        b = random.random()
        color = (r, g, b)

    # Índice de la máquina:
    imaq = maquinas.index(maq)
    # Posición de la barra:
    gantt.broken_barh([(t0, d)], (hbar*imaq, hbar),
                      facecolors=(color))
    # Posición del texto:
    gantt.text(x=(t0 + d/2), y=(hbar*imaq + hbar/2),
                  s=f"{nombre} ({d})", va='center', ha='center', color='white')

def mostrar():
    plt.show()

ht =100
maquinas = ['M1', 'M2', 'M3']
diagrama = crear_gantt(maquinas, ht)
agregar_tarea(diagrama, 35,15,'M1','T1','r')
agregar_tarea(diagrama, 10,20,'M3','T1','g')
mostrar()

