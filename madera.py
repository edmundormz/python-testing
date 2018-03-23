import sys


def aserrio():
    pass


def raja():
    pass


def troncos():
    pass


def celulosas(producto, ancho, largo, alto):
    volumen = ancho * largo * alto
    if producto == "astilla":
        precio = volumen * 240
    elif producto == "aserrin":
        precio = volumen * 180
    else:
        return "Producto incorrecto"
    return volumen, precio


if __name__ == "__main__":
    producto = sys.argv[1]
    if producto == "aserrio":
        aserrio()
    elif producto == "raja":
        raja()
    elif producto == "troncos":
        troncos()
    elif producto == "celulosas":
        celulosas()