import random
import string
import json

def generador(long):
    password = ""
    for i in range(long):
        aleatori = random.randint(1,3)
        if(aleatori == 1):
            point = random.choice(string.punctuation)
            if (point != "\\" and point != "\""):
                password += point
            else:
                password += "|"
        else: 
            if(aleatori == 2):
                password += random.choice(string.ascii_uppercase)
            else:
                if(aleatori == 3):
                    password += random.choice(string.ascii_lowercase)
        password = password.replace("\\", "_")
    
    return password

error=True

while error:
    cantidad = input("¿Cuantas password quieres?")
    longitud = input("¿Longitud de las contraseñas?")

    try:
        password = []
        for i in range(int(cantidad)):
            password.append(generador(int(longitud)))
        with open("archivos_pruebas/generapass.json", "w") as p:
            json.dump(password,p,indent=4)
        
        error=False

    except Exception:
        print("Ha habido un error")
        error = True