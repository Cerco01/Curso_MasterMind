so = input("¿Que SO prefieres? \n"
            "1 - Android\n"
            "2 - iOS\n")

if so == "1":


    money = input("Tienes dinero? \n"
                      "S para Si\n"
                        "N para No.")
    if money == "S":
        camara_android = input("Te importa la cámara del móvil?\n"
                                       "S para Si. \n"
                                       "N para No.")
        if camara_android == "S":
            print("Google Pixel Supercamar")
        elif camara_android == "N":
            print("Android calidad-precio")
    elif money == "N":
        print("Android Chino 100€")


elif so == "2":


    dinero = input("Tienes dinero?\n"
                       "S para Si. \n"
                       "N para No")
    if dinero == "S":
        print("iPhone Ultra Pro Max")
    elif dinero == "N":
        print("iPhone segunda mano")
