# unittest

[https://docs.python.org/3/library/unittest.html](https://docs.python.org/3/library/unittest.html)

_unittest admite la automatización de pruebas, el intercambio de código de configuración y apagado para pruebas, la agregación de pruebas en colecciones y la independencia de las pruebas del marco de informes._

_unittest contiene un marco de pruebas y un corredor de pruebas. unittest tiene algunos requisitos importantes para escribir y ejecutar pruebas:_

1. Las pruebas deben estar  dentro de clases, cada caso de prueba debe ser un método.
2. Utiliza una serie de métodos de aserción especiales en la clase **unittest.TestCase**  en lugar de la declaración assert  integrada en python.

```python
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```

_**Afirmaciones comunes**_

| Método | Equivalente a |
| ---------- | ---------- |
| assertEqual( a, b )   | a == b   |
| assertTrue( x )   | bool(x) is True   |
| assertFalse( x )   | bool(x) is False   |
| assertIs( a, b )   | a is b   |
| assertIsNone( x )   | x is None   |
| assertIn( a, b )   | a in b   |
| assertIsInstance( a, b )   | isinstance(a, b)   |

_**Nota:** assertIs(), assertIsNone(), assertIn(), Y assertIsInstance()todos tienen métodos opuestos, nombrados assertIsNot(), y así sucesivamente._

_**Corredor de pruebas**_

_La aplicación Python que ejecuta su código de prueba, verifica las aserciones y le brinda resultados de pruebas en su consola se llama **el corredor de pruebas**._

```python
if __name__ == '__main__':
    unittest.main()
```

_Este es un punto de entrada de línea de comando. Significa que si ejecuta el script solo ejecutando python `file_test.py` en la línea de comando, llamará `unittest.main()`. Esto ejecuta el corredor de pruebas al descubrir todas las clases en este archivo que heredan de `unittest.TestCase`._

_**setUp()**_

_Esto método sirve de configuración, se ejecuta antes de cada prueba, por lo que debe definir su instancia solo una vez y crearla antes de cada prueba._

```python
def setUp(self):
    self.calc = Calculate()
```

_**Interfaz de linea de comandos**_

_Correr los test desde la linea de comandos_

```python
python -m unittest tests
```

_Puede proporcionar opciones adicionales para cambiar la salida. Una de ellas es -v para verbosa. Intenta eso a continuación:_

```python
python -m unittest -v test
```

_En lugar de proporcionar el nombre de un módulo que contiene pruebas, puede solicitar un descubrimiento automático utilizando lo siguiente:_

```python
python -m unittest discover
```

_**Nota:** Esto buscará en el directorio actual cualquier archivo nombrado test*.py e intentará probarlos._

_puede proporcionar el nombre del directorio utilizando la  bandera `-s` y el nombre del directorio_

```python
python -m unittest discover -s tests
```

_si su código fuente no está en la raíz del directorio y está contenido en un subdirectorio, por ejemplo en una carpeta llamada src/, puede decir a unittest dónde ejecutar las pruebas para que pueda importar los módulos correctamente con la bandera `-s`_

```python
python -m unittest discover -s tests -t src
```

_**Nota:** unittest cambiará al src/directorio, buscará todos los  archivos `test*.py`  dentro del directorio `tests`  y los ejecutará._
