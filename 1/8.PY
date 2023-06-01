import os

def agregar_persona():
    # Código para agregar una persona
    print("Opción Agregar Personas seleccionada.")

def ver_persona():
    # Código para ver una persona
    print("Opción Ver Persona seleccionada.")

def limpiar_pantalla():
    if os.name == 'posix':
        os.system('clear')  # Para sistemas basados en Unix/Linux
    else:
        os.system('cls')  # Para sistemas basados en Windows

while True:
    print("----- MENÚ -----")
    print("1) Agregar Personas")
    print("2) Ver Persona")
    print("3) Limpiar Pantalla")
    print("0) Salir")

    opcion = input("Ingrese el número de opción que desea ejecutar: ")

    if opcion == "1":
        agregar_persona()
    elif opcion == "2":
        ver_persona()
    elif opcion == "3":
        limpiar_pantalla()
    elif opcion == "0":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
