# re

_**match( patron, cadena )**_

```python
import re

re.match( r"regular expresion", target )
# output: result
```

_**Nota:** Encuentra coincidencias si se produce al inicio de la cadena. Retorna la primera coincidencia_

_**search( patron, cadena )**_

```python
import re

re.search( r"regular expresion", target )
# output: result
```

_**Nota:** Encuentra coincidencias en cualquier parte de la cadena. Retrona la primera conincidencia_

_**findall( patron, cadena )**_

```python
import re

target = ""

re.findall( r"regular expresion", target )
# output: result
```

_**Nota:** Encuentra coincidencias en cualquier parte de la cadena. Retorna una lista con todas las coincidencias._

_**split( patron, cadena, maxsplit = 0 )**_

```python
import re

re.split( r"regular expresion", target )
# output: result
```

_**Nota:** Encuentra coincidencias. Divide la cadena donde encontro las coincidencias._

_**sub( patron,  replica, cadena  )**_

```python
import re

re.sub( r"regular expresion", target )
# output: result
```

_**Nota:** Encuentra coincidencias en cualquier parte de la cadena. Reemplaza la cadena donde encontro conincidencias_

_**compile( patron,  cadena  )**_

```python
import re

re.compile( r"regular expresion", target )
# output: result
```
