# sqlalchemy

[https://docs.sqlalchemy.org/en/13/](https://docs.sqlalchemy.org/en/13/)

_**Instalacion**_

```python
pip install sqlalchemy
```

_**Verificar Version**_

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

_**Object Relational Mapper**_

_presenta un método para asociar clases Python definidas por el usuario con tablas de bases de datos, e instancias de esas clases (objetos) con filas en sus tablas correspondientes. Incluye un sistema que sincroniza de manera transparente todos los cambios de estado entre los objetos y sus filas relacionadas, denominado [unidad de trabajo ](https://docs.sqlalchemy.org/en/13/glossary.html#term-unit-of-work), así como un sistema para expresar consultas de la base de datos en términos de las clases definidas por el usuario y sus relaciones definidas entre sí._

_**declarative_base()**_

_Permite crear clases que incluyen directivas para describir la tabla de base de datos real a la que se asignarán._

```python
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
```

_Ahora que tenemos una "base", podemos definir cualquier número de clases mapeadas en términos de ella._

```python
from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                                self.name, self.fullname, self.nickname)
```

_**metadata.create_all(engine)**_

_Permite crear las tablas explicitamente en la base de datos, las tablas creadas seran las mapeadas utilizando **declarative_base()**_

```python
Base.metadata.create_all(engine)
```

_**Sessions**_

_En el sentido más general, `Session` establece todas las conversaciones con la base de datos y representa una "zona de espera" para todos los objetos que ha cargado o asociado con ella durante su vida útil. Proporciona el punto de entrada para adquirir un objeto `Query`, que envía consultas a la base de datos utilizando la conexión `Session` de la base de datos actual._

_**sessionmaker(bind=some_engine)**_

_Permite configurar una session_

```python
Session = sessionmaker(bind=some_engine)
```

_**Session()**_

_Permite crear una session_

```python
session = Session()
```

_Mantenga el ciclo de vida de la sesión (y generalmente la transacción) separada y externa:_

```python
### this is a **better** (but not the only) way to do it ###

class ThingOne(object):
    def go(self, session):
        session.query(FooBar).update({"x": 5})

class ThingTwo(object):
    def go(self, session):
        session.query(Widget).update({"q": 18})

def run_my_program():
    session = Session()
    try:
        ThingOne().go(session)
        ThingTwo().go(session)

        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
```

_El enfoque más completo, recomendado para aplicaciones más sustanciales, tratará de mantener los detalles de la gestión de sesiones, transacciones y excepciones lo más lejos posible de los detalles del programa que realiza su trabajo. Por ejemplo, podemos separar las preocupaciones usando un administrador de contexto :_

```python
### another way (but again *not the only way*) to do it ###

from contextlib import contextmanager

@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def run_my_program():
    with session_scope() as session:
        ThingOne().go(session)
        ThingTwo().go(session)
```
