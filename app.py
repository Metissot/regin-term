# Importamos las librerías necesarias
import os
import sys
from SistemaOp import *
# Definimos las opciones del menú
opciones = ["■  1 - Consultar Inhabilitados ", "■  2 - Alta Oficios ", "■  3 - Alta Personas ", "■  4 - Lista de  Oficios "]
titulo = "┌ REGISTRO DE INHABILITADOS          \n"
NewSistemaOp = SistemaOp()
# Bucle principal
while True:
	
    # Mostrar el título
    NewSistemaOp.limpiarConsola()
    print(titulo)
    
    # Mostramos el menú al usuario
    for opcion in opciones:
		
        print(opcion)
    
    # Solicitamos al usuario que elija una opción
    opcion_elegida = input("\n└   Elija una opción (1-4) :")

    # Validamos la opción elegida
    if opcion_elegida not in ["1", "2","3","4"]:
        print("Opción no válida.")
        continue

    # Ejecutamos la acción asociada a la opción elegida
    if opcion_elegida == "1":
        # Consultamos los inhabilitados
        print("Consultando inhabilitados...")

    elif opcion_elegida == "2":
        # Cargamos los oficios
        print("Cargando oficios...")
        
    elif opcion_elegida == "3":
		
        print("Cargando personas...")
    
    elif opcion_elegida == "4":
		
        print("Cargando Lista...")

    # Preguntamos al usuario si desea continuar
    continuar = input("¿continuar? (N para cancelar): ")

    # Salimos del bucle si el usuario responde "N"
    if continuar.upper() == "N":
        sys.exit()
