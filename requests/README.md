# requests

[https://requests.readthedocs.io/es/latest/](https://requests.readthedocs.io/es/latest/)

_**Instalacion de la libreria**_

```python  
pip install requests
```

_**Realizar un petición**_

```python
import requests

url = 'http://httpbin.org/get'
response = requests.get(url)
```

_**Nota:** retorna un objeto `Response`. Podemos obtener toda la información que necesitamos a partir de este objeto._

_**Manejando la respuesta**_

_Para verificar el código de estado de la respuesta:_

```python
response = requests.get('http://httpbin.org/get')
response.status_code
# output: 200
```

_Requests también incluye un objeto para buscar estados de respuesta y pueden ser referenciados fácilmente:_

```python
response.status_code == requests.codes.ok
# output: True
```

_Una respuesta diferente a 200 puede levantar una excepción con **raise_for_status():**_

```python
response.raise_for_status()
"""
Traceback (most recent call last):
  File "requests/models.py", line 832, in raise_for_status
    raise http_error
requests.exceptions.HTTPError: 404 Client Error
"""
```

_**Nota:** `raise_for_status()` si la respuesta es 200 retorna `None`._

_**Cabeceras de respuesta**_

_Para ver las cabeceras._

```python
response.headers
"""
{
    'status': '200 OK',
    'content-encoding': 'gzip',
    'transfer-encoding': 'chunked',
    'connection': 'close',
    'server': 'nginx/1.0.4',
    'x-runtime': '148ms',
    'etag': '"e1ca502697e5c9317743dc078f67693f"',
    'content-type': 'application/json; charset=utf-8'
}
"""
```

_Es un diccionario especial: está hecho únicamente para las cabeceras HTTP. De acuerdo con el [RFC 7230](https://tools.ietf.org/html/rfc7230#section-3.2) , los nombres de las cabeceras HTTP no hacen distinción entre mayúsculas y minúsculas. Así que podemos acceder a las cabeceras utilizando letras mayúsculas o minúsculas._

```python
response.headers['Content-Type']
# output: 'application/json; charset=utf-8'

response.headers.get('content-type')
# output: 'application/json; charset=utf-8'
```

_**Cookies**_

_Si una respuesta contiene Cookies, puedes acceder a ellas rápidamente:_

```python
response.cookies['example_cookie_name']
# output: 'example_cookie_value'
```

_Para enviar tus propias cookies al servidor, puedes utilizar el parámetro `cookies`_

```python
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')

response = requests.get(url, cookies=cookies)
response.text
# output: '{"cookies": {"cookies_are": "working"}}'
```

_**Contenido de la respuesta**_

```python
import requests

url = 'http://httpbin.org/get'
response = requests.get(url)
response.text
# output: u'{\n  "args": {}, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.23.0", \n    "X-Amzn-Trace-Id": "Root=1-5e7f3030-64f1df36c00db8bc2360a396"\n  }, \n  "origin": "152.173.104.14", \n  "url": "http://httpbin.org/get"\n}\n'
```

_Requests automáticamente decodificará el contenido que viene del servidor. La mayoría de caracteres unicode serán decodificados correctamente._

_Cuando ejecutas una petición, Requests tratará de obtener la codificación de la respuesta basándose en las cabeceras HTTP. La codificación del texto que Requests halló ( o supuso ), será utilizada cuando se acceda a `response.text`. Puedes conocer la codificación que Requests está utilizando, y cambiarla, usando la propiedad `response.encoding`:_

```python
response.encoding
# output: 'utf-8'

response.encoding = 'ISO-8859-1'
```

_Si cambias la codificación, Requests utilizará este nuevo valor de `response.encoding` siempre que se invoque a `response.text`. Podrías querer hacer esto en cualquier situación donde puedas aplicar una lógica de trabajo especial para trabajar según la codificación que esté en el contenido. Por ejemplo, **HTTP** y **XML** tienen la habilidad de especificar su codificación en su cuerpo. En situaciones como esta, deberías usar `response.content` para encontrar la codificación y después configuar `response.encoding`. Esto te permitirá usar `response.text` con la codifiación correcta._

_Requests también puede utilizar codificaciones del usuario, en caso de ser necesario. Si creaste tu propia codificación, y la has registrado usando el módulo codecs, puedes asignar el nombre de este codec como valor de `response.encoding` y Requests se encargará de la decodificación._

_**Contenido binario**_

_También puedes acceder al cuerpo de la respuesta como bytes, para peticiones que no sean de texto:_

```python
response.content
# output:
```

_Las codificaciones de transferencia gzip y deflate serán decodificadas automáticamente. Por ejemplo, para crear una imagen a partir de datos binarios en una respuesta, puedes usar el siguiente código:_

```python
from PIL import Image
from StringIO import StringIO

image = Image.open(StringIO(response.content))
```

_**Contenido json**_

_También hay un decodificador de **json** incorporado en Requests, en caso de que estés trabajando con datos **json**:_

```python
response.json()
# output:
```

_Si la decodificación falla, `resonse.json()` levantará una excepción. Por ejemplo, si la respuesta obtiene un código 401 (No Autorizado/ Unauthorized), intentar `response.json()` mandará una excepción **ValueError: No JSON object could be decoded**._

_**Contenido crudo**_

_En el caso extraño que quieras obtener la respuesta en crudo a nivel socket, puedes acceder `response.raw`. Si quieres hacer esto, asegúrate de pasar `stream=True` en la petición inicial. Una vez que hagas esto, puedes hacer lo siguiente:_

```python
response = requests.get('https://github.com/timeline.json', stream=True)
response.raw
# output: <requests.packages.urllib3.response.HTTPResponse object at 0x101194810>

response.raw.read(10)
# output: '\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03'
```

_De manera general, sin embargo, deberías usar un patrón como este para guardar lo que se recibe del stream a un archivo:_

```python
with open(filename, 'wb') as fd:
    for chunk in response.iter_content(chunk_size):
        fd.write(chunk)
```

_Al usar `Response.iter_content` se manejará mucho de lo que deberías haber manipulado a mano usando `Response.raw` directamente. Lo de arriba es la forma preferida y recomendada de obtener el contenido obtenido._

_**Otras peticiones**_

_En Requests, un API simple significa que todas las formas de peticiones HTTP son obvias. Por ejemplo, así es como realizas otras peticiónes HTTP:_

```python
requests.post("http://httpbin.org/post")
requests.put("http://httpbin.org/put")
requests.delete("http://httpbin.org/delete")
requests.head("http://httpbin.org/get")
requests.options("http://httpbin.org/get")
```

_**Pasar parámetros en urls**_

_Requests te permite proveer estos argumentos en forma de diccionario, usando el parámetro en llave (keyword argument) `params`._

```python
payload = {'user': '@nelsonacos', 'dev': 'python'}
response = requests.get("http://httpbin.org/get", params=payload)
```

_Para ver la url codificada_

```python
response.url
# output: u'http://httpbin.org/get?user=@nelsonacos&dev=python'
```

_**Cabeceras personalizadas**_

_Si quieres agregar cabeceras HTTP a una petición, simplemente pasa un dict al parámetro `headers`._

```python
import json

url = 'http://httpbin.org/post'
payload = {'some': 'data'}
headers = {'content-type': 'application/json'}

response = requests.post(url, data=json.dumps(payload), headers=headers)
```

_**Peticiones de formulario html**_

_Para enviar información en forma de formulario, como un formulario HTML pasa un diccionario al argumento `data`. Este diccionario será codificado automáticamente como formulario al momento de realizar la petición._

```python
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post("http://httpbin.org/post", data=payload)
print response.text
{
  ...
  "form": {
    "key2": "value2",
    "key1": "value1"
  },
  ...
}
```

_Existen ocasiones en las que quieres enviar datos en otra codificación. Si pasas un string en vez de un dict, la información será posteada directamente._

```python
import json

url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}

response = requests.post(url, data=json.dumps(payload))
```

_**Pasar un Archivo como multipart/form-data**_

_Requests hace que sea simple subir archivos._

```python
url = 'http://httpbin.org/post'
files = {'file': open('report.xls', 'rb')}

response = requests.post(url, files=files)
response.text
{
  ...
  "files": {
    "file": "<censored...binary...data>"
  },
  ...
}
```

_Puedes establecer explícitamente el nombre del archivo, _content_type_ y encabezados:_

```python
url = 'http://httpbin.org/post'
files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}

response = requests.post(url, files=files)
response.text
{
  ...
  "files": {
    "file": "<censored...binary...data>"
  },
  ...
}
```

_Puedes enviar cadenas de caracteres para ser recibidas como archivos:_

```python
url = 'http://httpbin.org/post'
files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}

response = requests.post(url, files=files)
response.text
{
  ...
  "files": {
    "file": "some,data,to,send\\nanother,row,to,send\\n"
  },
  ...
}
```

_Si estás enviando un archivo muy largo como una petición multipart/form-data, puedes querer hacer un stream de la petición. Por defecto, requests no lo soporta, pero hay un paquete separado que sí lo hace  `requests-toolbelt`._
