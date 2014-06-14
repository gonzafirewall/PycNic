PycNic
======

PycNyc Is a python way to interact with Nic.Ar

Example
======


```python
from api import Pycnic

print 'Logueando'
p = Pycnic("test", "testingpass")

print '--- dominios --- '
for dominio in p.obtener_dominios():
    print dominio.url, dominio.estado
`````

output

Logueando
--- dominios --- 
midominio.com.ar Registrado
eldominioloco.com.ar Registrado

