from setuptools.command.build_ext import if_dl

f = float(input("Cuantos ºF quieres convertir a ºC?"))
c = round((f - 32)*5/9, 2)
resultado = print("{} ºF son {} ºC.".format(round(f, 2), round((f - 32)*5/9, 2)))
print("Fórmula: ({} °F − 32) × 5 / 9 = {} °C".format(round(f, 2), c))

if c >= 40:
    print("Temperatura demasiado alta para el humano.")
elif c >= 20:
    print("Que calorcito que hace :D.")
elif c >= 0:
    print("Hace fresquete.")
else:
    print("Ten cuidado, hace un frío del carajo.")
