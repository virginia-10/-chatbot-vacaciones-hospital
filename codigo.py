import csv
from datetime import datetime

# Buscar empleado
def buscar_empleado(dni):
    with open("empleados.csv", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for empleado in lector:
            if empleado["dni"] == dni:
                return empleado

    return None


print("=== Solicitud de Vacaciones ===")

# Estado: Esperando DNI
while True:
    dni = input("Ingrese su DNI: ")

    empleado = buscar_empleado(dni)

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

    except:
        print("Formato incorrecto.")

# Estado: Validando días
dias_solicitados = (fin - inicio).days + 1
dias_disponibles = int(empleado["dias_disponibles"])

if dias_solicitados > dias_disponibles:
    print("No posee días suficientes.")
    exit()

# Estado: Evaluación del jefe
decision = input("¿Jefe aprueba? (S/N): ").upper()

if decision == "S":

    with open("solicitudes.csv", "a", newline="", encoding="utf-8") as archivo:
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