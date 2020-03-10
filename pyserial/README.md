# pyserial

```bash
pip install pyserial
```

```python3
import pyserial


connection = serial.Serial(
        'COM1',
        baudrate=9600,
        bytesize=8,
        patity='N',
        stopbits=1
)

```
