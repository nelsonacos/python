# Json en Python

Acrónimo de **J**ava**S**cript **O**bject **N**otation es un formato de texto ligero y se ha convertido en el estándar para el intercambio de información. Existe un [sitio web](https://www.json.org/) que le puede explicar todo lo relacionado al estandar [JSON](https://www.json.org/) con gran claridad por si desea profundizar.

Es extremadamente importante dominar la habilidad de trabajar con este formato ya que es uno de los mas usados y aunque existen otros formatos como [XML](https://en.wikipedia.org/wiki/XML) y [YAML](http://yaml.org/) para el intercambio de informacion hoy en dia JSON es probablemente el mas importante.

## Un poco de contexto

El proceso de codificación de JSON generalmente se llama serialización y el proceso opuesto de decodificacíon se llama deserialización. Naturalmente, la deserialización es el proceso recíproco de decodificación de datos que se ha almacenado o entregado en el estándar JSON. quizas esto no lo entiendas del todo pero es bastante sencillo solo vealo de esta manera: leer y escribir datos en formato JSON. la codificación es para escribir datos en el disco, mientras que la decodificación es para leer datos en la memoria. Lo mas probable es que queramos mover datos de aqui para alla, escribir datos con informacion relevante en un fichero JSON o realizar una consulta a la base de datos y retornar la informacion para que Javascript la procese y genere la vista de nuestra aplicacion, en cualquiera de los casos para conseguirlo con python es bastante sencillo, python acepta JSON de manera nativa y todo lo que debemos hacer es agregar esta pieza de codigo `import json` al inicio de nuestro programa para importar la [bibloteca](https://docs.python.org/3/library/json.html) que contiene los metodos prefenidos en el lenguaje para el trabajo con JSON. Todo lo que usted debe conocer son los metodos **loads()**, **load()**, **dumps()**, **dumps()** Sencillo cierto? manos a la obra!

## El ejemplo

Para iniciar nuestro trabajo con JSON tomaremos un ejemplo simple pero de la vida real, nos conectaremos a el api de [CoinMarketcap](https://api.coinmarketcap.com/v2/ticker/) para recibir datos en el formato JSON decodificaremos estos datos y los almacenaremos en un diccionario nativo de python para poder tratarlos, aplicar algunos criterio para filtrar la información, almacenaremos en un nuevo diccionario y finalmente la escribimos en un archivo JSON.

## El flujo de trabajo

- Decodificar JSON
- Tratar y procesar los datos (convertirlos en información)
- Codificar JSON Y escríbirlos en un archivo

Como puedes ver es un flujo de trabajo del mundo real bastante comun, a continuacion vamos a conectarnos al api de [CoinMarketcap](https://api.coinmarketcap.com/v2/ticker/) para ello vamos hacer uso de la bibloteca [request](http://docs.python-requests.org/es/latest/)

```python
#!/usr/bin/python3
import json
import requests

response = requests.get("https://api.coinmarketcap.com/v2/ticker/")
data = json.loads(response.text)
```

como puedes ver hemos hecho uso de la bibloteca request y su metodo get() para realizar la peticion a la api y tambien estamos haciendo uso del metodo .loads() para decodificar el JSON y manejar la response.txt y la hemos asignado a data lo que nos da como resultado un diccionario nativo de python, felicidades ahora puedes manipular estos datos a tu gusto.

A continuacion vamos a comenzar a explorar nuestro diccionario:

```python
#!/usr/bin/python3
import json
import requests

response = requests.get("https://api.coinmarketcap.com/v2/ticker/")
data = json.loads(response.text)

def keep(data):
    for i in data['data'].items():
        print(i)

keep(data)
```

Si has ejecutado el scripts te daras cuenta que la salida de un diccionario nativo de python no es lo suficientemente legible para que sea agradable. A continuacion vamos a hacer uso del metodo .dumps() de la bibloteca JSON para imprimirlo en un formato mas agradable:

```python
#!/usr/bin/python3
import json
import requests

response = requests.get("https://api.coinmarketcap.com/v2/ticker/")
data = json.loads(response.text)

def keep(data):
    for i in data['data'].items():
        print(json.dumps(i, indent=4))

keep(data)
```

Como puedes ver en esta nueva version del script ya podemos visualizar mucho mejor los datos y notaras que llegado a este punto es un poco mas complejo de iterar sobre el diccionario ya que deberiamos conocer el id de la criptomenda para seguir iterando sobre ella, pero no te asustes, python lo tiene cubierto, para desarsernos de esta complejidad vamos hacer uso del metodo .values() para iterar sobre el diccionario pero la salida nos mostrar solo los valores a continuacion:

```python
#!/usr/bin/python3
import json
import requests

response = requests.get("https://api.coinmarketcap.com/v2/ticker/")
data = json.loads(response.text)

def keep(data):
    for i in data['data'].values():
        print(json.dumps(i, indent=4))

keep(data)
```

Maravilloso, estamos listos para explorar mas a fondo este diccionario. En la nueva version que produciremos de nuestro script agregaremos un condicional que nos retornara el top10 de criptomonedas:

```python
#!/usr/bin/python3
import json
import requests

response = requests.get("https://api.coinmarketcap.com/v2/ticker/")
data = json.loads(response.text)

def keep(data):
    for i in data['data'].values():
        if i['rank'] <= 10:
            print(json.dumps(i, indent=4))

keep(data)
```

nose si lo has notado pero en este punto ya estas manipulando datos a tu gusto y convirtiendolos en informacion. Maravilloso!

Agreguemos ahora otro criterio a el condicional, por ejemplo si quisieramos solo retornar las cripto monedas que esten en el top10 pero que su precio no sobrepase los $ 500 lo hariamos de esta forma:

```python
#!/usr/bin/python3
import json
import requests

response = requests.get("https://api.coinmarketcap.com/v2/ticker/")
data = json.loads(response.text)

def keep(data):
    for i in data['data'].values():
        if i['rank'] <= 10 and 1 <= i["quotes"]["USD"]["price"] <= 500:
            print(json.dumps(i, indent=4))

keep(data)
```

Solo nos queda poder escribir los datos en un fichero JSON.

```python
import json
import requests

response = requests.get("https://api.coinmarketcap.com/v2/ticker/")
data = json.loads(response.text)
finallist=[]

def keep(data):
    for i in data['data'].values():
        if i['rank'] <= 10:
    finallist.append(i)

keep(data)

# jsondata = json.dumps(finallist)

with open('top10.json', 'w') as outfile:
json.dump(finallist, outfile)
```

Hemos cubierto todo el flujo de trabajo habitual pero tambien podemos explorar otras opciones, ya que podemos lograrlo de otras maneras. Puedes hacer uso de list comprenhension y dicts comprenhensions para lograrlo ya que es un concepto bastante poderoso y bastante eficiente en rendimiento.

Si usted quiere aprender mas sobre las lista de comprensiones y diccionarios comprensiones puede mirar este tutorial:

- [List comprenhensions](#)
- [Dicts comprenhensions](#)

De esta forma lo hariamos usando estos conceptos:

```python
import requests
response = requests.get("https://api.coinmarketcap.com/v2/ticker/")
data = json.loads(response.text)

top_10 = [i for i in data['data'].values() if i['rank'] <= 10]
with open('top10.json', 'w') as outfile:
json.dump(top_10, outfile, indent=4, separators=(',', ': '))
```

# Resumen

Hemos cubierto una gran cantidad de detalles de una manera sencilla, tambien le he dejado algunas mensiones durante lo largo del texto por si desea profundizar en algunos temas que normalmente necesitan una mayor dedicasion para entenderlo en todo caso ya estamos listo para trabajar con el estandar JSON en Python.

**Recuerde**

- Si desea Decodificar JSON provenientes de un api o de cualquier otro lugar que no implique un abrir un fichero en el disco basta con usar el metodo loads()
- Si desea Decodificar JSON proveniente de un fichero en disco basta con usar el metodo load()
- Si Desea Codificar un JSON para seguir manipulando los datos en memoria use dumps()
- Si desea Codificar JSON y escribirlo en disco use dump()
