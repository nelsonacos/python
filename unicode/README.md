# Unicode  

## Python 2

_Python 2 solo tiene 2 tipos de cadena._

_**literal string**_

```python
my_string = "Hello World"

type(my_string)
# output: <type 'str'>
```

_**unicode string**_

```python
my_unicode = u"Hi \u2119\01b4\u2602\210c\xf8\u1f24"

type(my_unicode)
# output: <type 'unicode'>
```

_Las cadenas de bytes y las cadenas unicode tienen un método para convertirlo al otro tipo de cadena.__

```python
my_unicode = u"Hi \u2119\01b4\u2602\210c\xf8\u1f24"

len(my_unicode)
# output: 9
```

_Podemos  ver que tiene 9 caracteres tambien podemos codificarlo a `UTF-8` para crear una cadena de bytes._

```python
my_utf8 = my_unicode.encode("utf-8")

len(my_utf8)
# output: 19
```

_Podemos ver que tiene 19 bytes. Tambien podemos revertir la operacion decodificando la cadena `UTF-8` produciendo la cadena original unicode._

```python
my_utf8.decode("utf-8")
# output: u"Hi \u2119\01b4\u2602\210c\xf8\u1f24"
```

_La codificación y decodificación pueden producir errores si los datos no son apropiados para la codificación especificada._

```python
my_unicode.encode("ascii")
# output: raise error
```

_Intentamos codificar nuestra cadena `Unicode` a `ASCII`. Falla porque `ASCII` solo puede representar caracteres en el **rango de 0 a 127**, y nuestra cadena `Unicode` tiene puntos de código fuera de ese rango._

_La codificacion tambien puede generar problemas._

```python
my_utf8.decode("ascii")
# output: raise error

"u2119\01b4\u2602\210c\xf8\u1f24"decode("utf-8")
# output: raise error
```

_Intentamos decodificar nuestra cadena `UTF-8` como `ASCII` y obtenemos un `UnicodeDecodeError` porque `ASCII` solo puede aceptar valores de **0 hasta 127**, y nuestra cadena `UTF-8` tiene bytes fuera de ese rango._

_Al codificar o decodificar, puede especificar qué debe suceder cuando el códec no puede manejar los datos. Un segundo argumento opcional para codificar o decodificar especifica la política. El valor predeterminado es `"strict"`, lo que significa generar un error, como hemos visto._

```python
my_unicode.encode("ascii", "replace")
# output: 'Hi ??????'

my_unicode.encode("ascii", "xmlcharrefreplace")
# output: 'Hi &#8473;&#436;&#9730;&#8460;&#248;&#7972;'

my_unicode.encode("ascii", "ignore")
# output: 'Hi  '
```

_Se debe tener en cuenta que se utilizan diferentes políticas de error por diferentes razones. `replace` es un mecanismo defensivo contra datos que no se pueden interpretar y pierde información. `"Xmlcharrefreplace"` conserva toda la información original, y se utiliza al generar datos donde los escapes XML son aceptables. `ignore` simplemente ignorara los caracteres que no se puedan decodificar_

_También puede especificar el manejo de errores al decodificar. "Ignore" eliminará bytes que no pueden decodificarse correctamente._

_**Python 2** intenta ser útil cuando se trabaja con cadenas de bytes y unicode. Si intenta realizar una operación de cadena que combina una cadena unicode con una cadena de bytes, Python 2 decodificará automáticamente la cadena de bytes para producir una segunda cadena unicode, luego completará la operación con las dos cadenas unicode._

```python
u"Helllo" + "world"
# u'Hello World'

u"Hello " + ("world".decode("ascii"))
# output: u'Hello world'

sys.getdefaultencoding()
# output: 'ascii'
```

_La codificación utilizada para estas decodificaciones implícitas es el valor de `sys.getdefaultencoding()`._

