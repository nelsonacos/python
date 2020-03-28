# rounding

_Tenicas de redondeo con diferente precision. Inspirado en:_

- [Rounding](https://en.wikipedia.org/wiki/Rounding) 
- [ Lo que todo informático debe saber sobre la aritmética de punto flotante](http://perso.ens-lyon.fr/jean-michel.muller/goldberg.pdf)
- [Aritmética de coma flotante: problemas y limitaciones](https://docs.python.org/3/tutorial/floatingpoint.html)

_**truncate( n, decimals=0 )**_

_Sirve para truncar el número a un número dado de dígitos. Cuando trunca un número, reemplaza cada dígito después de una posición dada con 0._

```python
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier
```

_**round_up( n, decimals=0 )**_

_Una función especial  de techo asigna cada número a su techo. Para permitir que la función de techo acepte enteros, el techo de un entero se define como el entero mismo. Devuelve el entero más cercano que es mayor o igual a su entrada._

```python
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier
```

_**round_down( n, decimals=0 )**_

Una función especial  de piso asigna cada número a su piso. Para permitir que la función de piso acepte enteros, el piso de un entero se define como el entero mismo. Devuelve el entero más cercano que es menor o igual a su entrada._

```python
def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier
```

_**round_half_up( n, decimals=0 )**_

_Redondea cada número al número más cercano con la precisión especificada, y rompe los lazos al redondear._

```python
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier
```

_**round_half_down( n, decimals=0 )**_

_Redondea al número más cercano con la precisión deseada, al igual que el método de  **round_half_up()**, excepto que rompe los lazos al redondear al menor de los dos números._

```python
def round_half_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n*multiplier - 0.5) / multiplier
```

_**round_half_away_from_zero( n, decimals=0 )**_

_Redondea a la mitad de cero. Redondea los números de la forma en que la mayoría de las personas tienden a redondear los números en la vida cotidiana, **round_half_away_from_zero()** también elimina el sesgo de redondeo en los conjuntos de datos que tienen el mismo número de lazos positivos y negativos._

```python
def round_half_away_from_zero(n, decimals=0):
    rounded_abs = round_half_up(abs(n), decimals)
    return math.copysign(rounded_abs, n)
```
