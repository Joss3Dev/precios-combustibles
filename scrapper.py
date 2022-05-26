import pymongo 
from urllib.request import Request, urlopen
import json
from datetime import datetime

# Creacion del cliente de MongoDB, base de datos y la coleccion de datos
cliente = pymongo.MongoClient('mongodb://localhost:27017/')
db = cliente["Datos"] 
col = db["combustibles"]

# Se extraen los datos de la pagina http://gis.mic.gov.py/visor/#/sales
# Se obtienen los precios de los combustibles con los nombres de los emblemas con sus abreviaciones
r = Request(
	'http://gis.mic.gov.py/api/sales/by_price',
	headers={'User-Agent': 'Mozilla/5.0'}
)
respuesta = urlopen(r)
datos = json.load(respuesta)
precios = datos['data']
emblemas = datos['emblema']
filas = datos['rows']
cols = datos['columns']

# Se obtiene el nombre de los productos con sus abreviaciones
r_productos = urlopen(Request(
	'http://gis.mic.gov.py/api/sales/by_product/2022',
	headers={'User-Agent': 'Mozilla/5.0'}
))
productos = json.load(r_productos)['producto']

# Se transforma de la abreviacion al nombre completo del producto
for i in range(len(filas)):
	filas[i] = productos[filas[i]]

# Se transforma de la abreviacion al nombre completo del emblema
for i in range(len(cols)):
	cols[i] = emblemas[cols[i]]

# Se cargan los precios con sus productos a una lista donde el primer for recorre las filas y el segundo for recorre
# los precios por cada emblema creando un diccionario por cada precio.
a_guardar = []

for i, fila in enumerate(precios):
	for j, precio in enumerate(fila):
		dato = {
			'emblema': cols[j],
			'captura': datetime.now(),
			'producto': filas[i],
			'precio': precio
		}
		a_guardar.append(dato)

# Una vez se cargaron todos los precios a la lista se guardan en la base de datos conectada anteriormente
datos_insertados = col.insert_many(a_guardar)

# Finalmente se imprimen los objetos guardados en base de datos
print('Los siguientes precios de combustibles fueron agregados:')
for doc in col.find():
	print(doc)
