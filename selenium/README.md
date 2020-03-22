# selenium

_Selenium le permite ejecutar un navegador sin cabeza, es solo un navegador web normal, excepto que no contiene ningún elemento visible de la interfaz de usuario. Puede hacer más que hacer solicitudes: también puede representar HTML (aunque no puede verlo), mantener la información de la sesión e incluso realizar comunicaciones de red asincrónicas ejecutando código JavaScript._

_Instalar un WebDriver compatible con Selenium para su navegador web favorito_

_**Mozilla Firefox**_

_Descargando el web driver, visite  el [sitio web oficial](https://github.com/mozilla/geckodriver/releases/) para verificar la ultima version_

```bash
wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
```

_Descomprimiendo el contenido_

```bash
tar xvfz geckodriver-v0.26.0-linux64.tar.gz
```

_Instalando GeckoDriver_

```bash
mv geckodriver ~/.local/bin
```

_**Nota:** si no instala la ultima version de geckodriver o selenium puede generar un error_

_Instalando Selenium_

```bash
pip install selenium
```

```python
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

opts = Options()
opts.set_headless()
assert opts.headless  # Operating in headless mode
browser = Firefox(options=opts)
browser.get('https://duckduckgo.com')
```

_Buscando elementos por id_

```python
search_form = browser.find_element_by_id('search_form_input_homepage')
```

_Llenando formulario_

```python
search_form.send_keys('real python')
```

_Activando evento submit_

```python
search_form.submit()
```

_Buscando elemntos por clases_

```python
results = browser.find_elements_by_class_name('result')
```

_Accediendo a texto en elementos_

```python
results[0].text
```

_Activando el evento click_

```python
browser.find_element_by_class('playbutton').click()
```

_Cerrando una instancia del navegador_

```python
browser.close()
```
