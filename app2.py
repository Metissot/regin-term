import os
import sys
from persona import *
from SistemaOp import *
newPersona = Persona()
NewSistemaOp = SistemaOp()
class Sistema:
	
    def consultar_inhabilitados(self):
        print(" Consultando inhabilitados...")

    def cargar_oficios(self):
        print(" Cargando oficios...")

    def cargar_persona(self):
        NewSistemaOp.limpiarConsola()
        newPersona.ingresar_informacion()
        NewSistemaOp.limpiarConsola()
        newPersona.mostrar_informacion()
        

class Menu:
    def __init__(self):
        self.sistema = Sistema()
        self.opciones = {
            "1": self.sistema.consultar_inhabilitados,
            "2": self.sistema.cargar_oficios,
            "3": self.sistema.cargar_persona,
        }

    def mostrar_menu(self):
        NewSistemaOp.limpiarConsola()
        print(" ______________________________________________________")
        print("|             REGISTRO DE INHABILITADOS                |")
        print("                                                        ")
        print(" 1-Consultar inhabilitados                              ")
        print(" 2-Cargar oficios                                       ")
        print(" 3-Cargar persona                                       ")
        print("                                                        ")
        print("|                        ______________________________|")
    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion_elegida = input(" Elija una opción (1-3):")
            

            if opcion_elegida in self.opciones:
                self.opciones[opcion_elegida]()
            else:
                print(" Opción no válida.")

            continuar = input(" ¿Desea continuar? (S/N): ")
            if continuar.upper() == "N":
                sys.exit()

if __name__ == "__main__":
    menu = Menu()
    menu.ejecutar()