_La codificación implícita es `ASCII` porque es la única suposición segura: `ASCII` es tan ampliamente aceptado y es un subconjunto de tantas codificaciones que es poco probable que produzca falsos positivos._

_**Advertencia:** no son inmunes a los errores de decodificación. Si intenta combinar una cadena de bytes con una cadena unicode y la cadena de bytes no se puede decodificar como `ASCII`, la operación generará un `UnicodeDecodeError`._

```python
u"Helllo" + my_utf8
# raise error

u"Hello " + ( my_utf8.decode("ascii") )
# raise error
```

_La filosofía de Python 2 era que las cadenas unicode y las cadenas de bytes son confusas, y trató de aliviar su carga al convertir automáticamente entre ellas, tal como lo hace para ints y flotantes. Pero la conversión de int a float no puede fallar, mientras que la cadena de bytes a cadena unicode sí._

_Hay muchas formas de combinar dos cadenas, y todas ellas decodificarán bytes a unicode, por lo que debe tener cuidado con ellas._

_Este es el hecho más importante de la vida: los `bytes` y el `Unicode` son importantes, y debe lidiar con ambos. No puede pretender que todo es `bytes` o que todo es `unicode`. Debe usar cada uno para su propósito y convertir explícitamente entre ellos según sea necesario._

## Python 3

_El mayor cambio de Python 2 a Python 3 es su tratamiento de Unicode._

_Al igual que en Python 2, Python 3 tiene solo dos tipos de cadena, uno para `unicode` y otro para `bytes`, pero se nombran de manera diferente.

_**unicode string**_

```python
my_string = "Hi \u2119\01b4\u2602\210c\xf8\u1f24"

type(my_string)
# outout: <class 'str'>
```

_**bytes string**_

```python
my_bytes = b"Hello World"

type(my_bytes)
# output: <class 'bytes'>
```

_Entonces **"str" ​​en Python 2** ahora en **Python 3 se llama "bytes"**, y** "unicode" en Python 2** ahora en **Python 3 se llama "str"**. Esto tiene más sentido que los nombres de Python 2, ya que `Unicode` es cómo desea que se almacene todo el texto, y las cadenas de `bytes` son solo cuando se trata de `bytes`._

_El mayor cambio en el soporte `Unicode` en Python 3 es que no hay decodificación automática de cadenas de `bytes`. Si intenta combinar una cadena de `bytes` con una cadena `Unicode`, ¡obtendrá un error todo el tiempo, independientemente de los datos involucrados!_

```python
"Hello" + b"world"
# output: raise error

"Hello" == b"Hello"
# output: False

d = {"Hello": "world"}

d[b"Hello"]
# output: raise error
```

_Python 2 considera una cadena `unicode` y una cadena de `bytes` igual si contienen los mismos bytes `ASCII`, y Python 3 no lo hará. Una consecuencia de esto es que las claves de diccionario `unicode` no se pueden encontrar con cadenas de `bytes`, y viceversa, como pueden estar en Python 2._

_Esto cambia drásticamente la naturaleza del dolor `Unicode` en Python 3. Porque en Python 2, la combinación de `Unicode` y `bytes` tiene éxito siempre que solo use datos `ASCII`. En Python 3, falla inmediatamente, independientemente de los datos.

_Python 3 es estricto sobre la diferencia entre bytes y unicode. Usted está obligado a ser claro en su código con el que está tratando. Esto ha sido controvertido y puede causarle dolor._

_Debido a esta nueva rigurosidad, Python 3 ha cambiado la forma de leer los archivos. Python siempre ha tenido dos modos para leer archivos: binario y texto. En Python 2, solo afectaba los finales de línea, y en plataformas Unix, incluso eso era un no-op._

_En Python 3, los dos modos producen resultados diferentes. Cuando abre un archivo en modo de texto, ya sea con "r", o por defecto por completo el modo, los datos leídos del archivo se decodifican implícitamente en Unicode, y obtiene objetos str._

