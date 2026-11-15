# Entorno de virtualización Python

# Pasos de instalación en Linux:

## 1. Clonación del proyecto

Desde la terminal ejecutar:

**git clone** <URL_del_repositorio> <nombre_de_la_carpeta_de_destino>

Luego ejecutar **cd** <nombre_de_la_carpeta_de_destino>. Esta carpeta será la raíz de nuestro proyecto en Python.

## 2. Creación del entorno virtual

Supongamos que el nombre que le damos al entorno virtual es **cisco**, entonces se creará una carpeta **cisco** con todas las librerías y dependencias necesarias paea nuestro proyecto. 

La manera de realizarlo es la siguiente:

# python3 -m venv <nombre_del_entorno>
Ejemplo: python3 -m venv cisco

Para activar el entorno escribimos **source cisco/bin/activate**, en la carpeta raíz del proyecto. El nombre del entorno virtual aparecerá entre paréntesis ().

## 3. Instalación de las dependencias, en este caso las librerías requests y tabulate

En la carpeta raíz de nuestro proyecto y dentro del entorno virtual escribimos: **pip install -r requirements.txt**

## 4. Selección del intérprete Python para nuestro entorno virtual

<img width="881" height="118" alt="image" src="https://github.com/user-attachments/assets/18c41d8e-d338-48b6-953c-b2499c57319f" />

<img width="736" height="412" alt="image" src="https://github.com/user-attachments/assets/2a795fcd-2cf8-47ef-a5a6-d21e09ce967f" />

Tal como se ve en la figura seleccionamos Python 3.10.12 (cisco) que se mostrará como entorno recomendado.

## 5. Desactivación del entorno virtual

Simplemente escribimos en la línea de comandos: **deactivate**



Trabajo Práctico Integrador – Grupo 4

Este proyecto utiliza la API REST del Network Controller de Cisco Packet Tracer para consultar los dispositivos de red y los hosts de la topología del TP4.

Scripts incluidos

01_get-ticket.py: obtiene un ticket de autenticación del Network Controller.

02_get-network-device.py: consulta los dispositivos de red descubiertos.

03_get-host.py: consulta los hosts de la red.

04_tabulate.py: muestra la información de dispositivos y hosts en tablas.

05_inventario_csv.py: script desarrollado por el grupo que exporta el inventario a dos archivos CSV.

Los primeros cuatro scripts pertenecen al material de la cátedra y fueron adaptados cuando fue necesario para la topología del TP4.

Ejecución en Windows

Con Cisco Packet Tracer abierto y el acceso externo del Network Controller habilitado, ejecutar desde PowerShell:

Crear el entorno virtual:

py -m venv .venv

Instalar las dependencias:

.\.venv\Scripts\python.exe -m pip install -r requirements.txt

Ejecutar el script propio:

.\.venv\Scripts\python.exe .\src\05_inventario_csv.py

El script solicita el usuario y la contraseña del controlador al ejecutarse.

Resultados obtenidos

El inventario del TP4 contiene:

11 dispositivos de red administrados (Managed).

1 router ISP no administrado (Wrong credential).

15 registros de hosts, correspondientes a 14 hosts únicos.

Archivos generados

inventario_dispositivos.csv: nombre, IP, modelo y estado de los dispositivos.

inventario_hosts.csv: nombre, IP, tipo y dirección MAC de los hosts.

Los archivos CSV se pueden abrir con Excel.

Consideraciones

Los scripts 02_get-network-device.py y 03_get-host.py requieren un ticket de autenticación válido en el encabezado X-Auth-Token.

El script 04_tabulate.py obtiene el ticket automáticamente.

Antes de publicar el repositorio, se deben quitar las contraseñas y los tickets de autenticación escritos directamente en los archivos.