'''
Escritor de Imágenes BMP
Jose Mariano Reyes 20074
'''
from gl import *

glinit()
glCreateWindow(1000, 1000)
glViewPort(6, 6, 900, 900)
glClearColor(1, 1, 1)
glClear()

glColor(0.6, 0.5, 0.2)
# pared izquierda
x0 = -0.6
y0 = -0.6
x1 = 0.1
y1 = -0.6

coordsf = []

for i in range(5000):
    y0 += 0.0001
    y1 += 0.0001
    glLine(x0, y0, x1, y1)

    if i == 4999:
        coordsf = [x0, y0, x1, y1]

glColor(0.75, 0.5, 0.2)

for i in range(3500):
    coordsf[0] += 0.0001
    coordsf[1] += 0.0001
    coordsf[2] += 0.0001
    coordsf[3] += 0.0001
    glLine(coordsf[0], coordsf[1], coordsf[2], coordsf[3])

    if i == 3499:
        coordsf = (coordsf[0], coordsf[1], coordsf[2], coordsf[3])
        x1, y1 = coordsf[2], coordsf[3]


glColor(0.9, 0.5, 0.2)
x0, yo = 0.1, -0.10000000000005158


for i in range(3500):
    x1 += 0.0001
    y1 -= 0.0001
    glLine(x0, y0, x1, y1)

    if i == 3499:
        coordsf = (x0, y0, x1, y1)

x0, y0, x1, y1 = coordsf[0], coordsf[1], coordsf[2], coordsf[3]

for i in range(5000):
    y0 -= 0.0001
    y1 -= 0.0001
    glLine(x0, y0, x1, y1)

glColor(0, 0, 0)
glLine(0.35, -0.6, 0.55, -0.6)
y0, y1 = -0.6, -0.6

for i in range(2500):
    y0 += 0.0001
    y1 += 0.0001
    glLine(0.35, y0, 0.55, y1)

    if i == 2499:
        y1 = y1

y0 = -0.6
x0 = 0.55
x1 = 0.55
glColor(0.3, 0.3, 0.3)

for i in range(1000):
    x0 -= 0.0001
    glLine(x0, y0, x1, y1)


glFinish()
