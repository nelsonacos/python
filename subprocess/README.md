# subprocess
[https://docs.python.org/2.7/library/subprocess.html?highlight=subprocess#module-subprocess](https://docs.python.org/2.7/library/subprocess.html?highlight=subprocess#module-subprocess)

_El módulo de subproceso proporciona una interfaz consistente para crear y trabajar con procesos adicionales. Ofrece una interfaz de nivel superior que algunos de los otros módulos disponibles, y está destinado a reemplazar funciones como **os.system () , os.spawn * () , os.popen * () , popen2. * () Y comandos . * ()**._

_El módulo de subproceso define una clase, Popen y algunas funciones de contenedor que usan esa clase. El constructor de Popen toma argumentos para configurar el nuevo proceso para que el padre pueda comunicarse con él a través de tuberías. Proporciona toda la funcionalidad de los otros módulos y funciones que reemplaza, y más. La API es coherente para todos los usos, y muchos de los pasos adicionales de sobrecarga necesarios (como cerrar descriptores de archivos adicionales y garantizar que las tuberías estén cerradas) están "incorporados" en lugar de ser manejados por el código de la aplicación por separado._

_**call ( [command list], shell = True )**_

_Para ejecutar un comando externo sin interactuar con él, como lo haría con **os.system ()** , use la función **call()**._

```python
import subprocess

subprocess.call([ 'ls' ,  '-1' ],  shell = True)
```

_**Nota:** Al establecer el argumento de `shell=True `, el subproceso genera un proceso de shell intermedio y le dice que ejecute el comando. El valor predeterminado es ejecutar el comando directamente. El uso de un shell intermedio significa que las variables, los patrones globales y otras características especiales del shell en la cadena de comandos se procesan antes de ejecutar el comando._

_**check_call ( [command list], shell = True )**_

_Funciona como **call()**, excepto que se verifica el código de salida, y si indica que ocurrió un error, se genera una excepción **CalledProcessError **._

```pyhon
import subprocess

subprocess. check_call ([ 'false' ], shell = True)
```

_**Nota:** El comando `false` siempre sale con un código de estado distinto de cero, que **check_call()** interpreta como un error._

_**check_output()**_

_Los canales de entrada y salida estándar para el proceso iniciado por **call()** están vinculados a la entrada y salida del padre. Eso significa que el programa de llamada no puede capturar la salida del comando. Use **check_output()** para capturar la salida para su posterior procesamiento._

```pyhon
import subprocess

output = subprocess.check_output(['ls', '-1'])
print 'Have %d bytes in output' % len(output)
print output
```

_Este script ejecuta una serie de comandos en una subshell. Los mensajes se envían a la salida estándar y al error estándar antes de que los comandos salgan con un código de error._

```pyhon
import subprocess

output = subprocess.check_output(
    'echo to stdout; echo to stderr 1>&2; exit 1',
    shell=True,
    )
print 'Have %d bytes in output' % len(output)
print output
```

_**Nota:** El mensaje de `standard error` se imprime en la consola, pero el mensaje de `standard output` está oculto._

_Para evitar que los mensajes de error de los comandos ejecutados a través de **check_output ()** se escriban en la consola, establezca el parámetro `stderr` en la constante `STDOUT`._

```pyhon
import subprocess

output = subprocess.check_output(
    'echo to stdout; echo to stderr 1>&2; exit 1',
    shell=True,
    stderr=subprocess.STDOUT,
    )
print 'Have %d bytes in output' % len(output)
print output
```

_**Popen()**_

_Para ejecutar un proceso y leer toda su salida, establezca el valor **stdout** en `PIPE` y llame a **comunicate()**._

```python
import subprocess

print '\nread:'
proc = subprocess.Popen(['echo', '"to stdout"'], 
                        stdout=subprocess.PIPE,
                        )
stdout_value = proc.communicate()[0]
print '\tstdout:', repr(stdout_value)
```

_**Nota:** esto es similar a la forma en que funciona **os.popen()** , excepto que la lectura es administrada internamente por la instancia de `Popen`._