_Si abre un archivo en modo binario, proporcionando "rb" como modo, entonces los datos leídos del archivo son bytes, sin procesamiento en ellos._

```python
open("hello.txt", "r").read()
# output: 'Hello world!\n'

open("hello.txt", "rb").read()
# output: b'Hello world!\n'

open("hil_utf8.txt", "r").read()
# output: 'Hi \xe2\u201e\u2122\xc6\xb4\xe2\u02dc\u201a\xe2\u201e\u0152\xc3'

open("hil_utf8.txt", "r", encoding=locale.getpreferendencodig()).read()
# output: 'Hi \xe2\u201e\u2122\xc6\xb4\xe2\u02dc\u201a\xe2\u201e\u0152\xc3'

open("hil_utf8.txt", "r", encoding="utf-8").read()
# output: 'Hi \u2119\u01b4\u2602\u210c\xf8\u1f24'

open("hil_utf8.txt", "rb").read()
# output: b'Hi \xe2\u201e\u2122\xc6\xb4\xe2\u02dc\u201a\xe2\u201e\u0152\xc3'
```

_La conversión implícita de bytes a unicode utiliza la codificación devuelta por `locale.getpreferredencoding ()`, y es posible que no le brinde los resultados que espera. Por ejemplo, cuando leemos `hi_utf8.txt`, se decodifica utilizando la codificación preferida de la configuración regional, que al momento de crear estas muestras en Windows es `"cp1252"`. Al igual que `ISO 8859-1`, `CP-1252` es un código de caracteres de un byte que aceptará cualquier valor de byte, por lo que nunca generará un `UnicodeDecodeError`. Eso también significa que felizmente decodificará datos que no son realmente `CP-1252`, y producirá basura._

_Para que el archivo se lea correctamente, debe especificar una codificación para usar. La función open () ahora tiene un parámetro de codificación opcional._

_Los datos que entran y salen de su programa deben ser `bytes`. Pero no necesita lidiar con `bytes` en el interior de su programa. La mejor estrategia es decodificar `bytes` entrantes lo antes posible, produciendo `unicode`. Utiliza `unicode` en todo el programa y luego, al generar datos, codifíquelo en `bytes` lo más tarde posible._

_Esto crea un `sandwich Unicode`: `bytes` en el exterior, `Unicode` en el interior._

_Tenga en cuenta que a veces, una biblioteca que está utilizando puede hacer algunas de estas conversiones por usted. La biblioteca puede presentarle la entrada `Unicode`, o aceptará `Unicode` para la salida, y la biblioteca se encargará de la conversión del borde hacia y desde los `bytes`. Por ejemplo, **Django proporciona Unicode, al igual que el módulo json**._

_Al depurar su código, no puede simplemente imprimir un valor para ver qué es. Debe mirar el tipo, y puede que necesite mirar la repr del valor para llegar al fondo de los datos que tiene._

## Repaso

1. Todas las entradas y salidas de su programa son bytes.
2. El mundo necesita más de 256 símbolos para comunicar texto.
3. Su programa tiene que lidiar con bytes y Unicode.
4. Una secuencia de bytes no puede decirle su codificación.
5. Las especificaciones de codificación pueden estar equivocadas.

## Consejos

1. **Sandwich Unicode:** mantenga todo el texto en su programa como Unicode y conviértalo lo más cerca posible de los bordes.
2. Sepa cuáles son sus cadenas: debe poder explicar cuáles de sus cadenas son Unicode, cuáles son bytes y, para sus cadenas de bytes, qué codificación utilizan.
3. Pon a prueba tu soporte Unicode. Use cadenas exóticas en todas las suites de prueba para asegurarse de que cubre todos los casos.

**Nota:** Si sigues estos consejos, escribirás un buen código sólido que se adapte bien a Unicode, y no se caerá sin importar cuán salvaje sea el Unicode que encuentre.
