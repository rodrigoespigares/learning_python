try:
    with open('archivos_pruebas/file.txt', 'r') as f:
        contenido = f.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo no se ha encontrado")