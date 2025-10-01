import os

titulo = "Lista de la compra: \n"
lista_compra = []

def limpiar_pantalla():
    # 'nt' es para Windows, 'posix' para Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')



while True:

    limpiar_pantalla()

    print(titulo + "-" * len(titulo) + "\n")

    opcion = input("\n¿Que desea hacer con su lista de la compra?\n"
                   "Puede [A]ñadir o [R]etirar un producto. ([Q] para salir) > ").upper()

    if opcion == "Q":
        for item in lista_compra:
            print(item)
        input("Enter para cerrar.")
        exit()

    elif opcion == "A":


        while True:

            input_de_usuario = input("\n¿Que desea añadir a la lista de la compra? > ")
            if input_de_usuario in lista_compra:
                print(f"\n{input_de_usuario} ya está en la lista.")

            else:
                if input(f"\n¿Seguro que quiere añadir {input_de_usuario}? [S/N] > ").upper() == "S":
                    lista_compra.append(input_de_usuario)
                    print(f"\n¡{input_de_usuario} añadido/a!")
                    print("\nLista de la compra:\n")
                    for item in lista_compra:
                        print(item)
                    input("\nEnter para continuar.")
                    break


    elif opcion == "R":

        retirar_producto = input("\n¿Que producto desea retirar? ([Q] para salir) > ")

        if retirar_producto == "Q":
            input("\nEnter para cerrar.")
            exit()

        elif retirar_producto in lista_compra:

            confirmacion = input(f"\n¿Seguro que quiere retirar {retirar_producto}? [S/N] > ").upper()
            if confirmacion == "S":
                lista_compra.remove(retirar_producto)
                print(f"\n¡{retirar_producto} eliminado!")
                print("\nLista de la compra:\n")
                for item in lista_compra:
                    print(item)
                input("\nEnter para continuar.")


        else:

            print(f"\n{retirar_producto} no está en la lista.")
            print("\nLista actual:\n")
            for item in lista_compra:
                print(item)
            input("Enter para continuar.")