titulo = "Lista de la compra: \n"
lista_compra = []
anhadir_algo_mas = "S"
quitar_algo = None
input_de_usuario = None

print(titulo + "-" * len(titulo) + "\n")


while anhadir_algo_mas == "S":

    opcion = input("¿Que desea hacer con su lista de la compra?\n"
                   "Puede [A]ñadir o [R]etirar un producto. ([Q] para salir) > ").upper()

    if opcion == "Q":
        input("Enter para cerrar.")
        exit()

    elif opcion == "A":


        while True:

            input_de_usuario = input("¿Que desea añadir a la lista de la compra? > ")
            if input_de_usuario in lista_compra:
                print(f"{input_de_usuario} ya está en la lista.")

            else:
                if input(f"¿Seguro que quiere añadir {input_de_usuario}? [S/N] > ").upper() == "S":
                    lista_compra.append(input_de_usuario)
                    print(f"¡{input_de_usuario} añadido!")
                    print("Lista de la compra:")
                    print(lista_compra)
                    break


    elif opcion == "R":

        retirar_producto = input("¿Que producto desea retirar? ([Q] para salir) > ").upper()

        if retirar_producto == "Q":
            input("Enter para cerrar.")
            exit()

        elif retirar_producto in lista_compra:

                if input(f"¿Seguro que quiere retirar {retirar_producto}? [S/N] > ").upper() == "S":
                    lista_compra.remove(retirar_producto)
                    print(f"¡{retirar_producto} eliminado!")
                    print("Lista de la compra:")
                    print(lista_compra)

        else:
            print(f"{retirar_producto} no está en la lista.")


    anhadir_algo_mas = input("Desea añadir o retirar otro producto? [S/N] > ").upper()
    if anhadir_algo_mas == "N":
        input("Enter para cerrar.")
        exit()