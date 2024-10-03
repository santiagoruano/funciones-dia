# Ejemplo para calcular el area del triangulo


#Variables de entrada
base = int(input("Ingrese la base: "))
altura = int(input("Ingrese la altura: "))

#Proceso
def calcularAreaTriangulo(b,a):
    area = (b*a)/2
    return area

#Invocar la funcion
resultado = calcularAreaTriangulo(base,altura)
print(f"El area del triangulo cuya base {base}y altura {altura}es: {resultado}")

#funcion con argumentos predeterminados
def my_function(country = "Colombia"):
    print("I am from "+country)
my_function()
my_function("Sweden")

import math

num3 = math.ceil()











