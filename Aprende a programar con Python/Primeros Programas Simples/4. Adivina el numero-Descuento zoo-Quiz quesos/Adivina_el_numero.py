import random


print("Vamos a jugar a... ¡ADIVINA EL NUMERO! ")

numero_ganador = random.randint(1, 10)
numero_elegido = int(input("Por favor, elija un número entre el 1 y el 10. --> "))

if numero_elegido > 10:
    print("Ha perdido su intento. Se ha pasado... Era entre 1 y 10. ")

if numero_elegido < 1:
    print("Ha perdido su intento. Se ha quedado corto... Era entre 1 y 10. ")

if numero_elegido == numero_ganador:
    print("¡Enhorabuena! ¡Tenía un 10% de probabilidad de acertar! ¡El {} es el número ganador!".format(numero_ganador))

elif abs(numero_elegido - numero_ganador) == 1:
    print("¡Se ha quedado realmente cerca! Una pena que solo tuviera una oportunidad... Se ha perdido el viaje a Bali"
                                     " gratis para 2 personas. :S ¡El {} es el número ganador!".format(numero_ganador))
else :
    print("Una pena que solo tuviera una oportunidad... Se ha perdido el viaje gratis a Bali para 2 personas. "
                                                              ":S ¡El {} es el número ganador!".format(numero_ganador))