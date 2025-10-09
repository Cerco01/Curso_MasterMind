edad = int(input("Dígame su edad: "))
tipo_carnet = input("Dígame su tipo de carnet (E para Estudiante / P para Pensionista / F para Familia Numerosa / N de Ninguno: ")

if  (25 <= edad <= 35 and tipo_carnet == "E") or edad <= 10 or (edad >= 65 and tipo_carnet == "P") or (tipo_carnet == "F"):
        print("Se te aplica el 25% de descuento. ")
else:
    print("No tiene descuento. ")