

#Esto es la impresión de un print repetido el número de veces que se selecciona en el input.
numero_de_repeticiones = int(input("¿Cuantas veces quieres repetir el mensaje?"))
for a in range(numero_de_repeticiones):
    print("hola")
#Repite "hola" input(x) veces.


#Esto es un intervalo de números.
print(range(4))
#range(0, 4)
#Sería equivalente a poner for a in range(0, 4):


#Eto es una lista de números. Convierte el rango de números en una lista.
print(list(range(4)))
#[0, 1, 2, 3]
#Sería equivalente a poner for a in [0, 1, 2, 3]: