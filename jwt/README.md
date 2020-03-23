# jwt

```bash
pip install PyJWT
```
```python
import jwt

encoded = jwt.encode({'name': 'Nelson Acosta'}, 'secret', algorithm='HS256')
# output: 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoiTmVsc29uIEFjb3N0YSJ9.j49yqXTePjQRKjNJbDX7abg6UZ1KED8OjOqRbdE_4ng'

jwt.decode(encoded, 'secret', algorithms=['HS256'])
# output: {'name': 'Nelson Acosta'}
```
