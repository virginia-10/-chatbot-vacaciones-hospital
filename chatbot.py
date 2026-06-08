
# ----- Sistema: Gestión de solicitudes de vacaciones -----


# 1. BASE DE DATOS SIMULADA (Refleja la tabla "Integración de Datos")
# Usamos el DNI como clave única para identificar a cada empleado
base_de_datos = {
    "34678921": {"nombre y apellido": "Juan Benitez", "dias_disponibles": 15},
    "35440332": {"nombre y apellido": "Maria Manchini", "dias_disponibles": 10}
}

# 2. INICIALIZACIÓN DE LA MÁQUINA DE ESTADOS
# Definimos los estados posibles: "INICIO", "ESPERANDO_DNI", "ESPERANDO_DIAS"
estado = "INICIO"
dni_actual = None

print(" SISTEMA AUTOMATIZADO DE GESTIÓN DE VACACIONES ")
print("Instrucciones: Escriba 'vacaciones' para comenzar.")

# 3. BUCLE PRINCIPAL (Mantiene al bot "escuchando" en la consola)
while True:
    mensaje = input("\nUsuario: ").strip().lower()
    
    # --- ESTADO INICIAL ---
    if estado == "INICIO":
        if mensaje.lower() == "vacaciones":
            print("Bot: Bienvenido al sistema. Por favor, ingrese su Nombre, Apellido y DNI: ")
            estado = "ESPERANDO_DATOS"
        else:
            # Entrada inválida antes de iniciar
            print("Bot:Comando no reconocido. Escriba 'vacaciones'.")
            
    # --- ESTADO: VALIDACIÓN DE DATOS ---
    elif estado == "ESPERANDO_DATOS":
        # Verificamos si la entrada existe en nuestra base de datos simulada
        dni_encontrado = None
        for dni in base_de_datos:
            if dni in mensaje:
                dni_encontrado = dni
                break
        if dni_encontrado:
            dni_actual = dni_encontrado
            nombre_completo = base_de_datos[dni_actual]["nombre y apellido"]
            
            # El bot extrae los datos y saluda de manera personalizada
            print(f"Bot: Éxito. Empleado verificado: {nombre_completo}.")
            print("Bot: ¿Cuántos días de vacaciones desea solicitar?")
            estado = "ESPERANDO_DIAS"
        else:
            # CASO 5: Rulo de retorno si el DNI no existe (Camino infeliz del BPMN)
            print("Bot: [Camino Infeliz] Error: los datos ingresados no existe en nuestra base de datos.")
            print("Bot: Por favor, intente nuevamente Nombre, Apellido y DNi: ")
                       
    # --- ESTADO: VALIDACIÓN DE DÍAS ---
    elif estado == "ESPERANDO_DIAS":
        # CASO 3: Validación técnica de entrada (comprueba si es un número válido)
        if mensaje.isdigit():
            dias_solicitados = int(mensaje)
            
            # CASO 4: Validación de número menor o igual a cero
            if dias_solicitados <= 0:
                print("Bot: [Camino Infeliz] Error: la cantidad de días debe ser mayor a cero.")
                print("Bot: Intente nuevamente:")
            else:
                nombre_completo = base_de_datos[dni_actual]["nombre y apellido"]
                dias_disponibles = base_de_datos[dni_actual]["dias_disponibles"]
                
                print(f"Empleado: {nombre_completo} | Disponibles: {dias_disponibles} | Solicitados: {dias_solicitados}")
                
                #DIAGRAMA TO-BE: ¿Tiene días suficientes?
                if dias_solicitados <= dias_disponibles:
                    # CASO 1: Aprobación por saldo suficiente
                    print("Bot:Solicitud APROBADA automáticamente")
                else:
                    # CASO 2: Rechazo por falta de días
                    print("Bot:Solicitud RECHAZADA")
                    print(f"Bot: Motivo: No posee días suficientes para realizar la solicitud.")
                
                # Finalización del ciclo de vida del trámite. 
                print("Bot: Sistema libre. Ingrese 'vacaciones' para una nueva consulta:")
                estado = "INICIO"
                dni_actual = None
        else:
            # CASO 3: El usuario ingresó texto en lugar de un número de días
            print("Bot: [Camino Infeliz] Error: debe ingresar un número válido.")
            print("Bot: Intente nuevamente:")