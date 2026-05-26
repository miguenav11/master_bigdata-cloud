print("\nCLASE 2 de PYTHON")
print("27/09/2025\n")

vueltas = [1,2,3,4,5,6,7,8]
for vuelta in vueltas:
    print(f'Esta es la vuelta nº {vuelta}')

vueltas = [1,2,3,4,5,6,7,8]
contador = 1
while contador <= 5:
    print(f"Estoy en la vuelta {vueltas[contador]}")
    contador += 1


productos = [
    {"nombre": "Laptop", "categoria": "Electrónica", "precio": 799.99, "stock": 25},
    {"nombre": "Auriculares Bluetooth", "categoria": "Accesorios", "precio": 59.99, "stock": 50},
    {"nombre": "Cámara Digital", "categoria": "Fotografía", "precio": 399.99, "stock": 10},
    {"nombre": "Smartwatch", "categoria": "Relojes", "precio": 149.99, "stock": 75},
    {"nombre": "Teclado Mecánico", "categoria": "Accesorios", "precio": 89.99, "stock": 30}
]

# Muestra por consola el nombre de cada producto
for producto in productos:
    print(producto["nombre"])

# Lo mismo, pero con un while
contador = 0
while contador <= 4:
    print(productos[contador]["nombre"])
    contador += 1

# Muestra por consola el nombre de cada producto cuyo precio es mayor que 100
for producto in productos:
    if producto["precio"]>100:
        print(producto["nombre"])

# Muestra por consola el nombre de cada producto cuyo stock es menor o igual a 25
for producto in productos:
    if producto["stock"]<=25:
        print(producto["nombre"])


def saludar(nombre):
    return(f"Hola {nombre}")
print(saludar("Migue"))

def cuentaCaracteres(palabra):
    if type(palabra) != str:
        return ("Debo ser ejecutada con un string")
    else:
        return len(palabra)
print(cuentaCaracteres("Valencia"))

# Devuelve la primera letra de una palabra. Usando lambda.
primera_letra = lambda palabra : palabra[0]
print(primera_letra("hamburguesa"))

def sumar_lista(lista):
    total = 0
    for num in lista:
        total += num
    return total
numeros = [1, 2, 3, 4]
print(sumar_lista(numeros))


# DEBUG
def obtener_nombre_completo(nombre, apellido):
    if not apellido:
        return nombre
    return nombre + " " + apellido

def main():
    usuarios = [
        {"nombre": "Sofía"},
        {"nombre": "Luis", "apellido": "Martínez"},
    ]

    for usuario in usuarios:
        if not usuarios[usuario]["apellido"]:
            completo = obtener_nombre_completo(usuario["nombre"])
        completo = obtener_nombre_completo(usuario["nombre"], usuario["apellido"])
    print(completo)