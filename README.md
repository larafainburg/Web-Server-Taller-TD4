# Web Server - Taller TD4
Este proyecto consiste en la implementación de un pequeño **Web Server** utilizando sockets y protocolos HTTP.
El objetivo del taller es comprender cómo funciona la comunicación entre cliente y servidor a bajo nivel, manejando conexiones TCP y procesando requests HTTP manualmente.

El servidor permite:

* Abrir un socket y escuchar conexiones entrantes.
* Aceptar conexiones de clientes.
* Procesar requests HTTP `GET`.
* Enviar archivos solicitados si existen.
* Responder con errores `404 Not Found` cuando el recurso no existe.

## Tecnologías utilizadas
* Python
* Sockets
* HTTP
* Scapy (para ejercicios de análisis de paquetes)

## Cómo ejecutar

1. Clonar el repositorio:

```bash
git clone <repo-url>
```

2. Entrar al directorio:

```bash
cd <repo>
```

3. Ejecutar el servidor:

```bash
python server.py
```

4. Abrir el navegador y conectarse al puerto configurado:

```bash
http://localhost:PUERTO
```

## Ejemplo de funcionamiento

### Request

```http
GET /index.html HTTP/1.1
```

### Response exitosa

```http
HTTP/1.1 200 OK
```

### Response de error

```http
HTTP/1.1 404 Not Found
```
