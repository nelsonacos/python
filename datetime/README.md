# datetime

[https://docs.python.org/3/library/datetime.html](https://docs.python.org/3/library/datetime.html)

Esta  hoja de trucos  cubre las funciones relacionadas con la fecha y hora más utilizadas en Python. 

- Fecha y hora de hoy en diferentes formatos.
- Conversión de cadena a fecha
- Diferencia en el cálculo de fecha y hora
- Fecha y hora más / menos cierto período de tiempo
- Comparación de fecha y hora

```python
from datetime import datetime

date = datetime.now()
# ouput: datetime.datetime(2020, 3, 7, 19, 45, 8, 973442)
```

A menudo solo necesitamos una parte de ella. Podemos imprimir las diferentes partes a continuación.

```python
date.year
# ouput: 2020

date.month
# ouput: 3

date.day
# ouput: 7 

date.hour
# ouput: 19

date.min
# ouput: datetime.datetime(1, 1, 1, 0, 0)

date.second
# ouput: 8

```
