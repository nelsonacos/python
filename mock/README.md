# unittest.mock

[https://docs.python.org/3/library/unittest.mock.html](https://docs.python.org/3/library/unittest.mock.html)

_Se incluye en la bibloteca estandar a partir de Python 3.3 si esta usando una version anterior hay un [backport](https://pypi.org/project/mock/) disponible en pypi que se puede instalar con pip_

```python
pip install mock
```

_**Mock( spec=None, side_effect=None, return_value=DEFAULT, wraps=None, name=None, spec_set=None, unsafe=False, \*\*kwargs )**_

_Crea un objeto flexible para poder adaptarse a cualquier necesidad a la hora de crear objetos simulados._

```python
from unittest.mock import Mock

json = Mock()
json.dumps()
# output: <Mock name='mock.dumps()' id='4392249776'>
```

_**Nota:** nos burlarnos de la bibloteca `json` pero debemos tomar en cuenta que el metodo **dumps()** es un método simulado que no requiere argumentos. De hecho, aceptará cualquier argumento que se le pase._

_El valor de retorno de **dumps()** también es un `Mock`. La capacidad de `Mock` para definir recursivamente otros simulacros le permite usar simulacros en situaciones complejas:_

```python
json = Mock()
json.loads('{"k": "v"}').get('k')
# output: <Mock name='mock.loads().get()' id='4379599424'>
```

_**assert_called()**_

_Asegura que haya llamado al método simulado._

```python
json = Mock()
json.loads()
json.loads('{"k": "v"}')

json.loads.assert_called()
```

_**assert_called_once()**_

_Verifica que haya llamado al método exactamente una vez._

```python
json = Mock()
json.loads()

json.loads.assert_called_once()
```

_**assert_called_with( *args, \*\*kwargs )**_

_Inspecciona los argumentos pasados ​​al método simulado_

```python
json = Mock()
json.loads()
json.loads('{"k": "v"}')

json.loads.assert_called_with({"k": "v"})
```

_**assert_called_once_with( *args, \*\*kwargs )**_

_Verifica que haya llamado al método exactamente una vez e inspecciona los argumentos pasados ​​al método simulado._

```python
json = Mock()
json.loads('{"k": "v"}')

json.loads.assert_called_once_with({"k": "v"})
```

_**assert_not_called()**_

_Verifica que el metodo no haya sido llamado._

```python
json = Mock()

json.loads.assert_not_called()
```

_**call_count**_

_Un número entero que le indica cuántas veces se ha llamado al objeto simulado._

```python
json = Mock()

json.loads()
json.loads().call_count
# output: 1
```

_**call_args**_

_Esto es None (si no se ha llamado al simulacro), o los argumentos con los que se invocó el simulacro por última vez. Esto será en forma de una tupla: el primer miembro, al que también se puede acceder a través de la propiedad args, es cualquier argumento ordenado con el que se invocó el simulacro (o una tupla vacía) y el segundo miembro, al que también se puede acceder a través de propiedad kwargs, es cualquier argumento de palabra clave (o un diccionario vacío)._

```python
json = Mock()

json.loads('{"key": "value"}')
json.loads().call_args
# output: call('{"key": "value"}')
```

_**call_args_list**_

_Esta es una lista de todas las llamadas realizadas al objeto simulado en secuencia (por lo que la longitud de la lista es la cantidad de veces que se ha llamado). Antes de realizar ninguna llamada, es una lista vacía. El objeto call se puede usar para construir convenientemente listas de llamadas para comparar call_args_list._

```python
json = Mock()

json.loads('{"key": "value"}')
json.loads().call_args_list
# output: [call('{"key": "value"}')]
```

_**method_calls**_

_Además de rastrear llamadas a sí mismos, los simulacros también rastrean llamadas a métodos y atributos, y sus métodos y atributos._

```python
json = Mock()

json.loads('{"key": "value"}')
json.method_calls
# output: [call.loads('{"key": "value"}')]
```

_**return_value**_

_Establezca esto para configurar el valor devuelto llamando al simulacro._ 

```python
import datetime
from unittest.mock import Mock

# Save a couple of test days
tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)

# Mock datetime to control today's date
datetime = Mock()

def is_weekday():
    today = datetime.datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return (0 <= today.weekday() < 5)

# Mock .today() to return Tuesday
datetime.datetime.today.return_value = tuesday
# Test Tuesday is a weekday
assert is_weekday()
# Mock .today() to return Saturday
datetime.datetime.today.return_value = saturday
# Test Saturday is not a weekday
assert not is_weekday()
```

_**Nota:** existe un bibloteca [freezegun](https://github.com/spulec/freezegun) para burlarse de datetime._

_**side_effect**_

_Le permite realizar efectos secundarios, incluida una excepción cuando se llama un simulacro._

```python
import unittest
from requests.exceptions import Timeout
from unittest.mock import Mock

# Mock requests to control its behavior
requests = Mock()

def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None

class TestCalendar(unittest.TestCase):
    def test_get_holidays_timeout(self):
        # Test a connection timeout
        requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()

if __name__ == '__main__':
    unittest.main()
```

_**configure_mock( ** kwargs )**_

_Permite establecer atributos en el simulacro a través de argumentos de palabras clave._

_Los atributos más los valores de retorno y los efectos secundarios se pueden establecer en simulaciones secundarias utilizando la notación de puntos estándar y desempacando un diccionario en la llamada al método_

```python
mock = Mock()
attrs = {'method.return_value': 3, 'other.side_effect': KeyError}
mock.configure_mock(**attrs)
mock.method()
# output: 3
```

_**Nota:** configure_mock() existe para facilitar la configuración una vez que se ha creado el simulacro. Algunos atributos como `.side_effect` y `.return_value` se puede establecer cuando crear una instacion `Mock()`, otros atributos como `.name` solo se pueden establecer a través de `.__init__()`o `.configure_mock().` Si intenta establecer el `.name` en la instancia `Mock`, obtendrá un resultado no deseado._

_**patch( target , new = DEFAULT , spec = None , create = False , spec_set = None , autospec = None , new_callable = None , ** kwargs )**_

_Los decoradores de parches se usan para parchar objetos solo dentro del alcance de la función que decoran. Manejan automáticamente la eliminación de parches por usted, incluso si se generan excepciones. Todas estas funciones también se pueden usar con declaraciones o como decoradores de clase._

_patch()actúa como decorador de funciones, decorador de clases o administrador de contexto. Dentro del cuerpo de la función o con una declaración, el objetivo se parchea con un nuevo objeto. Cuando la función / con la declaración sale, el parche se deshace._

_`my_calendar.py`_

```python
import requests
from datetime import datetime

def is_weekday():
    today = datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return (0 <= today.weekday() < 5)

def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None
```

_`my_calendar_test.py`_

```python
import unittest
from my_calendar import get_holidays
from requests.exceptions import Timeout
from unittest.mock import patch

class TestCalendar(unittest.TestCase):
    @patch('my_calendar.requests')
    def test_get_holidays_timeout(self, mock_requests):
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_holidays()
                mock_requests.get.assert_called_once()

if __name__ == '__main__':
    unittest.main()
```

_**Nota:** patch() devuelve una instancia de `MagicMock`, que es una subclase de `Mock`. `MagicMock` es útil ya que implementa la mayoría de los métodos mágicos para usted, como `.__len__()`, `.__str__()` y `.__iter__()`, con valores por defecto razonables._

_**usar patch() como administrador de contexto**_

_Algunas razones por las que podría preferir un administrador de contexto incluyen las siguientes:_

- Solo desea burlarse de un objeto para una parte del alcance de la prueba.
- Ya está utilizando demasiados decoradores o parámetros, lo que perjudica la legibilidad de su prueba.

_`my_calendar_test.py`_

```python
import unittest
from my_calendar import get_holidays
from requests.exceptions import Timeout
from unittest.mock import patch

class TestCalendar(unittest.TestCase):
    def test_get_holidays_timeout(self):
        with patch('my_calendar.requests') as mock_requests:
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_holidays()
                mock_requests.get.assert_called_once()

if __name__ == '__main__':
    unittest.main()
```

_**patch.object()**_

_usando `patch.object()` puede burlarse de un método de un objeto en lugar de todo el objeto._

_`my_calendar_test.py`_

```python
import unittest
from my_calendar import requests, get_holidays
from unittest.mock import patch

class TestCalendar(unittest.TestCase):
    @patch.object(requests, 'get', side_effect=requests.exceptions.Timeout)
    def test_get_holidays_timeout(self, mock_requests):
            with self.assertRaises(requests.exceptions.Timeout):
                get_holidays()

if __name__ == '__main__':
    unittest.main()
```

_**Nota:** Cuando la prueba sale de la declaración with, **patch()** reemplaza el objeto burlado con el original._

_Además de objetos y atributos, también puedes usar patch.dict()`._

_**Problemas comunes**_

_Burlarse de objetos puede introducir varios problemas en sus pruebas. Algunos problemas son inherentes a la burla, mientras que otros son específicos unittest.mock._

_Los que se tratan aquí son similares entre sí en que el problema que causan es fundamentalmente el mismo. En cada caso, las afirmaciones de prueba son irrelevantes. Aunque la intención de cada simulacro es válida, los simulacros en sí mismos no lo son._

_**Cambios en las interfaces de objetos y errores ortográficos**_

_Las definiciones de clases y funciones cambian todo el tiempo. Cuando la interfaz de un objeto cambia, cualquier prueba que se base en un Mock de ese objeto puede ser irrelevante._

_Por ejemplo, cambia el nombre de un método pero olvida que una prueba se burla de ese método e invoca `.assert_not_called()`. Después del cambio, `.assert_not_called()` está quieto `True`. Sin embargo, la afirmación no es útil, porque el método ya no existe._

_Las pruebas irrelevantes pueden no parecer críticas, pero si son sus únicas pruebas y usted asume que funcionan correctamente, la situación podría ser desastrosa para su aplicación._

_Un problema específico de `Mock` es que una falta de ortografía puede romper una prueba. Recuerde que a `Mock` crea su interfaz cuando accede a sus miembros. Entonces, sin darse cuenta, creará un nuevo atributo si escribe mal su nombre._

Si llama a `.asert_called()` en lugar de `.assert_called()`, su prueba no elevará un `AssertionError`. Esto se debe a que ha creado un nuevo método en el objeto simulado de Python llamado `.asert_called()` en lugar de evaluar una afirmación real._

_**Detalle técnico:** Curiosamente, `assret` es un error ortográfico especial de `assert`. Si intenta acceder a un atributo que comienza con `assret` (o assert), `Mock` automáticamente elevará un `AttributeError`._

_Estos problemas ocurren cuando se burla de objetos dentro de su propia base de código. Un problema diferente surge cuando se burlan de los objetos que interactúan con bases de códigos externas._

_**Cambios a las dependencias externas**_

_Imagine nuevamente que su código hace una solicitud a una API externa. En este caso, la dependencia externa es la API que es susceptible de cambio sin su consentimiento._

_Por un lado, las pruebas unitarias prueban componentes aislados del código. Entonces, burlarse del código que hace la solicitud lo ayuda a probar sus componentes aislados en condiciones controladas. Sin embargo, también presenta un problema potencial._

_Si una dependencia externa cambia su interfaz, los objetos simulados de Python dejarán de ser válidos. Si esto sucede ( y el cambio en la interfaz no funciona ), sus pruebas pasarán porque sus objetos simulados han enmascarado el cambio, pero su código de producción fallará._

_Desafortunadamente, este no es un problema que `unittest.mock` brinde una solución. Debe ejercer su criterio cuando se burle de las dependencias externas._

_Estos tres problemas pueden causar irrelevancia en la prueba y problemas potencialmente costosos porque amenazan la integridad de sus simulacros. `unittest.mock` le brinda algunas herramientas para tratar estos problemas._

_**Evitar problemas comunes usando especificaciones**_

_Como se mencionó anteriormente, si cambia una definición de clase o función o escribe mal el atributo de un objeto simulado de Python, puede causar problemas con sus pruebas._

Estos problemas se producen porque `Mock` crea atributos y métodos cuando accede a ellos. La respuesta a estos problemas es evitar la creación de atributos `Mock` que no se ajustan al objeto que intenta burlarse._

_Al configurar una instancia `Mock`, puede pasar una especificación de objeto mediante el parametro `spec`. Acepta una lista de nombres u otro objeto y define la interfaz del simulacro. Si intenta acceder a un atributo que no pertenece a la especificación, `Mock` generará un `AttributeError`_

```python
from unittest.mock import Mock

calendar = Mock(spec=['is_weekday', 'get_holidays'])
calendar.is_weekday()
# output: <Mock name='mock.is_weekday()' id='4569015856'>

calendar.create_event()
# generated error
```

_Las especificaciones funcionan de la misma manera si configura `Mock` con un objeto_

```python
import my_calendar
from unittest.mock import Mock

calendar = Mock(spec=['is_weekday', 'get_holidays'])
calendar.is_weekday()
# output: <Mock name='mock.is_weekday()' id='4569015856'>

calendar.create_event()
# generated error
```

_unittest.mock proporciona métodos convenientes para especificar automáticamente la interfaz de una instancia `Mock`._

```python
import my_calendar
from unittest.mock import create_autospec

calendar = create_autospec(my_calendar)
calendar.is_weekday()
# output: <Mock name='mock.is_weekday()' id='4569015856'>

calendar.create_event()
# generated error
```

_Si está utilizando `patch()`, puede enviar un argumento al parámetro `autospec` para lograr el mismo resultado._

```python
import my_calendar
from unittest.mock import patch

with patch('__main__.my_calendar', autospec=True) as calendar:
    calendar.is_weekday()
    calendar.create_event()
```
