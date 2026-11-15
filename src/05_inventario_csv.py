
import requests
import csv
from pathlib import Path
from getpass import getpass

baseUri = "http://localhost:58000/api/v1"

# Solicitar credenciales
usuario = input("Usuario del controlador: ")
contrasena = getpass("Contraseña del controlador: ")

# Obtener ticket
resp = requests.post(
    baseUri + "/ticket",
    json={"username": usuario, "password": contrasena}
)
resp.raise_for_status()

ticket = resp.json()["response"]["serviceTicket"]
headers = {"X-Auth-Token": ticket}

# Obtener dispositivos de red
resp = requests.get(baseUri + "/network-device", headers=headers)
resp.raise_for_status()
dispositivos = resp.json()["response"]

# Obtener hosts
resp = requests.get(baseUri + "/host", headers=headers)
resp.raise_for_status()
hosts = resp.json()["response"]

# Carpeta donde se guardarán los archivos CSV
carpeta = Path(__file__).resolve().parent.parent

# Exportar dispositivos
with open(carpeta / "inventario_dispositivos.csv", "w", newline="", encoding="utf-8-sig") as archivo:
    writer = csv.writer(archivo, delimiter=";")
    writer.writerow(["Hostname", "IP", "Modelo", "Estado"])

    for item in dispositivos:
        nombre = item.get("hostname", "ISP")
        ip = item.get("managementIpAddress", "")
        modelo = item.get("platformId", "")
        estado = item.get("inventoryStatusDetail", "")

        writer.writerow([nombre, ip, modelo, estado])

# Exportar hosts
with open(carpeta / "inventario_hosts.csv", "w", newline="", encoding="utf-8-sig") as archivo:
    writer = csv.writer(archivo, delimiter=";")
    writer.writerow(["Hostname", "IP", "Tipo", "MAC"])

    for item in hosts:
        nombre = item.get("hostName", "")
        ip = item.get("hostIp", "")
        tipo = item.get("hostType", "")
        mac = item.get("hostMac", "")

        writer.writerow([nombre, ip, tipo, mac])

print("\nInventario exportado correctamente.")
print("Dispositivos de red:", len(dispositivos))
print("Registros de hosts:", len(hosts))
print("\nArchivos generados:")
print("- inventario_dispositivos.csv")
print("- inventario_hosts.csv")
