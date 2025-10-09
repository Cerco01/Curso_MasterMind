x_libras = float(input("Que número de libras quieres convertir a Euros?"))
euros_redondeados = float(round(x_libras * 1.1443, 2))
print("{} libras son {} euros".format(round(x_libras, 2), euros_redondeados))