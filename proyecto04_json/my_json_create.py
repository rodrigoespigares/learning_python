import json


asd = 2
d = {
    "prueba": "hola",
    "pan" : asd,
}

with open('archivos_pruebas/creando.json', 'w') as f:
    json.dump(d,f,indent=4)
