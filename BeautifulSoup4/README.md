# BeautifulSoup

[https://www.crummy.com/software/BeautifulSoup/bs4/doc/](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

```python
pip install BeautifulSoup
```

**BeautifulSoup** normalmente se usa en conjunto con [ requests ](https://github.com/nelsonacos/python/tree/master/requests)

```python
from requests import requests
from bs4 import BeautifulSoup

url = 'https://example.com/'
response = requests.get(url)

html = BeautifulSoup( response, 'html.parser' )
```
