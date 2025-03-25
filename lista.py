import os

class Tarea:
    def __init__(self, descripcion):  # Constructor corregido
        self.descripcion = descripcion
        self.completada = False

def agregar_tarea(nombre_archivo):
    descripcion = input("Ingrese la asignatura de la tarea: ")
    tarea = Tarea(descripcion)  # Ahora sí se puede instanciar correctamente

    try:
        with open(nombre_archivo, "a") as archivo:
            archivo.write(f"{tarea.descripcion}\n")
        print("Tarea agregada exitosamente.")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al escribir en el archivo: {e}")

def mostrar_tareas(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            tareas = archivo.readlines()
            if tareas:
                print("\nTareas:")
                for i, tarea in enumerate(tareas, 1):
                    print(f"{i}. {tarea.strip()}")
            else:
                print("No hay tareas guardadas.")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def marcar_tarea_completada(nombre_archivo):
    mostrar_tareas(nombre_archivo)
    try:
        indice_tarea = int(input("\nIngrese el número de la tarea a completar: ")) - 1
        with open(nombre_archivo, "r") as archivo:
            tareas = archivo.readlines()

        if 0 <= indice_tarea < len(tareas):
            tarea_eliminada = tareas.pop(indice_tarea)
            with open(nombre_archivo, "w") as archivo:
                archivo.writelines(tareas)
            print(f"Tarea '{tarea_eliminada.strip()}' completada y eliminada.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Entrada inválida. Ingrese un número.")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al procesar la tarea: {e}")

# Menú principal
nombre_archivo = "tareas.txt"

while True:
    print("\n=== MENÚ ===")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Marcar tarea como completada")
    print("4. Salir")
    
    opcion = input("\nSeleccione una opción: ")
    
    if opcion == '1':
        agregar_tarea(nombre_archivo)
    elif opcion == '2':
        mostrar_tareas(nombre_archivo)
    elif opcion == '3':
        marcar_tarea_completada(nombre_archivo)
    elif opcion == '4':
        print("Hasta luego.")
        break
    else:
        print("Opción inválida. Intente de nuevo.")
