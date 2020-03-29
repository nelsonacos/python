# statistics

[https://docs.python.org/3/library/statistics.html](https://docs.python.org/3/library/statistics.html)

_**mean( x )**_

_Calcula la **media muestral** , también llamada **media aritmética muestral** o simplemente el **promedio** , es el promedio aritmético de todos los elementos en un conjunto de datos. La **media** de un conjunto de datos **𝑥** se expresa matemáticamente como **Σᵢ𝑥ᵢ / 𝑛,** donde **𝑖 = 1, 2, ..., 𝑛**. En otras palabras, es la suma de todos los elementos **𝑥ᵢ** dividido por el número de elementos en el conjunto de datos **𝑥**._

```python
import statistics
import math

x = [8.0, 1, 2.5, 4, 28.0]
mean_ = statistics.mean(x)
# output: 8.7

x_with_nan = [8.0, 1, 2.5, math.nan, 4, 28.0]
mean_ = statistics.mean(x_with_nan)
# output: nan
```

_**Nota:** si hay  valores **nan** entre sus datos, entonces retorna **nan**. Esto funciona de manera similiar si calcula el **promedio** usando python puro `sum(x) / len(x)`._

_**fmean( x )**_

_Se presenta en Python **3.8** como una alternativa más rápida a **mean()**. Siempre devuelve un número de coma flotante._

```python
import statistics
import math

x = [8.0, 1, 2.5, 4, 28.0]
mean_ = statistics.fmean(x)
# output: 8.7

x_with_nan = [8.0, 1, 2.5, math.nan, 4, 28.0]
mean_ = statistics.fmean(x_with_nan)
# output: nan
```

_**weighted_mean( x, w )**_

_Calcula la **media ponderada** , también llamada **media aritmética ponderada** o **promedio ponderado** , es una generalización de la **media aritmética** que le permite definir la contribución relativa de cada punto de datos al resultado._

_La media ponderada es muy útil cuando necesita la media de un conjunto de datos que contiene elementos que ocurren con frecuencias relativas dadas. Con este método, no necesita saber la cantidad total de elementos._

_Esta libreria no calcula la **weighted_mean( )** pero puede implementar la media ponderada en Python puro combinando **sum()** con **range()** o **zip()**:_

```python
x = [8.0, 1, 2.5, 4, 28.0]
w = [0.1, 0.2, 0.3, 0.25, 0.15]

wmean = sum(w[i] * x[i] for i in range(len(x))) / sum(w)
# output: 6.95

wmean = sum(x_ * w_ for (x_, w_) in zip(x, w)) / sum(w)
# output: 6.95
```

_**harmonic_mean( x )**_

_Calcula la **media armónica** es el recíproco de la media de los recíprocos de todos los elementos en el conjunto de datos: **𝑛 / Σᵢ (1 / 𝑥ᵢ)**, donde **𝑖 = 1, 2, ..., 𝑛** y **𝑛** es el número de elementos en el conjunto de datos **𝑥**. Una variante de la implementación pura de Python de la media armónica es esta:_

```python
import statistics

x = [8.0, 1, 2.5, 4, 28.0]
hmean = statistics.harmonic_mean(x)
# output: 2.7613412228796843
```

_Es bastante diferente del valor de la **media aritmética** para el mismo conjunto de datos, que calculó en **8.7**. Esto se comporta de manera similar a calcular con python puro `len(x) / sum(1 / item for item in x)`._

_**Nota:** si tiene un **nan** valor en un conjunto de datos, retorna **nan**. Si hay al menos un **0**, entonces retorna **0**. Si proporciona al menos un número negativo, obtendrá `StatisticsError`_

_**geometric_mean( x )**_

_Calcula la **media geométrica** es la raíz **𝑛-ésima** del producto de todos los **𝑛** elementos **𝑥ᵢ** en un conjunto de datos **𝑥: ⁿ√ (Πᵢ𝑥ᵢ)**, donde **𝑖 = 1, 2, ..., 𝑛**._

```python
import statistics

x = [8.0, 1, 2.5, 4, 28.0]
gmean = statistics.geometric_mean(x)
# output: 4.67788567485604
```

_**Nota:** Si pasa datos con valores **nan**, se comportará como la mayoría de las funciones similares y retornara **nan**. Si hay un número cero o negativo entre sus datos, entonces retornara `StatisticsError`._

_Puede implementar la media geométrica en Python puro de esta manera:_

```python
gmean = 1
for item in x:
    gmean *= item

gmean **= 1 / len(x)
```

_**median( x )**_

_Calcula la **mediana de muestra** es el elemento medio de un conjunto de datos ordenado. El conjunto de datos se puede ordenar en orden creciente o decreciente. Si el número de elementos **𝑛** del conjunto de datos es **impar**, entonces la mediana es el valor en la posición media: **0.5 (𝑛 + 1)**. Si **𝑛** es **par**, entonces la mediana es la **media aritmética** de los dos valores en el medio, es decir, los elementos en las posiciones **0.5𝑛** y **0.5𝑛 + 1**._

_**ej:** si tiene los puntos de datos **2, 4, 1, 8 y 9**, entonces el valor medio es **4**, que se encuentra en el medio del conjunto de datos ordenados **(1, 2, 4, 8, 9)**. Si los puntos de datos son **2, 4, 1 y 8**, entonces la mediana es **3**, que es el promedio de los dos elementos intermedios de la secuencia ordenada **(2 y 4)**._

```python
import statistics

x = [2, 4, 1, 8 , 9]
median_ = statistics.median(x)
# output: 4

x = [2, 4, 1, 8 , 9]
median_ = statistics.median(x[:-1])
# output: 3.25
```

_**Nota:** A diferencia de la mayoría de las otras funciones no retornan **nan** cuando hay valores **nan**  entre los puntos de datos_

_Para implementar con python puro debe tener en cuenta lo siguiente:_

1. **Ordenar** los elementos del conjunto de datos
2. **Encontrar** los elementos intermedios en el conjunto de datos ordenados

```python
n = len(x)
if n % 2:
    median_ = sorted(x)[round(0.5*(n-1))]
else:
    x_ord, index = sorted(x), round(0.5 * n)
    median_ = 0.5 * (x_ord[index-1] + x_ord[index])
```

_**median_low( x )**_

_Esta relacionada con la **mediana** Siempre retorna un elemento del conjunto de datos:_ 

- _Si el número de elementos es **impar** , entonces hay un único valor medio, por lo que se comportan de la misma manera que **median()**._

- _Si el número de elementos es **par** , entonces hay dos valores medios. En este caso, **median_low()** retorna el valor medio más bajo._

```python
import statistics

x = [2, 4, 1, 8 , 9]
statistics.median_low(x)
# output: 4

x = [2, 4, 1, 8 , 9]
statistics.median_low(x[:-1])
# output: 2
```

_**Nota:** se comporta de manera similar a **mediam()** no retornan **nan** cuando hay valores **nan** entre los puntos de datos._

_**median_high( x )**_

_Esta relacionada con la **mediana** Siempre retorna un elemento del conjunto de datos:_ 

- _Si el número de elementos es **impar** , entonces hay un único valor medio, por lo que se comportan de la misma manera que **median()**._

- _Si el número de elementos es **par** , entonces hay dos valores medios. En este caso, **median_high()** retorna el valor medio más alto._

```python
import statistics

x = [2, 4, 1, 8 , 9]
statistics.median_high(x)
# output: 4

x = [2, 4, 1, 8 , 9]
statistics.median_high(x[:-1])
# output: 4
```

_**Nota:** se comporta de manera similar a **mediam()** no retornan **nan** cuando hay valores **nan** entre los puntos de datos._

_**mode( x )**_

_Calcula el **modo de muestra** es el valor en el conjunto de datos que ocurre con mayor frecuencia. **Si no hay un solo valor**, el conjunto es **multimodal** ya que tiene múltiples valores modales._

_**ej:** en el conjunto que contiene los puntos **2, 3, 2, 8 y 12**, el número **2** es **el modo** porque ocurre dos veces, a diferencia de los otros elementos que ocurren solo una vez._

```python
import statistics

x = [2, 3, 2, 8, 12]
mode_ = statistics.mode(x)
# output: 2
```

_**Nota:** si hay más de un valor modal, entonces **mode()** retorna `StatisticsError`. Maneja valores **nan**  como valores regulares y puede retornar **nan** como el valor modal._

_Una implementacion de python puro `max((u.count(item), item) for item in set(u))[1]`._

_**multimode( x )**_

_Calcula el  conjunto de valores que ocurre con mayor frecuencia. Es util cuando el conjunto es **multimodal** ya que tiene múltiples valores modales._

_**ej:** en el conjunto que contiene los puntos **2, 3, 2, 8, 12, 45 y 8**, el conjunto de valores es **[ 2, 8]** es **el modo** porque ocurren con mayor frecuencia, a diferencia de los otros elementos que ocurren solo una vez._

```python
import statistics

x = [2, 3, 2, 8, 12, 45, 8]
mode_ = statistics.multimode(x)
# output: [2, 8]
```

_**Nota:** maneja valores **nan**  como valores regulares y puede retornar **nan** como el valor modal._

_**variance( x )**_

_Calcula la **varianza de la muestra** cuantifica la propagación de los datos. Muestra numéricamente qué tan lejos están los puntos de datos de la media. Puede expresar la varianza muestral del conjunto de datos **𝑥** con **𝑛** elementos matemáticamente como **𝑠² = Σᵢ (𝑥ᵢ - mean (𝑥)) ² / (𝑛 - 1)**, donde **𝑖 = 1, 2, ..., 𝑛** y **mean (𝑥)** es la **media muestral** de **𝑥**. Si desea comprender más profundamente por qué divide la suma con **𝑛 - 1** en lugar de **𝑛**, puede profundizar en [la corrección de Bessel ](https://en.wikipedia.org/wiki/Bessel%27s_correction)._

```python
import statistics

x = [8.0, 1, 2.5, 4, 28.0]
variance_ = statistics.variance(x)
# output: 123.2
```

_**Nota:** si el conjunto de datos tiene valores **nan**, retornara **nan**._

_Una implementacion de python puro:_

```python
n = len(x)
mean_ = sum(x) / n
variance_ = sum((item - mean_)**2 for item in x) / (n - 1)
# output: 123.19999999999999
```

_**pvariance( x, mu=None )**_

_Calcula la **varianza de la población** de manera similar a la **varianza de la muestra**. Sin embargo, debe usar **𝑛** en el denominador en lugar de **𝑛 - 1: Σᵢ (𝑥ᵢ - mean (𝑥)) ² / 𝑛**. En este caso, **𝑛** es el número de elementos en toda la población._

_¡Tenga en cuenta que siempre debe saber si está trabajando con una muestra o con toda la población cada vez que calcula la varianza!_

```python
import statistics

x = [8.0, 1, 2.5, 4, 28.0]
variance_ = statistics.pvariance(x)
# output: 98.56
```

_**stdev( x, mu=None )**_

_Calcula la **desviación estándar de la muestra** es otra medida de la propagación de datos. Está conectado a la **varianza de la muestra**, ya que la **desviación estándar**, **𝑠**, es la raíz cuadrada positiva de la **varianza de la muestra**. La **desviación estándar** a menudo es más conveniente que la **varianza** porque tiene la misma unidad que los puntos de datos._

```python
import statistics

x = [8.0, 1, 2.5, 4, 28.0]
stdev_ = statistics.stdev(x)
# output: 11.099549540409287
```

_Una forma de implementarla con python puro seria, una vez que obtenga la **varianza**, puede calcular la **desviación estándar**:_

```python
stdev_ = variance_ ** 0.5
# output: 11.099549540409285
```

_**pstdev( x, mu=None )**_

_Calcula la **desviación estándar de la poblacion** de manera similar a la **desviacion de la muestra**_

```python
import statistics

x = [8.0, 1, 2.5, 4, 28.0]
stdev_ = statistics.stdev(x)
# output: 9.927738916792686
```

_**skew()**_

_La **asimetría de la muestra** mide la asimetría de una muestra de datos._

_Hay varias definiciones matemáticas de asimetría. Una expresión común para calcular la asimetría del conjunto de datos **𝑥** con **𝑛** elementos es **(𝑛² / ((𝑛 - 1) (𝑛 - 2))) (Σᵢ (𝑥ᵢ - mean (𝑥)) ³ / (𝑛𝑠³))**. Una expresión más simple es **Σᵢ (𝑥ᵢ - mean (𝑥)) ³ 𝑛 / ((𝑛 - 1) (𝑛 - 2) 𝑠³)**, donde **𝑖 = 1, 2, ..., 𝑛** y **mean (𝑥)** es la media muestral de **𝑥**. La **asimetría** definida de esta manera se denomina coeficiente de momento estandarizado de Fisher-Pearson ajustado.

_esta libreria no nos proporciona esta funcion pero puede implementarlo con python puro:_

```python
x = [8.0, 1, 2.5, 4, 28.0]
n = len(x)
mean_ = sum(x) / n
variance_ = sum((item - mean_)**2 for item in x) / (n - 1)
stdev_ = variance_ ** 0.5
skew_ = (sum((item - mean_)**3 for item in x)
        * n / ((n - 1) * (n - 2) * std_**3))
# output: 1.9470432273905929
```

_**quantiles( x, *, n=4, method='exclusive' )**_

_Divide los datos en **n** intervalos continuos con igual probabilidad. Devuelve una lista de puntos de corte que separan los intervalos. **n - 1**._

```python
import statistics

x = [-5.0, -1.1, 0.1, 2.0, 8.0, 12.8, 21.0, 25.8, 41.0]
statistics.quantiles(x, n=2)
# output: [8.0]

statistics.quantiles(x, n=4, method='inclusive')
#output: [0.1, 8.0, 21.0]
```
