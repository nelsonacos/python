# datetime

[https://docs.python.org/3/library/datetime.html](https://docs.python.org/3/library/datetime.html)

## datetime class

```python
from datetime import datetime

date = datetime.now()
# ouput: datetime.datetime(2020, 3, 7, 19, 45, 8, 973442)
```

_A menudo solo necesitamos una parte de ella. Podemos imprimir las diferentes partes a continuación._

```python
date.year
# ouput: 2020

date.month
# ouput: 3

date.day  # return day of month
# ouput: 7

date.hour
# ouput: 19

date.min
# ouput: datetime.datetime(1, 1, 1, 0, 0)

date.second
# ouput: 8

date.weekday()  # return day of week
# output: 

calendar.day_name[date.weekday()])
#  output:  jueves
```

### Calendario ISO

```python
date.isocalendar()  # Return a tuple with 3 elements (ISO year, ISO week number, ISO weekday).
# output: (2019, 43, 5)
```

_Como se trata de una tupla podemos acceder a sus elementos_

```python
date.isocalendar()[1]
# output: 43
```

### Unix timestamp

_El tiempo `Unix` es ampliamente utilizado en `sistemas operativos` y `formatos de archivo`. En este [sitio](https://en.wikipedia.org/wiki/Unix_time) puede aprender mas sobre el tiempo `Unix`._

#### timestamp()

```python
datetime.timestamp(date)
# output: 1572014192.8273
```

#### fromtimestamp()

```python
datetime.fromtimestamp(1572014192.8273)
# output: 2019-10-25 10: 36: 32.827300
```

### strptime(string, format)

_Puede leer cadenas con información de fecha y hora y convertirlas en objetos `datetime`. Consulte  la [documentacion](https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior) para encontrar la infromacion sobre los formatos, este [sitio](https://strftime.org/) definitivamente tambien puede ser de gran ayuda_

```python
my_string = "2020-03-07"
my_date = datetime.strptime(my_string, "%y-%m-%d")

print(my_date)
# output: 2020-03-07 00:00:00

print(type(my_date))
# output: <class 'datetime.datetime'>
```

```python
date_string = "1 August, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")

print(date_object)
# output: 2019-08-01 00:00:00
```

### strftime(format)

_convierte los objetos `datetime`  en cadenas. Una version mas agradable a la vista de los humanos este [sitio](https://strftime.org/) tambien puede ser de gran ayuda_

```python
now = datetime.now()

now.strftime("%H:%M:%S")
# output: 11:56:41

now.strftime("%m/%d/%Y, %H:%M:%S")
# output: 10/25/2019, 11:56:41
```

## timedelta class

_Un objeto timedelta  representa la cantidad de tiempo entre dos fechas u horas. Podemos usar esto para medir períodos de tiempo, o manipular fechas u horas agregando y restando de ellos, etc._

_Por defecto, un objeto timedelta tiene todos los parámetros establecidos en cero. Creemos un nuevo objeto timedelta que dure dos semanas y veamos cómo se ve:_

_Consulte la [documentacion](https://docs.python.org/2/library/datetime.html#timedelta-objects) para mas detalles_

### timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])

```python
from datetime import timedelta

d = timedelta(weeks=2)  # this object have diferences of 2 days

print(d)
# 14 días, 0:00:00
print(type(d))
# <clase 'datetime.timedelta'>
print(d.days)
# 14
```

_El menor objeto timedelta_

```python
timedelta.min  # timedelta(-999999999)
# output: -999999999 days, 0:00:00
```

_El mayor objeto timedelta_

```python
timedelta.max  # timedelta(days=999999999, hours=23, minutes=59, seconds=59, microseconds=999999)
# output: 999999999 days, 23:59:59.999999
```

_La menor diferencia posible entre no iguales_

```python
timedelta.resolution  # timedelta(microseconds=1).
# output: 0:00:00.000001
```

## timezone

_Trabajar con fechas y horas puede ser más complicado cuando las zonas horarias se involucran. Afortunadamente el modulo `pytz`  esta para ayudarnos a lidiar con las conversiones de zonas horarias cruzadas. Gracias a este modulo tenemos los objetos `timezone`. También maneja el horario de verano en lugares que lo usan._

### astimezone()

_Podemos usar la `localize()` para agregar una ubicación de zona horaria a un objeto de fecha y hora de Python. Entonces podemos usar la función `astimezone()` para convertir la zona horaria local existente en cualquier otra zona horaria que especifiquemos (toma la zona horaria que queremos convertir como argumento)._

```python
from pytz import timezone

east = timezone('US/Eastern')  # Create timezone US/Eastern
loc_dt = east.localize(datetime(2011, 11, 2, 7, 27, 0))
# output: 2011-11-02 07:27:00-04:00

kolkata = timezone("Asia/Kolkata")  # Convert localized date into Asia/Kolkata timezone
loc_dt.astimezone(kolkata)
# output: 2011-11-02 16:57:00+05:30 

au_tz = timezone('Australia/Sydney')  # Convert localized date into Australia/Sydney timezone
loc_dt.astimezone(au_tz))
# output: 2011-11-02 22:27:00+11:00
```
