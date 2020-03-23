# csv

[https://docs.python.org/3/library/csv.html](https://docs.python.org/3/library/csv.html)

_Proporciona funcionalidad para leer y escribir en archivos CSV. Diseñado para trabajar fuera de la caja con archivos CSV generados por Excel, se adapta fácilmente para trabajar con una variedad de formatos CSV. Contiene objetos y otro código para leer, file = "escribir y procesar datos desde y hacia archivos CSV._

_**reader(file , delimiter=",")**_

```python
#!/usr/bin/env python3
import csv

file = ""

with open( file ) as csv_file:
    csv_reader = csv.reader( csv_file, delimiter=',' )
```

_**Nota**: Retorna una lista de String elementos  por cada fila encontrada. Contienen los datos encontrados al eliminar los delimitadores. La primera fila ( encabezados ) se le da un tratamiento diferente_

_**DictReader(csv_file)**_

```python
#!/usr/bin/env python3
import csv

file = ""

with open(file, mode='r') as csv_file:
    csv_reader = csv.DictReader( csv_file )
```

_**Nota:** retorna una coleccion de diccionarios y las claves asignadas se toman de la primera fila ( encabezados ). Si no tiene estos encabezados en su archivo CSV, debe especificar sus propias claves configurando el parámetro opcional `fieldnames` en una lista que las contenga._

_**Parametros opcionales**_

_Visite la [documentacion oficial](https://docs.python.org/3/library/csv.html?highlight=csv#csv-fmt-params) para conocer mas sobre los parametros opcionales._

```csv
john smith,1132 Anywhere Lane Hoboken NJ, 07030,Jan 4
erica meyers,1234 Smith Lane Hoboken NJ, 07030,March 2
```

_**writerow()** del objeto **writer**_

```python
#!/usr/bin/env python3
import csv

file = ""

with open(file, mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
```

_**DictWriter(csv_file, fieldnames=fieldnames)**_

```python
#!/usr/bin/env python3
import csv

file = ""

with open(file, mode='w') as csv_file:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})
```

_**Nota:** Con DictReader, el parámetro `fieldnames` es obligatorio al escribir un diccionario._
