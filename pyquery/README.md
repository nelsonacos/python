# pyquery

[https://pyquery.readthedocs.io/en/latest/](https://pyquery.readthedocs.io/en/latest/)

```python
pip install pyquery
```

```python
from requests import requests
from pyquery import PyQuery as pyquery 

response = requests.get( 'https://www.example.com' )
html = pyquery( response.text )

```
njop
