# Chatbot Vacaciones Hospital

Este proyecto simula un chatbot diseñado para gestionar solicitudes de vacaciones del personal hospitalario, con el objetivo de optimizar tiempos de respuesta y reducir errores administrativos.

---

## Funcionalidades

- Solicitud de días de vacaciones mediante conversación
- Validación de datos ingresados por el usuario
- Consulta de disponibilidad en base de datos
- Aprobación o rechazo automático de solicitudes
- Manejo de errores (camino infeliz)

---

### Tecnologías utilizadas

- **Python** (simulación de la lógica del chatbot)
- **WhatsApp Business API** (canal de comunicación propuesto)
- **Base de datos en Excel** (almacenamiento de datos de empleados)

---

#### Descripción del funcionamiento

El sistema permite a un usuario iniciar una solicitud de vacaciones escribiendo un comando en el chatbot.

El flujo del proceso es el siguiente:

1.	Inicio del trámite: El usuario inicia la conversación escribiendo “vacaciones”. 
2.	Solicitud de datos personales: el chatbot recibe el comando y le solicita al usuario que ingrese Nombre, Apellido y DNI.
3.	Validar identidad (camino feliz/infeliz): 
	Camino feliz: el usuario ingresa Nombre, Apellido y DNI valido, el sistema lo reconoce en la base de datos y lo saluda por su nombre.
	Camino infeliz: si el Nombre, Apellido y DNI no existe e el sistema, el bot muestra un mensaje de error y le solicita que lo ingrese nuevamente de forma correcta.
4.	Solicitud de días: una vez validado el empleado, el chatbot le solicita “Ingresar cantidad de días”.
5.	Ingreso de cantidad: El usuario ingresa el número de días deseados. “Ejemplo: 10”
6.	Procesamiento de Reglas de Negocio: el sistema consulta de forma interna el saldo de día disponibles del empleado y evalúa si lo solicitado es menor o igual a la que tiene permitida.
7.	Fin del proceso: si tiene días suficientes el bot confirma “APROBADO” automáticamente.
Si no tiene días suficientes el notifica “RECHAZADO”. consultando la base de datos 


---

## Ejemplo de interacción

-	Usuario: vacaciones  
-	Bot: Bienvenido al sistema. Por favor ingrese su Nombre, Apellido y DNI
-	Usuario: Juan
-	Bot: Éxito. Empleado verificado: Juan ¿Cuántos días de vacaciones desea solicitar?
-	Usuario: 10
-	Bot: usted tiene 15 días disponibles. Solicitud aprobada.

