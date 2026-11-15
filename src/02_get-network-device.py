import json
import requests
api_url = "http://localhost:58000/api/v1/network-device"

headers={"X-Auth-Token": "NC-2-a5a2460f39b3488391bf-nbi"}

resp = requests.get(api_url, headers=headers)

print("Request status: ", resp.status_code)

response_json = resp.json()
print()
print()
print (response_json)
print()
print()
networkDevices = response_json["response"]

for networkDevice in networkDevices:
    print(
        networkDevice.get("hostname", "Sin hostname"),
        networkDevice.get("managementIpAddress", "Sin IP"),
        networkDevice.get("inventoryStatusDetail", "Sin estado")
    )
