#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
import numpy as np
import time
import random
import serial
import sys
from random import randrange
import subprocess

#conectarse al arduino en el puerto que corresponda
device='/dev/ttyACM1'
print "Trying to connect"
con = 0
salir = False
arduino = serial.Serial(device, 9600)

#crear un archivo para el log
#file = open("testfile_lectura.txt","w")

#variables
valor = arduino.readline()
tareas=['tarea1','tarea2','tarea3','tarea4','tarea5']
dific=[1,1,1,1,1]

#lectura de tareas
while salir == False:

    tarea = raw_input("Introduce tarea: ")
    tareas[con] = tarea

    dificultad = raw_input("Introduce dificultad: ")
    dific[con] = dificultad

    con = con + 1
    if con == 4:
        salir = True

#cerramos el log
#file.close()
#for i, val in enumerate(tareas):

for i, val in enumerate(tareas):
    if valor > 50 and dific[i] > 3:
        print(tareas[i])
    if valor < 50 and dific[i] < 3:
        print(tareas[i])

    time.sleep(20)
