# pip

[https://pip.pypa.io/en/stable/reference/pip_install/](https://pip.pypa.io/en/stable/reference/pip_install/)

Instalar pip en python 2.x

```bash
sudo apt install python-pip
```

Instalar pip en python 3.x

```bash
sudo apt install python3-pip
```

Instalar un paquete de Python

```python
pip install ansible
```

Instalar una versión de paquete específica

```python
pip install ansible==2.7.8
```

Desinstalar un paquete de Python

```python
pip uninstall ansible
```

Vea qué versiones están disponibles ( !use una cadena de version ilegal )

```python
pip install ansible==foobar
```

Actualiza un paquete

```python
pip install --upgrade ansible
```

Otra forma de actualizar un paquete

```python
pip install ansible -U
```

Lista de paquetes instalados

```python
pip list
```

Lista de paquetes instalados obsoletos

```python
pip list --outdated
```

Capture paquetes instalados

```python
pip freeze > requirements.txt
```

Instalar un archivo de dependencias

```python
pip install -r requirements.txt
```

Busca un paquete

```python
pip search foo
```
