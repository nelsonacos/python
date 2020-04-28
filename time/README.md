# time

```python
time.gmtime(0)
```

Devuelve el número de segundos que han pasado desde la época:

```python
time.time()
```

Devuelve el tiempo representado por un string:

```python
time.ctime(time)
```

```python
from time import struct_time

time_tuple = (2019, 2, 26, 7, 6, 55, 1, 57, 0)
time_obj = struct_time(time_tuple)
# time.struct_time(tm_year=2019, tm_mon=2, tm_mday=26, tm_hour=7, tm_min=6, tm_sec=55, tm_wday=1, tm_yday=57, tm_isdst=0)
```

```python
day_of_year = time_obj.tm_yday
 day_of_year
# 57

day_of_month = time_obj.tm_mday
day_of_month
# 26
```

```python
time.localtime(1551448206.86196)
```
