import sys
import math


def aserrio(ancho, alto, largo, clase):
    """
    Calcula precio de una pieza de madera aserrada (tabla, polin, viga) de
    acuerdo a su clasificacion de calidad (primera, segunda o tercera)
    :param ancho: ancho de la pieza, en pulgadas
    :param alto: alto de la pieza, en pulgadas
    :param largo: largo de la pieza, en pies
    :param clase: calidad de la pieza (1, 2 o 3), determina el precio
    :return: string con descripcion y precio de la pieza
    """
    volumen = ancho * largo * alto / 12
    if clase == 1:
        precio = volumen * 15
    if clase == 2:
        precio = volumen * 12
    if clase == 3:
        precio = volumen * 10
    nombre = '{0} x {1} x {2} {3}a, ${4}'.format(str(ancho), str(alto),
                                                str(largo), str(clase),
                                                 str(precio))
    return nombre

def raja(ancho, largo, altos):
	"""
	Calcula el volumen de una carga de raja, promediando 3 medidas de la
	altura y usando un factor de conversion

	:param ancho: ancho de la carga, en metros
	:param largo: largo de la carga, en metros
	:param altos: lista con n alturas, en metros
	:return: tupla con volumen de carga y precio de la misma
	"""
	alto = 0
	for a in altos:
		alto += a
	alto = alto/len(altos)
	volumen = ancho * alto * largo
	precio = volumen * 0.65 * 320
	# TODO(Edmundo): fix precio to use two decimals
	return volumen, precio

def troncos(diametro, longitud, piezas=1):
	"""
	Calcula el volumen de troncos de madera
	:param diametro: diametro de la pieza, en centimetros
	:param longitud: longitud de la pieza, en metros
	:param piezas: cantidad de piezas que comparten diametro y longitud para
	calcular sus volumenes
	:return: volumen del total de troncos calculados
	"""
	radio_metros = (float(diametro)/100)/2
	area = math.pi * (radio_metros**2)
	volumen =  area * longitud * piezas
	vol_str = "{0:.3f}".format(volumen)
	return float(vol_str)


def celulosas(producto, ancho, largo, alto):
    """
    Calcula volumen y costo de cargas de productos para celulosa,
    como aserrin o astilla
    :param producto: tipo de producto [aserrin, astilla] para definir precio
    :param ancho: ancho de la carga, en metros
    :param largo: largo de la carga, en metros
    :param alto: longitud de la carga, en metros
    :return: tupla que contiene volumen calculado y precio del mismo
    """
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