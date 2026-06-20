import csv
import os
from datetime import datetime

# Carpeta donde está guardado este script (sin importar desde dónde se ejecute)
CARPETA = os.path.dirname(os.path.abspath(__file__))
RUTA_EMPLEADOS = os.path.join(CARPETA, "empleados.csv")
RUTA_SOLICITUDES = os.path.join(CARPETA, "solicitudes.csv")


# Buscar empleado
def buscar_empleado(dni):
    with open(RUTA_EMPLEADOS, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for empleado in lector:
            if empleado["dni"] == dni:
                return empleado

    return None


print("=== Solicitud de Vacaciones ===")

# Estado: Esperando DNI
while True:
    dni = input("Ingrese su DNI: ")

    try:
        empleado = buscar_empleado(dni)
    except FileNotFoundError:
        print(f"No se encontró el archivo empleados.csv en: {CARPETA}")
        print("Verifique que el archivo esté en la misma carpeta que este script.")
        input("Presione ENTER para salir...")
        exit()
    except UnicodeDecodeError as e:
        print("ERROR: el archivo empleados.csv no está guardado en UTF-8.")
        print(f"Detalle técnico: {e}")
        print("Solución: abra el CSV con el Bloc de notas, use 'Guardar como' y elija codificación UTF-8.")
        input("Presione ENTER para salir...")
        exit()
    except Exception as e:
        print(f"ERROR inesperado: {type(e).__name__}: {e}")
        input("Presione ENTER para salir...")
        exit()

    if empleado:
        break

    print("Empleado no encontrado. Intente nuevamente.")

# Estado: Esperando Fechas
while True:

    fecha_inicio = input("Fecha inicio (dd/mm/yyyy): ")
    fecha_fin = input("Fecha fin (dd/mm/yyyy): ")

    try:
        inicio = datetime.strptime(fecha_inicio, "%d/%m/%Y")
        fin = datetime.strptime(fecha_fin, "%d/%m/%Y")

        if fin >= inicio:
            break

        print("Fechas inválidas.")

    except ValueError:
        print("Formato incorrecto.")

# Estado: Validando días
dias_solicitados = (fin - inicio).days + 1
dias_disponibles = int(empleado["dias_disponibles"])

if dias_solicitados > dias_disponibles:
    print("No posee días suficientes.")
    input("\nPresione ENTER para salir...")
    exit()

# Estado: Evaluación del jefe
while True:
    decision = input("¿Jefe aprueba? (S/N): ").strip().upper()

    if decision in ("S", "N"):
        break

    print("Respuesta no válida. Por favor ingrese S (Sí) o N (No).")

if decision == "S":

    with open(RUTA_SOLICITUDES, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)

        escritor.writerow([
            empleado["dni"],
            empleado["nombre"],
            fecha_inicio,
            fecha_fin,
            dias_solicitados,
            "Aprobada"
        ])

    print("Solicitud aprobada.")
    print("Oficina de Personal registra las vacaciones.")

else:
    print("Solicitud rechazada.")

input("\nPresione ENTER para salir...")