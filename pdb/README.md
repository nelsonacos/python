# pdb

[https://docs.python.org/3/library/pdb.html](https://docs.python.org/3/library/pdb.html)

```python
import pdb; pdb.set_trace()
```

_A partir de Python 3.7, hay otra forma de ingresar al depurador_

```python
breakpoint()
```

_Por defecto, `breakpoint()` importará pdby llamará `pdb.set_trace()`_

_También puede ingresar al depurador, sin modificar la fuente y usar `pdb.set_trace()` o `breakpoint()`, ejecutando Python directamente desde la línea de comandos y pasando la opción `-m pdb`_.

```python
python3 -m pdb app.py arg1 arg2
```

## Comenzando

_example1.py_

```python
#!/usr/bin/env python3

filename = __file__
import pdb; pdb.set_trace()
print(f'path = {filename}')
```

_Si corres esto en la terminal_

```python
$ ./example1.py 
> /code/example1.py(5)<module>()
-> print(f'path = {filename}')
(Pdb)
```

## Comandos Escensiales

### p

_Imprime el valor de una expresión_

```python
(Pdb) p filename
'./example1.py'
(Pdb)
```

### pp

_Bonita impresión del valor de una expresión_

### n

_Continúe la ejecución hasta que se alcance la siguiente línea en la función actual o regrese._

```python
$ ./example3.py
> /code/example3.py(14)<module>()
-> filename_path = get_path(filename)
(Pdb) n
> /code/example3.py(15)<module>()
-> print(f'path = {filename_path}')
(Pdb) 
```

### s

_Ejecute la línea actual y pare en la primera ocasión posible (ya sea en una función que se llama o en la función actual)._

```python
$ ./example3.py
> /code/example3.py(14)<module>()
-> filename_path = get_path(filename)
(Pdb) s
--Call--
> /code/example3.py(6)get_path()
-> def get_path(filename):
(Pdb)
```

### enter

_Para repetir el comando hasta llegar a la última línea de origen._

```python
$ ./example3.py 
> /code/example3.py(14)<module>()
-> filename_path = get_path(filename)
(Pdb) s
--Call--
> /code/example3.py(6)get_path()
-> def get_path(filename):
(Pdb) n
> /code/example3.py(8)get_path()
-> head, tail = os.path.split(filename)
(Pdb) 
> /code/example3.py(9)get_path()
-> return head
(Pdb) 
--Return--
> /code/example3.py(9)get_path()->'.'
-> return head
(Pdb) 
> /code/example3.py(15)<module>()
-> print(f'path = {filename_path}')
(Pdb) 
path = .
--Return--
> /code/example3.py(15)<module>()->None
-> print(f'path = {filename_path}')
(Pdb)
```

### c

_Continúe la ejecución y solo pare cuando se encuentre un punto de interrupción. unt Continúe la ejecución hasta alcanzar la línea con un número mayor que el actual. Con un argumento de número de línea, continúe la ejecución hasta que se alcance una línea con un número mayor o igual a ese._

```python
$ ./example4.py
> /code/example4.py(7)<module>()
-> filename_path = util.get_path(filename)
(Pdb) b util:5
Breakpoint 1 at /code/util.py:5
(Pdb) c
> /code/util.py(5)get_path()
-> return head
(Pdb) p filename, head, tail
('./example4.py', '.', 'example4.py')
(Pdb)
```

```python
$ ./example4.py
> /code/example4.py(7)<module>()
-> filename_path = util.get_path(filename)
(Pdb) b util.get_path
Breakpoint 1 at /code/util.py:1
(Pdb) c
> /code/util.py(3)get_path()
-> import os
(Pdb) p filename
'./example4.py'
(Pdb)
```

### l

_Listar el código fuente para el archivo actual. Sin argumentos, enumere 11 líneas alrededor de la línea actual o continúe con el listado anterior._

```python
$ ./example3.py
> /code/example3.py(14)<module>()
-> filename_path = get_path(filename)
(Pdb) l
  9         return head
 10
 11
 12     filename = __file__
 13     import pdb; pdb.set_trace()
 14  -> filename_path = get_path(filename)
 15     print(f'path = {filename_path}')
[EOF]
(Pdb) l
[EOF]
(Pdb) l .
  9         return head
 10  
 11  
 12     filename = __file__
 13     import pdb; pdb.set_trace()
 14  -> filename_path = get_path(filename)
 15     print(f'path = {filename_path}')
[EOF]
(Pdb)
```

#### ll

_Lista el código fuente completo para la función o marco actual._

```python
$ ./example2.py
> /code/example2.py(10)get_path()
-> return head
(Pdb) ll
  6     def get_path(filename):
  7         """Return file's path or empty string if no path."""
  8         head, tail = os.path.split(filename)
  9         import pdb; pdb.set_trace()
 10  ->     return head
(Pdb) p filename
'./example2.py'
(Pdb) p head, tail
('.', 'example2.py')
(Pdb) p 'filename: ' + filename
'filename: ./example2.py'
(Pdb) p get_path
<function get_path at 0x100760e18>
(Pdb) p getattr(get_path, '__doc__')
"Return file's path or empty string if no path."
(Pdb) p [os.path.split(p)[1] for p in os.path.sys.path]
['pdb-basics', 'python36.zip', 'python3.6', 'lib-dynload', 'site-packages']
(Pdb)
```

### b (break) [ ([filename:]line | function) [, condition] ]

_Sin argumentos, enumere todos los saltos. Con un argumento de número de línea, establezca un punto de interrupción en esta línea en el archivo actual._

```python
$ ./example4.py
> /code/example4.py(7)<module>()
-> filename_path = util.get_path(filename)
(Pdb) b util:5
Breakpoint 1 at /code/util.py:5
(Pdb) c
> /code/util.py(5)get_path()
-> return head
(Pdb) p filename, head, tail
('./example4.py', '.', 'example4.py')
(Pdb)
```

```python
$ ./example4.py
> /code/example4.py(7)<module>()
-> filename_path = util.get_path(filename)
(Pdb) b util.get_path
Breakpoint 1 at /code/util.py:1
(Pdb) c
> /code/util.py(3)get_path()
-> import os
(Pdb) p filename
'./example4.py'
(Pdb)
```

_Ingrese b sin argumentos para ver una lista de todos los puntos de interrupción_

```python
(Pdb) b
Num Type         Disp Enb   Where
1   breakpoint   keep yes   at /code/util.py:1
(Pdb)
```

_Puede deshabilitar y volver a habilitar los puntos de interrupción con el comando `disable` Num `enable` Num._

```python
(Pdb) disable 1
Disabled breakpoint 1 at /code/util.py:1
(Pdb) b
Num Type         Disp Enb   Where
1   breakpoint   keep no    at /code/util.py:1
(Pdb) enable 1
Enabled breakpoint 1 at /code/util.py:1
(Pdb) b
Num Type         Disp Enb   Where
1   breakpoint   keep yes   at /code/util.py:1
(Pdb)
```

_Para eliminar un punto de interrupción, use el comando `cl` (borrar)_

```python
cl(ear) filename:lineno
cl(ear) [bpnumber [bpnumber...]]
```

### w

_Imprima un seguimiento de pila, con el cuadro más reciente en la parte inferior. Una flecha indica el marco actual, que determina el contexto de la mayoría de los comandos._

```python
$ ./example5.py
> /code/fileutil.py(5)get_path()
-> head, tail = os.path.split(fname)
(Pdb) w
  /code/example5.py(12)<module>()
-> filename_path = get_file_info(filename)
  /code/example5.py(7)get_file_info()
-> file_path = fileutil.get_path(full_fname)
> /code/fileutil.py(5)get_path()
-> head, tail = os.path.split(fname)
(Pdb)
```

_Esto nos permite identificar quien llama a quien en cada momento en la pila de llamadas. Si desea aprender mas sobre lo que es una pila de llamada puede mirar este [articulo en la Wikipedia](https://en.wikipedia.org/wiki/Call_stack)_

### h

_Vea una lista de comandos disponibles._

```python
(Pdb) h

Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt
alias  clear      disable  ignore    longlist  r        source   until
args   commands   display  interact  n         restart  step     up
b      condition  down     j         next      return   tbreak   w
break  cont       enable   jump      p         retval   u        whatis
bt     continue   exit     l         pp        run      unalias  where

Miscellaneous help topics:
==========================
exec  pdb

(Pdb)
```

### h \<topic\>

_Mostrar ayuda para un comando o tema._

```python
(Pdb) h w
w(here)
        Print a stack trace, with the most recent frame at the bottom.
        An arrow indicates the "current frame", which determines the
        context of most commands. 'bt' is an alias for this command.
```

### h pdb

_Mostrar la documentación completa de pdb._

```python
The Python Debugger Pdb
=======================

To use the debugger in its simplest form:

        >>> import pdb
        >>> pdb.run('<a statement>')

The debugger's prompt is '(Pdb) '.  This will stop in the first
function call in <a statement>.

Alternatively, if a statement terminated with an unhandled exception,
you can use pdb's post-mortem facility to inspect the contents of the
traceback:

        >>> <a statement>
        <exception traceback>
        >>> import pdb
        >>> pdb.pm()

The commands recognized by the debugger are listed in the next
section.  Most can be abbreviated as indicated; e.g., h(elp) means
that 'help' can be typed as 'h' or 'help' (but not as 'he' or 'hel',
:
```

### q

_Salga del depurador y salga._
