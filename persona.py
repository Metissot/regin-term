
class Persona:
    def __init__(self):
        self.dni = ""
        self.nombre = ""
        self.apellido = ""

    def ingresar_informacion(self):
        print(" _____________________________________________________")
        print("|          FORMULARIO DE ALTA DE PERSONAS             |")
        self.dni = input("| INGRESE DNI: ")
        self.nombre = input("| INGRESE NOMBRE: ")
        self.apellido = input("| INGRESE APELLIDO")
        print("|_____________________________________________________|")

        

    def mostrar_informacion(self):
       
        print(" _____________________________________________________")
        print("|          FORMULARIO DE ALTA DE PERSONAS             |")
        print(f" {self.dni}")
        print(f" {self.apellido}, {self.nombre}")
        print("|                               _____________________|")
        accion = input("¿Desea guardar? (1-SI   2-NO): ")
        if accion == "1":
            pass
        elif accion == "2":
            pass
        else:
            print("\n OPCION INVALIDA \n")
            pass


             

    def cargar_persona(self):
        print("Cargando información de la persona...")
        # Puedes realizar aquí cualquier acción de carga necesaria.

# Ejemplo de uso de la clase CargarPersona:
Newpersona = Persona()
#persona.ingresar_informacion()
#persona.mostrar_informacion()
