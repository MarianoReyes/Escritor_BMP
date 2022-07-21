'''
Escritor de Imágenes BMP
Jose Mariano Reyes 20074
'''
from gl import *

glinit()
glCreateWindow(100, 100)
glViewPort(12, 12, 90, 90)
glClearColor(1, 1, 1)
glClear()
glVertex(0.8, 0.8)
glColor(0.7, 0.5, 0.4)
glVertex(0.7, 0.7)
glColor(0.2, 0.9, 0.2)
glVertex(0.6, 0.6)
glFinish()
