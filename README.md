PycNic
======

PycNyc Is a python way to interact with Nic.Ar

Example
======


```python
from api import Pycnic

print 'Logueando'
p = Pycnic("gonzafirewall", "Laformuladed10s")

print '--- dominios --- '
for dominio in p.obtener_dominios():
    print dominio.url, dominio.estado
`````



