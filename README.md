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

1.	El usuario inicia la conversación escribiendo “vacaciones”. 
2.	El sistema solicita la cantidad de días a solicitar. “¿Cuántos días desea solicitar?”
3.	El usuario ingresa el número de días deseados. “Ejemplo: 10”
4.	El sistema procesa la solicitud consultando la base de datos 
5.	El chatbot responde automáticamente con el resultado:  
                    a.	Aprobado (si posee días suficientes) 
                    b.	Rechazado (si no posee días suficientes) 


---

## Ejemplo de interacción

Usuario: vacaciones  
Bot: ¿Cuántos días desea solicitar?  
Usuario: 10  
Bot: Solicitud aprobada  
