print("CLASE 3 - PYTHON, 10/10/2025")

lista_edades = [15, 22, 17, 30, 65, 45, 70, 19]
for edad in lista_edades:
    if edad >= 65:
        break
    elif edad > 18:
        print(edad)

intentos = 0
while intentos < 5: # El usuario tiene 5 intentos
    entrada = input("Introduzca un número: ")
    try:
        numero = int(entrada)
        print("El número es válido.")
        break
    except:
        print("No es válido")
    intentos += 1



print("PROGRAMACIÓN ORIENTADA A OBJETOS (PPO)")

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def hacer_sonido(self):
        print("El animal hace un sonido genérico.")

mi_animal = Animal("Tana", 8)
print(f"Mi animal se llama {mi_animal.nombre} y tiene {mi_animal.edad} años.")
mi_animal.hacer_sonido()


class Empleado:
    sueldo_base = 50000
    def __init__(self, nombre, cargo):
        self.nombre = nombre
        self.cargo = cargo
    @classmethod    # se aplica a toda la clase
    def aumentar_sueldo_base(cls, porcentaje):  # pongo 'cls' en lugar de 'self'
        cls.porcentaje = porcentaje
        cls.sueldo_base *= (1 + porcentaje/100)
        cls.sueldo_base = round(cls.sueldo_base) # Lo redondeo para que no me de decimales
        print("El nuevo sueldo base es: {cls.sueldo_base}")

empleado1 = Empleado("Benito", "Gerente")
print(f"Sueldo de {empleado1.nombre}: {Empleado.sueldo_base}")

Empleado.aumentar_sueldo_base(10) # Aumento el sueldo un 10% a toda la clase
empleado2 = Empleado("Juan", "Peón")
print(f"Sueldo de {empleado2.nombre}: {Empleado.sueldo_base}")


class Matematica:
    @staticmethod
    def sumar(a, b):
        return a + b
    @staticmethod
    def restar(a, b):
        return a - b
    @staticmethod
    def multiplicar(a, b):
        return a * b
print(Matematica.sumar(2, 4))


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def mostrarDetalles(self):
        print(f"El precio del producto '{self.nombre}' es de {self.precio} €")

producto1 = Producto("tijeras", 7)
producto2 = Producto("boli", 2)
Producto.mostrarDetalles(producto1)
Producto.mostrarDetalles(producto2)


class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    def hacer_sonido(self):
        print("El animal hace un sonido genérico.")

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre) # Llama al atributo de la Clase Padre y lo hereda la Clase Hija
        self.raza = raza # Crea un nuevo atributo para la Clase Hija
    def hacer_sonido(self):
        # super().hacer_sonido()    # Extensión de un módulo    (lo hereda de la Clase Padre)
        print("El perro ladra: ¡Guau!")   # sobrescritura o overriding del método (lo cambio para esta Clase Hija)
        
animal_generico = Animal("Boby")
animal_generico.hacer_sonido()

mi_perro = Perro("Tana", "Bichón maltés")
print(f"Mi perro se llama {mi_perro.nombre} y es un {mi_perro.raza}")
mi_perro.hacer_sonido()


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def mostrarDetalles(self):
        print(f"El precio del producto '{self.nombre}' es de {self.precio} €")

class Electrodomestico(Producto):
    def __init__(self, nombre, precio, marca):
        super().__init__(nombre, precio)
        self.marca = marca
    def mostrarDetalles(self):
        print(f"El precio de '{self.nombre}' de la marca '{self.marca}' es de {self.precio} €")
    def encender():
        print("Encendiendo...")

producto1 = Producto("tijeras", 7)
producto2 = Producto("boli", 2)
Producto.mostrarDetalles(producto1)
Producto.mostrarDetalles(producto2)
mielectro = Electrodomestico("nevera", 500, "Bosch")
mielectro.mostrarDetalles()



import mismodulos.matematicas as matematicas

resultado_suma = matematicas.sumar(5, 3)
print(f"La suma es: {resultado_suma}")

resultado_resta = matematicas.restar(5, 3)
print(f"La resta es: {resultado_resta}")

print(f"El valor de PI es: {matematicas.PI}")


from mismodulos.matematicas import sumar, PI

print(sumar(8, 2))
print(PI)



import mismodulos.saludos as saludos # Importar el módulo saludos.
saludos.saludar("Migue") # Llamar a la función saludar() con tu nombre.
saludos.despedir("Pepito") # Llamar a la función despedir() con otro nombre.

print(saludos.saludar("Migue")) # Muestra los resultados por consola.
print(saludos.despedir("Pepito"))



import math
print(math.pi)