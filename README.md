# Experimentos

## Experimento 1 - Latencia en segundos servicio de Alertas

Propósito: Determinar el tiempo en segundos en que una alerta es recibida por el cliente desde que
se solicita la notificación de esta

Servicios involucrados:

- [adverse_incidents](adverse_incidents): Servicio que se encarga de procesar y enviar los incidentes adversos al
  servicio de `alertas`.
- [adverse_incidents_provider](adverse_incidents_provider): Servicio que simula la generación de incidentes adversos.
- [alerts](alerts): Servicio que se encarga de procesar, priorizar y enviar alertas a los usuarios mediante FCM (
  Firebase Cloud Messaging).
- [nutritional_plan](nutritional_plan): Servicio que se encarga de procesar y enviar notificaciones de ingesta de
  alimentos al servicio de `alertas`.
- [mobile_app](mobile_app): Aplicación móvil en React Native que recibe las alertas y las muestra al usuario.

### Objetivo

El objetivo de este experimento es:

- Simular la generación y envio de alertas a los usuarios a través de la aplicación móvil sobre incidentes adversos (en
  menos de 5 segundos)
- Simular la generación y envio de alertas a los usuarios a través de la aplicación móvil sobre la ingesta de
  alimentos (en menos de 3 segundos)

## Experimento 2 - Número de instancias requeridas en proceso de Registro de Usuarios

Propósito: Determinar el número de instancias máximas necesarias para que el servicio de registro sea capaz de procesar
hasta 1000 usuarios concurrentes registrándose al tiempo

Servicios involucrados:

- [mock](mock): Servicio que simula el comportamiento del servicio de Usuarios, registrando estos en una base de datos
  PostgreSQL.
- [experimento-2](experimento-2): Conjunto de archivos requeridos tanto por Locust como por Jmeter para realizar las
  pruebas de carga.
- [users](users): Propuesta inicial de servicio de Usuarios, se descartó debido a los problemas de rendimiento con
  procesamiento síncrono.

### Objetivo

El objetivo de este experimento es:

- Simular el registro de 1000 usuarios concurrentes en el servicio de Usuarios, determinando el número de instancias
  necesarias para que el servicio sea capaz de procesarlos en un tiempo razonable.+
