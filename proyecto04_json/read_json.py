import json

with open('archivos_pruebas/creando.json', 'r') as f:
    prueba = json.load(f)

print(prueba)
print(json.dumps(prueba, indent=4))