print("\nCLASE 1 de PYTHON")
print("26/09/2025\n")

# Esto me mostrará por consola el mensaje: Hola mundo
print("Hola mundo")

nombre = "Miguel Ángel"
apellido = "Navarro"

print(f"Soy {nombre} y mi apellido es {apellido}")

edad = 23
ciudad = "Valencia"
tengo_carnet = True

print(f"Tengo {edad} años, soy de {ciudad}. Es {tengo_carnet} que tengo el carnet de conducir")

print(f"{nombre.upper()} {apellido.lower()}")
print(f"Mi nombre tiene {len(nombre)} caracteres")
print(f"La primera letra de mi nombre es {nombre[0]}")
print(f"La última letra de mi apellido es {apellido[-1]}")

diccionario = {
    "nombre" : "Miguel Ángel",
    "apellido" : "Navarro",
    "ciudad" : "Valencia",
    "solterx" : False
}

print(diccionario["nombre"])

lista_compra = ["pan", "leche", "huevos"]
lista_compra.append("frutas")
lista_compra.insert(1, "verduras")
print(lista_compra)
lista_compra.pop(-1)
print(lista_compra)

culpable = True
if culpable == True:
    print("Es culpable")
else:
    print("No es culpable")


persona = {
	"nombre": "Sofía",
	"edad": 27,
	"altura": 1.70,
	"hobbies": ["tenis", "fútbol"]
}

if type(persona) == dict:
	print("apruebas 1")
else:
	print("suspendes 1")

if persona["nombre"] == "Sofía":
	print("apruebas 2")
else:
	print("suspendes 2")

if persona["edad"] >= 18:
	print("apruebas 3")
else:
	print("suspendes 3")

if type(persona["altura"])== float:
	print("apruebas 4")
else:
	print("suspendes 4")

if persona["hobbies"][1] == "fútbol":
	print("apruebas 5")
else:
	print("suspendes 5")


pruebaDicc = {
    "x": 7,
	"y": "hola",
	"a": {"b": 3},
	"z": [1, 2, "josue"]
}

if type(pruebaDicc) == dict:
	print("apruebas 1")
else:
	print("suspendes 1")

if pruebaDicc["x"] == 7:
	print("apruebas 2")
else:
	print("suspendes 2")

if pruebaDicc["y"] == "hola":
	print("apruebas 3")
else:
	print("suspendes 3")

if pruebaDicc["a"]["b"] == 3:
	print("apruebas 4")
else:
	print("suspendes 4")

if pruebaDicc["z"][1] == 2:
	print("apruebas 5")
else:
	print("suspendes 5")

if type(pruebaDicc["z"][2]) == str:
	print("apruebas 6")
else:
	print("suspendes 6")