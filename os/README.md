# os
[https://docs.python.org/3/library/os.html?highlight=os#module-os](https://docs.python.org/3/library/os.html?highlight=os#module-os)

_El módulo OS de Python  nos permite trabajar con archivos y directorios. Todo lo referente al sistema operativo._

_**access( path, mode )**_

_Prueba el acceso a una ruta._

1. os.F_OK ( Encontrado )
2. os.R_OK ( Legible )
3. os.W_OK ( Escribible )
4. os.X_OK ( Ejecutable )

```python
import os

os.chdir( 'C:\\Users\\ lifei \\Desktop' )
os.acces( 'test.txt' , os.R_OK )
# outout: True
```

_**chdir( path )**_

_Moverse entre directorios._

```python
import os

os.chdir('C:\\Users\\lifei\\Desktop')
```

_**chflags( path, flags )**_

_Establece banderas de ruta a las banderas numéricas. Los valores que puede tomar:_

- os.UF_NODUMP  ( No volcar el archivo )
- os.UF_IMMUTABLE ( no puede cambiar el archivo )
- os.UF_APPEND ( solo puede agregar al archivo )
- os.UF_NOUNLINK ( no puede cambiar el nombre ni eliminar el archivo )
- os.UF_OPAQUE ( El directorio es opaco cuando lo vemos a través de una pila de unión )
- os.SF_ARCHIVED ( Puede archivar el archivo )
- os.SF_IMMUTABLE ( no puede cambiar el archivo )
- os.SF_APPEND ( solo puede agregar al archivo )
- os.SF_NOUNLINK ( no puede cambiar el nombre ni eliminar el archivo )
- os.SF_SNAPSHOT ( es un archivo de instantánea )

```python
import os

>>> os.chflags('Today.txt',os.SF_NOUNLINK)
```

_**Nota:** La mayoría de las banderas solo el superusuario puede cambiarlas. Además, algunas banderas no funcionan en todos los sistemas._

_**chmod( path, mode )**_

_Altera el modo de la ruta al modo numérico pasado. El modo puede ser uno de los siguientes valores ( o una combinación de ellos O a nivel de bits ):_

- stat.S_ISUID ( Establecer ID de usuario en ejecución )
- stat.S_ISGID ( Establecer ID de grupo en ejecución )
- stat.S_ENFMT ( Bloqueo de registro forzado )
- stat.S_ISVTX ( Después de la ejecución, guarda la imagen de texto )
- stat.S_IREAD ( Leído por el propietario )
- stat.S_IWRITE ( Escribir por el propietario )
- stat.S_IEXEC ( Ejecutar por propietario )
- stat.S_IRWXU ( Lectura, escritura y ejecución por parte del propietario )
- stat.S_IRUSR ( Leído por el propietario )
- stat.S_IWUSR ( Escribir por propietario )
- stat.S_IXUSR ( Ejecutar por propietario )
- stat.S_IRWXG ( Leer, escribir y ejecutar por grupo )
- stat.S_IRGRP ( Leído por grupo )
- stat.S_IWGRP ( Escribir por grupo )
- stat.S_IXGRP ( Ejecutar por grupo )
- stat.S_IRWXO ( Leer, escribir y ejecutar por otros )
- stat.S_IROTH ( Leído por otros )
- stat.S_IWOTH ( Escribir por otros )
- stat.S_IXOTH ( Ejecutar por otros )

```python
import os
import stat

os.chmod('Today.txt', stat.S_ISVTX)
```

_**chroot( path )**_

_Altera el directorio raíz del proceso actual a la ruta dada. Para usar esto, necesitamos privilegios de superusuario._

```python
import os

os.chroot("/Photos")
```

_**close( fd )**_

_Cierra el archivo asociado con el descriptor fd._

```python
import os

fd=os.open('Today.txt', os.O_RDWR)
os.close(fd)
```

_**closerange( fd_low, fd_high )**_

_ Cierra todos los descriptores de archivo de fd_low a fd_high. Aquí, fd_low es inclusivo y fd_high es exclusivo. Aquí, fd_low es el descriptor de archivo más bajo que se cerrará, mientras que fd_high es el más alto. Este método ignora los errores._

```python
import os

fd = os.open( "Today.txt", os.O_RDWR)
os.write(fd, "Testing")
os.closerange( fd, fd)
```

_**dup( fd )**_

_Devuelve un duplicado del descriptor de archivo fd._

```python
import os

fd = os.open( "Today.txt", os.O_RDWR)
d_fd = os.dup( fd )
os.write(d_fd, "Testing")
os.closerange( fd, d_fd)
```

_**dup2( fd, fd2 )**_

_Duplica el descriptor fd a fd2  si es necesario, cierra fd2 primero. El intérprete asigna la nueva descripción del archivo solo cuando está disponible._

```python
import os

os.open( "Today.txt", os.O_RDWR)
os.write(fd, "Testing")
fd2 = 1000
os.dup2(fd, fd2)
os.lseek(fd2, 0, 0)
str = os.read(fd2, 100)
print(f"Read String is {str}")
os.close( fd )
```

_**fchdir( fd )**_

_Altera el directorio de trabajo actual al directorio que representa el descriptor de archivo fd. Para esto, es obligatorio que el descriptor haga referencia a un directorio abierto, y no a un archivo abierto._

```python
import os

fchdir(fd)
```

_**fchmod( fd, mode )**_

_Altera el modo de archivo del archivo, especificado por fd, al modo numérico. El modo puede ser uno de los siguientes o una combinación de:_

- stat.S_ISUID ( Establecer ID de usuario en ejecución )
- stat.S_ISGID ( Establecer ID de grupo en ejecución )
- stat.S_ENFMT ( Bloqueo de registro forzado )
- stat.S_ISVTX ( Guardar imagen de texto después de la ejecución )
- stat.S_IREAD ( Leído por el propietario )
- stat.S_IWRITE ( Escribir por el propietario )
- stat.S_IEXEC ( Ejecutar por propietario )
- stat.S_IRWXU ( Lectura, escritura y ejecución por parte del propietario )
- stat.S_IRUSR ( Leído por el propietario )
- stat.S_IWUSR ( Escribir por propietario )
- stat.S_IXUSR ( Ejecutar por propietario )
- stat.S_IRWXG ( Leer, escribir y ejecutar por grupo )
- stat.S_IRGRP ( Leído por grupo )
- stat.S_IWGRP ( Escribir por grupo )
- stat.S_IXGRP ( Ejecutar por grupo )
- stat.S_IRWXO ( Leer, escribir y ejecutar por otros )
- stat.S_IROTH ( Leído por otros )
- stat.S_IWOTH ( Escribir por otros )
- stat.S_IXOTH ( Ejecutar por otros )

```python
import os

fd = os.open( "/tmp", os.O_RDONLY )
os.fchmod( fd, stat.S_IXGRP)
os.fchmod(fd, stat.S_IWOTH)
print "Changed mode successfully!!"
os.close( fd )
```

_**fchown( fd, uid, gid )**_

_Altera el propietario y la identificación del grupo del archivo especificado por fd al uid numérico y gid. Establece una identificación en -1 lo deja sin cambios._

```python
import os

fd = os.open( "/tmp", os.O_RDONLY )
os.fchown( fd, 100, -1)
os.fchown( fd, -1, 50)
print "Changed ownership successfully!!"
os.close( fd )
```

_**fdatasync( fd )**_

_Obliga a escribir el archivo con el descriptor de archivo fd en el disco. Esto, sin embargo, no obliga a actualizar los metadatos. Puede hacer esto para vaciar su búfer._

```python
import os

fd = os.open( "Today.txt", os.O_RDWR)
os.write(fd, "Testing")
os.fdatasync(fd)
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print(f"Read String is {str}")
os.close( fd )
```

_**fdopen( fd[, mode[, bufsize]] )**_

_Devuelve un objeto de archivo abierto. Este objeto está conectado al descriptor fd. Una vez que haga esto, puede realizar todas las funciones definidas en el objeto de archivo._

```python
import os

fd = os.open( "Today.txt", os.O_RDWR)
fo = os.fdopen(fd, "w+")
print (f"Current I/O pointer position {fo.tell()}")
fo.write( "Python is a great language.\nYeah its great!!\n");
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print (f"Read String is {str}")
print (f"Current I/O pointer position {fo.tell()}")
fo.close()
```

_**fpathconf( fd, name )**_

_Devuelve información de configuración del sistema que es relevante para un archivo abierto. Esto es bastante similar a la llamada al sistema unix fpathconf (). También acepta argumentos similares._

```python
import os

fd = os.open( "Today.txt", os.O_RDWR)
print (f"{os.pathconf_names}")
no = os.fpathconf(fd, 'PC_LINK_MAX')
print (f"Maximum number of links to the file: {no}")
no = os.fpathconf(fd, 'PC_NAME_MAX')
print (f"Maximum length of a filename :{no}")
os.close( fd)
```

_**fstat(fd)**_

_Devuelve información sobre el archivo perteneciente al fd. Echemos un vistazo a la estructura que devuelve :_

- st_dev ( ID del dispositivo que contiene el archivo )
- st_ino ( número de inodo )
- st_mode ( protección )
- st_nlink ( número de enlaces duros )
- st_uid ( ID de usuario del propietario )
- st_gid ( ID de grupo del propietario )
- st_rdev ( ID del dispositivo. Si es un archivo especial )
- st_size ( tamaño total, en bytes )
- st_blksize ( tamaño de bloque para E / S del sistema de archivos )
- st_blocks ( número de bloques asignados )
- st_atime ( hora del último acceso )
- st_mtime ( hora de la última modificación )
- st_ctime ( hora del último cambio de estado )

```python
import os

fd = os.open( "Today.txt", os.O_RDWR)
info = os.fstat(fd)
print (f"File Info: {info}")
print (f"UID of the file: {info.st_uid}")
print (f"GID of the file: {info.st_gid}")
os.close( fd)
```

_**fstatvfs( fd )**_

_Devuelve información relacionada con el sistema de archivos que contiene el archivo vinculado con el descriptor de archivo fd. Esta es la estructura que devuelve._

- f_bsize ( tamaño de bloque del sistema de archivos )
- f_frsize ( tamaño del fragmento )
- f_blocks ( tamaño de fs en unidades f_frsize )
- f_bfree ( bloques libres )
- f_bavail ( bloques libres para no root )
- f_files ( inodes )
- f_ffree ( inodes libres )
- f_favail ( inodes libres para no root )
- f_fsid (  un sistema de archivos )
- f_flag ( montar banderas )
- f_namemax ( longitud máxima del nombre de archivo )

```python
import os

fd = os.open( "Today.txt", os.O_RDWR)
info = os.fstatvfs(fd)
print(f"File Info: {info}")
print(f"Maximum filename length: {info.f_namemax}")
print (f"Free blocks: {info.f_bfree}")
os.close( fd)
```

_**fsync(fd)**_

_Obliga a escribir en el archivo relacionado con el descriptor fd al disco. Comenzando con un objeto de archivo Python f, primero ejecute f.flush (), luego ejecute os.fsync (f.fileno ()). Haga esto para asegurarse de que todos los búferes internos vinculados a f se escriban en el disco._

```python
import os

fd = os.open( "Today.txt", os.O_RDWR)
os.write(fd, "Testing")
os.fsync(fd)
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print("Read String is: {str} ")
sos.close( fd )
```

_**ftruncate(fd,length)**_

_Trunca el archivo vinculado al descriptor fd, por lo que tiene un tamaño de bytes como máximo._

```python
import os

fd = os.open( "Today.txt", os.O_RDWR)
os.write(fd, "Testing")
os.ftruncate(fd, 10)
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print("Read String is: {str}”)
os.close( fd )
```

_**getcwd()**_

_Devuelve el directorio de trabajo actual de un proceso._

```python
import os

os.getcwd()
```

_**getcwdu()**_

_Devuelve un objeto unicode que representa el directorio de trabajo actual._

```python
import os

os.chdir("/var/www/html" )
print(f"Current working dir: {os.getcwdu()}")
fd = os.open( "/tmp", os.O_RDONLY )
os.fchdir(fd)
print(f"Current working dir: {os.getcwdu()}”)
os.close( fd )
```

_**isatty( fd )**_

_Devuelve True si el descriptor fd está abierto y está conectado a un dispositivo tty (similar). De lo contrario, devuelve False._

```python
import os

fd = os.open( "Today.txt", os.O_RDWR)
os.write(fd, "Testing")
ret = os.isatty(fd)
print(f"Returned value is: {ret}")
os.close( fd )
```

_**lchflags( path, flags )**_

_Establece banderas de ruta a las banderas numéricas. A diferencia de **chflags ()**, ut no sigue enlaces simbólicos. Las banderas pueden ser uno de los siguientes valores, o una combinación de bit a bit de:_

- UF_NODUMP ( no volcar el archivo )
- UF_IMMUTABLE ( el archivo no puede modificarse )
- UF_APPEND ( el archivo solo se puede agregar a )
- UF_NOUNLINK ( el archivo no puede renombrarse ni eliminarse )
- UF_OPAQUE ( el directorio es opaco cuando se ve a través de una pila de unión )
- SF_ARCHIVED ( El archivo puede ser archivado )
- SF_IMMUTABLE ( el archivo no puede modificarse )
- SF_APPEND ( el archivo solo se puede agregar a )
- SF_NOUNLINK ( el archivo no se puede renombrar ni eliminar )
- SF_SNAPSHOT ( el archivo es un archivo de instantánea. )

```python
import os

path = "/var/www/html/Today.txt"
fd = os.open( path, os.O_RDWR)
os.close( fd )
ret = os.lchflags(path, os.UF_IMMUTABLE )
```

_**lchmod( path, mode )**_

_Establece el modo de ruta al modo numérico. Si la ruta es un enlace simbólico, afecta el enlace simbólico, no el destino. El modo puede ser uno de los siguientes valores, o una combinación de bits:_

- stat.S_ISUID ( Establecer ID de usuario en ejecución )
- stat.S_ISGID ( Establecer ID de grupo en ejecución )
- stat.S_ENFMT ( Bloqueo de registro forzado )
- stat.S_ISVTX ( Guardar imagen de texto después de la ejecución )
- stat.S_IREAD ( Leído por el propietario )
- stat.S_IWRITE ( Escribir por el propietario )
- stat.S_IEXEC ( Ejecutar por propietario )
- stat.S_IRWXU ( Lectura, escritura y ejecución por parte del propietario )
- stat.S_IRUSR ( Leído por el propietario )
- stat.S_IWUSR ( Escribir por propietario )
- stat.S_IXUSR ( Ejecutar por propietario )
- stat.S_IRWXG ( Leer, escribir y ejecutar por grupo )
- stat.S_IRGRP ( Leído por grupo )
- stat.S_IWGRP ( Escribir por grupo )
- stat.S_IXGRP ( Ejecutar por grupo )
- stat.S_IRWXO ( Leer, escribir y ejecutar por otros )
- stat.S_IROTH ( Leído por otros )
- stat.S_IWOTH ( Escribir por otros )
- stat.S_IXOTH ( Ejecutar por otros )

```python
import os

path = "/var/www/html/Today.txt"
fd = os.open( path, os.O_RDWR )
os.close( fd )
os.lchmod( path, stat.S_IXGRP)
os.lchmod("/tmp/Today.txt", stat.S_IWOTH)
```

_**lchown( path, uid, gid )**_

_Altera el propietario y la identificación del grupo de la ruta al uid y gid numéricos. No sigue enlaces simbólicos. Establecer una identificación en -1 lo deja sin cambios._

```python
import os

path = "/var/www/html/Today.txt"
fd = os.open( path, os.O_RDWR)
os.close( fd )
os.lchown( path, 500, -1)
os.lchown( path, -1, 500)
```

_**link( src, dst )**_

_Creará un enlace duro que apunta a un src llamado dst. Puede hacerlo cuando desee crear una copia de un archivo existente._

```python
import os

path = "/var/www/html/Today.txt"
fd = os.open( path, os.O_RDWR)
os.close( fd )
dst = "/tmp/today.txt"
os.link( path, dst )
```

_**listdir( path )**_

_Devolverá una lista con los nombres de las entradas en el directorio en la ruta. Esta lista está en un orden arbitrario y excluye entradas especiales '.' y '..', incluso si existen en el directorio._

```python
import os

path = "/var/www/html/"
dirs = os.listdir( path )
for file in dirs:
    print(file)
```

_**lseek( fd, pos, how )**_

_Establecerá la posición actual del descriptor fd en la posición especificada pos. 'how' lo modifica._

```python
import os

fd = os.open( "Today.txt", os.O_RDWR)
os.write(fd, "This is test")
os.fsync(fd)
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print(f"Read String is: {str}")
os.close( fd )
```

_**lstat( path )**_

_Al igual que **fstat ()**, **lstat ()** devuelve información sobre un archivo, pero no sigue enlaces simbólicos. lstat es un alias para **fstat ()** en aquellas plataformas que no admiten enlaces simbólicos, por ejemplo, Windows._

_Devuelve la siguiente estructura:_

- st_dev ( ID del dispositivo que contiene el archivo )
- st_ino ( número de inodo )
- st_mode ( protección )
- st_nlink ( número de enlaces duros )
- st_uid ( ID de usuario del propietario )
- st_gid ( ID de grupo del propietario )
- st_rdev ( ID del dispositivo. Si es un archivo especial )
- st_size ( tamaño total, en bytes )
- st_blksize ( tamaño de bloque para E / S del sistema de archivos )
- st_blocks ( número de bloques asignados )
- st_atime ( hora del último acceso )
- st_mtime ( hora de la última modificación )
- st_ctime ( hora del último cambio de estado )

```python
import os

path = "/var/www/html/Today.txt"
fd = os.open( path, os.O_RDWR)
os.close( fd )
info = os.lstat(path)
print(f"File Info: {info}")
print(f"UID of the file: {info.st_uid}")
print(f"GID of the file: {info.st_gid}")
```

_**major( device )**_

_Toma un número de dispositivo sin procesar y extrae el número mayor del dispositivo (generalmente el campo st_dev o st_rdev de stat)._

```python
import os

path = "/var/www/html/Today.txt"
info = os.lstat(path)
major_dnum = os.major(info.st_dev)
minor_dnum = os.minor(info.st_dev)
print(f"Major Device Number: {major_dnum}")
print(f"Minor Device Number: {minor_dnum}")
```

_**makedev(major,minor)**_

_Toma los números de dispositivo menor y mayor, y crea un número de dispositivo sin formato._

```python
import os

 path = "/var/www/html/Today.txt"
info = os.lstat(path)
major_dnum = os.major(info.st_dev)
minor_dnum = os.minor(info.st_dev)
print(f"Major Device Number: {major_dnum}")
print(f"Minor Device Number: {minor_dnum}")
dev_num = os.makedev(major_dnum, minor_dnum)
print(f"Device Number: {dev_num}")
```

_**makedirs( path [, mode ] )**_

_Crea un directorio de forma recursiva. De esta manera, es como **mkdir ()**. Sin embargo, exige que todos los directorios de nivel intermedio contengan el directorio hoja._

```python
import os

path = "/tmp/home/monthly/daily"
os.makedirs( path, 0755 )
```

_**minor( device )**_

_Tomará un número de dispositivo sin formato y extraerá el menor del dispositivo (generalmente el campo st_dev o st_rdev de stat)._

```python
import os

path = "/var/www/html/Today.txt"
info = os.lstat(path)
major_dnum = os.major(info.st_dev)
minor_dnum = os.minor(info.st_dev)
print(f"Major Device Number: {major_dnum}")
print(f"Minor Device Number: {minor_dnum}")
```

_**mkdir( path [, mode ] )**_

_Crea un directorio 'ruta' con el modo numérico 'mode'. Algunos sistemas ignoran el modo. Pero cuando se usa, enmascara primero el valor de umask actual. Modo predeterminado = 0777 (octal)._

```python
import os

path = "/tmp/home/monthly/daily/hourly"
os.mkdir( path, 0755 )
```

_**mkfifo( path [, mode] )**_

_Crea un FIFO llamado 'ruta' con el modo numérico especificado. Enmascara primero el valor actual de umask. Modo predeterminado = 0666 (octal)._

```python
import os

path = "/tmp/hourly"
os.mkfifo( path, 0644 )
```

_**mknod( filename[, mode=0600, device] )**_

_Creará un nodo del sistema de archivos llamado 'filename'. Puede ser un archivo, un archivo especial de dispositivo o una canalización con nombre._

```python
import os

filename = '/tmp/tmpfile'
mode = 0600|stat.S_IRUSR
os.mknod(filename, mode)
```

_**open( file, flags[, mode] )**_

_Abrirá el archivo 'file' y establecerá flags en función de los flags especificados. Posiblemente establece su modo de acuerdo con el modo especificado. También oculta primero el valor de umask actual. Modo predeterminado = 0777 (octal)._

_Puede tomar uno de estos valores, o una combinación de bit a bit de estos:_

- os.O_RDONLY ( abierto solo para lectura )
- os.O_WRONLY ( abierto solo para escritura )
- os.O_RDWR ( abierto para leer y escribir )
- os.O_NONBLOCK: ( no bloquear al abrir )
- os.O_APPEND ( agregar en cada escritura )
- os.O_CREAT ( crea un archivo si no existe )
- os.O_TRUNC ( trunca el tamaño a 0 )
- os.O_EXCL ( error si crear y archivo existe )
- os.O_SHLOCK ( obtiene atómicamente un bloqueo compartido )
- os.O_EXLOCK ( obtiene atómicamente un bloqueo exclusivo )
- os.O_DIRECT ( elimina o reduce los efectos de caché )
- os.O_FSYNC ( escrituras sincrónicas )
- os.O_NOFOLLOW ( no sigas enlaces simbólicos )

```python
import os

fd = os.open( "Today.txt", os.O_RDWR)
os.write(fd, "This is test")
os.close( fd )
```

_**Nota:** devuelve el descriptor para el archivo que abrimos._

_**openpty()**_

_Abre un par pseudo-terminal. Luego, devuelve un par de descriptores, maestro y esclavo, para pty y tty, respectivamente._

```python
import os

m,s = os.openpty()
print(m)
print(s)
s = os.ttyname(s)
print(m)
print(s)
```

_**pathconf( path, name )**_

_Devuelve información de configuración del sistema perteneciente a un archivo con nombre._

```python
import os

print(f"{os.pathconf_names}" )
no = os.pathconf('a2.py', 'PC_NAME_MAX')
print(f"Maximum length of a filename: {no}")
no = os.pathconf('a2.py', 'PC_FILESIZEBITS')
print(f"file size in bits: {no}")
```

_**pipe()**_

_Crea una tubería. Luego, devuelve un par de descriptores, r & w, para leer y escribir._

```python
import os

os.pipe()
```

_**popen( command [, mode[, bufsize ]] )**_

_Abrirá una tubería hacia o desde el comando especificado. Devuelve un objeto de archivo abierto que está conectado al tubo. Podemos leer o escribir en este objeto dependiendo de si el modo es 'r' (predeterminado) o 'w'. El argumento bufsize significa lo mismo que en la función open ()._

```python
import os

a = 'mkdir nwdir'
b = os.popen(a,'r',1)
```

_**read( fd, n )**_

_Permite leer a lo sumo n bytes desde el descriptor fd. Devuelve una cadena que contiene los bytes que acabamos de leer. Y si llega al final del archivo, devuelve una cadena vacía._

```python
import os

fd = os.open("f1.txt",os.O_RDWR)
ret = os.read(fd,12)
print(ret)
os.close(fd)
```

_**readlink( path )**_

_Devolverá una cadena que indica la ruta a la que apunta el enlace simbólico. Puede devolver un nombre de ruta relativo o absoluto._

```python
import os

src = '/usr/bin/python'
dst = '/tmp/python'
os.symlink(src, dst)
path = os.readlink( dst )
print(path)
```

_**remove( path )**_

_Elimina la ruta del archivo especificado. Si esa ruta es un directorio, genera un OSError._

```python
import os

print(f"The dir is: {os.listdir(os.getcwd())}")
os.remove("aa.txt")
print(f"The dir after removal of path: {os.listdir(os.getcwd())}")
```

_**removedirs( path )**_

_Eliminará directorios de forma recursiva. Y si eliminamos con éxito el directorio hoja, intenta eliminar sucesivamente todos los directorios principales que se muestran en esa ruta._

```python
import os

print(f"The dir is: {os.listdir(os.getcwd())}")
os.removedirs("/tutorialsdir")
print(f"The dir after removal is: {os.listdir(os.getcwd())}")
```

_**rename( src, dst )**_

_Cambia el nombre de un archivo o directorio. Si el destino es un archivo o un directorio que ya existe, genera un OSError._

```python
import os

print(f"The dir is: {os.listdir(os.getcwd())}”)
os.rename("tutorialsdir","tutorialsdirectory")
print(“Successfully renamed”)
print(f"The dir is: {os.listdir(os.getcwd())}")
```

_**renames( old, new )**_

_Renombra directorios y archivos de forma recursiva. Es como **os.rename ()**, pero también mueve un archivo a un directorio, o un árbol completo de directorios, que aún no existen._

```python
import os

print("Current directory is: { os.getcwd()}")
print("The dir is: { os.listdir(os.getcwd())}")
os.renames("aa1.txt","newdir/aanew.txt")
print("Successfully renamed”)
print(f"The dir is: {os.listdir(os.getcwd())}")
```

_**rmdir( path )**_

_ Elimina la ruta de directorio especificada. Sin embargo, si el directorio no está vacío, genera un OSError._

```python
import os

print(f"the dir is: { os.listdir(os.getcwd())}")
os.rmdir("mydir")
print(f"the dir is: { os.listdir(os.getcwd())}"
```

_**stat( path )**_

_Realiza una llamada de sistema de estadísticas en la ruta especificada._

_Estos son los miembros de la estructura estadística:_

- st_mode ( bits de protección )
- st_ino ( número de inodo )
- st_dev ( dispositivo )
- st_nlink ( número de enlaces duros )
- st_uid ( ID de usuario del propietario )
- st_gid ( ID de grupo del propietario )
- st_size ( tamaño del archivo, en bytes )
- st_atime ( hora del acceso más reciente )
- st_mtime ( hora de la modificación de contenido más reciente )
- st_ctime ( hora del cambio de metadatos más reciente. )

```python
import os

statinfo = os.stat('a2.py')
print(statinfo)
```

_**stat_float_times( [newvalue] )**_

_Module decide si stat_result denota marcas de tiempo como objetos flotantes._

```python
import os

import os, sys
statinfo = os.stat('a2.py')
print(statinfo)
statinfo = os.stat_float_times()
print(statinfo)
```

_**statvfs( path )**_

_Ejecuta una llamada al sistema statvfs en la ruta especificada._

_La estructura tiene los siguientes miembros:_

- f_bsize ( tamaño de bloque del sistema de archivos preferido )
- f_frsize ( tamaño de bloque fundamental del sistema de archivos )
- f_blocks ( número total de bloques en el sistema de archivos )
- f_bfree ( número total de bloques libres )
- f_bavail ( bloques gratuitos disponibles para usuarios no super )
- f_files (número total de nodos de archivo )
- f_ffree ( número total de nodos de archivos libres )
- f_favail ( nodos gratuitos disponibles para usuarios no super )
- f_flag ( depende del sistema )
- f_namemax ( longitud máxima del nombre del archivo )

```python
import os

stinfo = os.statvfs('a1.py')
print(stinfo)
```

_**symlink( src, dst )**_

_Compone un enlace simbólico dst que apunta a la fuente._

```python
import os

src = '/usr/bin/python'
dst = '/tmp/python'
os.symlink( src, dst )
```

_**tcgetpgrp( fd )**_

_Devuelve el grupo de procesos vinculado al terminal especificado por fd, que es un descriptor de archivo abierto, y lo devuelve os.open ()._

```python
import os

print(f"Current working dir : { os.getcwd()}")
fd = os.open("/dev/tty",os.O_RDONLY)
f = os.tcgetpgrp(fd)
print(f"the process group associated is: {f}")
os.close(fd)
```

_**tcsetpgrp( fd, pg )**_

_Establece el grupo de procesos vinculado al terminal especificado por fd, que es un descriptor de archivo abierto, y os.open () lo devuelve a pg._

```python
import os

print(f"Current working dir : { os.getcwd()}")
fd = os.open("/dev/tty",os.O_RDONLY)
f = os.tcgetpgrp(fd)
print(f"the process group associated is: {f}")
os.tcsetpgrp(fd,2672)
print("done")
os.close(fd)
```

_**tempnam( [dir[, prefix]] )**_

_Devuelve un nombre de ruta único lo suficientemente razonable como para crear un archivo temporal._

```python
import os

tmpfn = os.tempnam('/tmp/tutorialsdir,'tuts1')
```

_**tmpfile()**_

_Devolverá un nuevo objeto de archivo temporal, abriéndolo en modo de actualización (w + b). Este archivo tiene cero entradas de directorio vinculadas y se eliminará automáticamente cuando no haya descriptores disponibles._

```python
import os

tmpfile = os.tmpfile()
tmpfile.write('Temporary newfile is here.....')
tmpfile.seek(0)
print(tmpfile.read())
tmpfile.close()
```

_**tmpnam()**_

_Devolverá un nombre de ruta único lo suficientemente razonable como para crear un archivos temporal._

```python
import os

tmpfn = os.tmpnam()
print(f"This is the unique path: {tmpfn}")
```

_**ttyname( fd )**_

_Devolverá una cadena que denota el dispositivo terminal vinculado al descriptor fd. Si no está vinculado a un dispositivo terminal, genera una excepción._

```python
import os

print(f"Current working dir : { os.getcwd()}")
fd = os.open("/dev/tty",os.O_RDONLY)
p = os.ttyname(fd)
print(f"the terminal device associated is: {p}")
os.close(fd)
```

_**unlink( path )**_

_Eliminará la ruta de archivo especificada. Si es un directorio, genera un OSError._

```python
import os

print(f"The dir is: { os.listdir(os.getcwd())}")
os.unlink("aa.txt")
print(f"The dir after removal of path : { os.listdir(os.getcwd())}")
```

_**utime( path, times )**_

_Establece el acceso y los tiempos modificados del archivo en la ruta especificada._

```python
import os

stinfo = os.stat('a2.py')
print(stinfo)
print(f"access time of a2.py: { stinfo.st_atime }")
print(f"modified time of a2.py: { stinfo.st_mtime }")
os.utime("a2.py",(1330712280, 1330712292))
```

_**walk(top[, topdown=True[, onerror=None[, followlinks=False]]])**_

_Crea nombres de archivo en un árbol de directorios. Lo hace caminando el árbol de abajo hacia arriba o de arriba hacia abajo. Tiene los siguientes parámetros:_

- top: cada directorio está enraizado en el directorio
- topdown: si topdown es True o no se especifica, escanea los directorios de arriba a abajo.
- onerror: esto puede mostrar un error para continuar con la caminata, o puede generar una excepción para abortar la caminata.
- sfollowlinks: visitará los directorios a los que apunta symlinks, es decir, si se establece en true.

```python
import os

for root, dirs, files in os.walk(".", topdown=False):
```

_**write( sfd, str )**_

_Escribirá la cadena especificada en el descriptor fd. Devuelve el número de bytes que realmente escribió._

```python
import os

fd = os.open("f1.txt",os.O_RDWR|os.CREAT)
ret = os.write(fd,"This is test")
print(f"the number of bytes written: {ret}")
print("written successfully")
os.close(fd)
```
