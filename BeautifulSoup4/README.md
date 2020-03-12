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

```python
html.prettify()
```

```python
html.title
```

```python
html.title.name
```

```python
html.title.string
```

```python
html.title.parent.name
```

```python
html.p
```

```python
html.p['class']
```

```python
html.a
```

```python
html.find_all('a')
```

```python
html.find(id='link3')
```

```python
for link in html.find_all('a'):
    print(link.get('href'))
```

```python
html.get_text()
```
