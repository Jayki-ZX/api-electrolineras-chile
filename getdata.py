from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pprint import pprint

# todo hacerle un env + requirements
# Por ahora getdata hace lo siguiente
# - Simula una conexion a la pagina del mapa.
# - Saca los datos ejecutando el comando return JSON.parse(window._pageData)[1][6][i][12][0][13][0] en la consola del navegador.
# Donde "i" representa el numero de agrupación (limite de kW, AC/DC) asignado por enel (rojo = 0, morado = 1, verde = 2)
# - Guarda el resultado del paso anterior en una lista de python.

# selenium hace los siguientes parse
# Los null de js pasan a None de python
# Los true/false de js pasan a True/False de python

options = webdriver.ChromeOptions()

options.add_argument('headless')

browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

url = "https://www.google.com/maps/d/u/0/embed?mid=1WJH79QSYNRlQIBrkhFB8OQxXpDFG6L0q"
browser.get(url)

# _pageData[1][6][0][12][0][13][0]
# _pageData[1][6][1][12][0][13][0]
# _pageData[1][6][2][12][0][13][0]

a = browser.execute_script("return JSON.parse(window._pageData)[1][6][0][12][0][13][0]")
#b = browser.execute_script("return JSON.parse(window._pageData)[1][6][1][12][0][13][0]")
#c = browser.execute_script("return JSON.parse(window._pageData)[1][6][2][12][0][13][0]")
#print(type(a))
#print(a)
pprint(a)

#  [ID -> str,
#   [[[latitude -> float, long -> float]]],
#   [],
#   [],
#   Unknown -> num,
#   [['Nombre Punto de Carga' -> Fixed str, [Name -> str], Unknown -> nu,],
#    None -> Unknown (None),
#    [],
#    [['Dirección' -> Fixed str,
#      [Google Maps address -> str],
#      Unknown -> num],
#     ['Carga Simultanea' -> Fixed str, [None, None, 1], 3],
#     ['Potencia por toma (kW) -> Fixed str', [None, None, 50], 3],
#     ['Modelo Cargador' -> Fixed str, ['JuicePump Enel X'], 1],
#     ['Tipo Conexión' -> Fixed str, ['Tri-estándar'], 1],
#     ['Contacto' -> Fixed str, ['movilidad.electrica@enel.com'], 1]]],
#   None,
#   3]]