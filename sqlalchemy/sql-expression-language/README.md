# sqlalchemy

[https://docs.sqlalchemy.org/en/13/](https://docs.sqlalchemy.org/en/13/)

_**Instalacion**_

```python
pip install sqlalchemy
```

_**sqlalchemy.__version__**_

_Permite verificar la version de sqlalchemy que esta instalada._

```python
import sqlalchemy

sqlalchemy.__version__ 
# output: 1.3.15
```

_**create_engine( database_url )**_

_El motor es el punto de partida para cualquier aplicación **sqlalchemy**. Crear un motor es solo cuestión de emitir una sola llamada **create_engine()**. _Puede encontrar [ejemplos de configuracion](https://docs.sqlalchemy.org/en/13/core/engines.html) del motor de base de datos.__

```python
from sqlalchemy import create_engine

engine = create_engine('dialect + driver: // user: pass @host : port / db', echo=True)
```

_**Nota:** Esto crea un  objeto `Dialect` adaptado al motor del la base de datos, así como un objeto `Pool` que establecerá una conexión **DBAPI** cuando se reciba por primera vez una solicitud de conexión. Tenga en cuenta que el motor y su subyacente `Pool` no establecen la primera conexión **DBAPI** real hasta que el método  `engine.connect()` es llamado, o una operación que depende de este método, como cuando se invoca `engine.execute()`._

_**Importar base de datos**_

_Puede cargar tablas automáticamente desde una base de datos ya existente, se hace  usando **reflexión**. La **reflexión** es el proceso de leer la base de datos y construir los metadatos basados ​​en esa información._

```python
import sqlalchemy as db

engine = db.create_engine('sqlite:///developer.sqlite')
connection = engine.connect()
metadata = db.MetaData()
nelson = db.Table('users', metadata, autoload=True, autoload_with=engine)
```

_**connect()**_

_Si en la conexion a la base de datos, esta no existe el motor de **sqlalchemy** creara automáticamente una nueva base de datos._

```python
import sqlalchemy as db

engine = db.create_engine('sqlite:///developer.sqlite')  # Create database developer
connection = engine.connect()
metadata = db.MetaData()

users = db.Table('users', metadata,
              db.Column('Id', db.Integer()),
              db.Column('name', db.String(255), nullable=False),
              db.Column('salary', db.Float(), default=100.0),
              db.Column('active', db.Boolean(), default=True)
              )

metadata.create_all(engine)  # Creates the table
```

_**table_name.columns.keys()**_

_Permite acceder a los nombres de las columnas de una tabla_

```python
print(nelson.columns.keys())
# output: ['Id', 'name', 'salary', 'active']
```

_**metadata.tables[ table_name ]**_

_Permite acceder a los metadatos de una tabla_

```python
print(repr(metadata.tables['users']))
"""
Table('census', MetaData(bind=None), Column('state', VARCHAR(length=30), table=<census>), Column('sex', VARCHAR(length=1), table=<census>), Column('age', INTEGER(), table=<census>), Column('pop2000', INTEGER(), table=<census>), Column('pop2008', INTEGER(), table=<census>), schema=None)
"""
```

_**db.insert( table )**_

_Inserting record one by one_

```python
query = db.insert(users).values(Id=1, name='naveen', salary=60000.00, active=True)
result_proxy = connection.execute(query)
```

_Inserting many records at ones_

```python
query = db.insert(users)

values_list = [
        {'Id':'2', 'name':'ram', 'salary':80000, 'active':False},
        {'Id':'3', 'name':'ramesh', 'salary':70000, 'active':True}
        ]
result_proxy = connection.execute(query,values_list)
```

_**connection.execute( query )**_

_Permite ejecutar la consulta. Retorna un objeto del tipo `ResultProxy` que contiene los resultados de la consulta._

```python
result_proxy = connection.execute(query)
```

_**fetchall()**_

_Permite recorer los datos almacenados en un objeto `ResultProxy`. Retorna un objeto de tipo `ResultSet`._

```python
result_set = result_proxy.fetchall()
```

_**db.select( [ table ] )**_

```python
query = db.select([users])  # Equivalent to 'SELECT * FROM users'

result_proxy = connection.execute(query)

result_set = result_proxy.fetchall()

result_set[:3]
```

_**where**_

```python
"""
Equivalent to SELECT * FROM users WHERE sex = F
"""
db.select([census]).where(census.columns.sex == 'F')
```

_**in**_

```python
"""
Equivalent to SELECT state, sex FROM users WHERE state IN (Texas, New York)
"""
db.select([users.columns.state, users.columns.sex]).where(users.columns.state.in_(['Texas', 'New York']))
```

_**and, or, not**_

```python
"""
Equivalent to SELECT * FROM  users WHERE state = 'California' AND NOT sex = 'M'
"""
db.select([users]).where(db.and_(users.columns.state == 'California', users.columns.sex != 'M'))
```

_**order by**_

```python
"""
Equivalent to SELECT * FROM users ORDER BY State DESC, pop2000
"""
db.select([users]).order_by(db.desc(users.columns.state), users.columns.pop2000)
```

_**funciones**_

```python
"""
Equivalent to SELECT SUM(pop2008) FROM users
"""
db.select([db.func.sum(users.columns.pop2008)])
```

_**Nota:** otras funciones incluidas avg, count, min, max…_

_**group by**_

```python
"""
Equivalent to SELECT SUM(pop2008) as pop2008, sex FROM users
"""
db.select([db.func.sum(users.columns.pop2008).label('pop2008'), users.columns.sex]).group_by(users.columns.sex)
```

_**distinct**_

```python
"""
Equivalent to SELECT DISTINCT state FROM users
"""
db.select([users.columns.state.distinct()])
```
