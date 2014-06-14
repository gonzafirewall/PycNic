from mechanize import Browser
import webbrowser
import sys
from BeautifulSoup import BeautifulSoup as bs

def guardar(html):
    name = 'index.html'
    f = open(name, 'w+')
    f.write(html)
    f.close()
    webbrowser.open(name)


class ItemsNic(object):
    def __init__(self, res):
        pass

class Pycnic(object):
    def __init__(self, user,pwd):
        self.url = "https://nic.ar"
        self.br = Browser()
        self.tramites = []
        self.alertas = []
        self.br.addheaders = [('user-agent',
                               'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/28.0.1500.71 Chrome/28.0.1500.71 Safari/537.36'
                              )]
        self.login(user, pwd)

    def login(self, user, pwd):
        self.br.open(self.url)
        self.br.select_form(name="loginForm")
        self.br['loginForm:usuario'] = user
        self.br['loginForm:password'] = pwd
        self.br.form.controls.remove(self.br.form.controls[-2])
        res = self.br.submit()
        self.dominios = parse_dominios(res.read())

    def obtener_dominios(self):
        if self.dominios:
            return self.dominios
        else:
            res = self.br.open('https://nic.ar/misDominios.xhtml')
            self.dominios = parse_dominios(res.read())
            return self.dominios

    def obtener_tramites(self):
        if self.tramites:
            return self.tramites
        else:
            res = self.br.open('https://nic.ar/misTramites.xhtml')
            self.tramites = parse_tramites(res.read())
            return self.tramites

    def obtener_alertas(self):
        if self.alertas:
            return self.alertas
        else:
            res = self.br.open('https://nic.ar/alertas.xhtml')
            self.alertas = parse_alertas(res.read())
            return self.alertas



class Dominio(object):
    def __init__(self, dom):
        self.id = dom['id']
        self.url = dom['dominio']
        self.creado = dom['creado']
        self.vencimiento = dom['vencimiento']
        self.estado = dom['estado']
        self.mensajes = dom['mensajes']

    def delegar(self, dns=[None]):
        pass

def parse_dominios(html):
    soup = bs(html)
    vacio = soup.find('tr', {'class': 'ui-widget-content ui-datatable-empty-message'})
    if vacio:
        return 'No se encontraron datos'
    table = soup.find('tbody', {'id': 'misDominiosForm:tabla_data'})
    trs = table.findAll('tr')
    dominios = []
    for tr in trs:
        tds = tr.findAll('td',{'role': 'gridcell'})
        dom = {}
        dom['id'] = tr['data-ri']
        dom['dominio'] = tds[1].div.string
        dom['creado'] = tds[2].div.string
        dom['vencimiento'] = tds[3].div.string
        dom['estado'] = tds[4].div.string
        dom['mensajes'] = tds[5].div.string
        dominios.append(Dominio(dom))
    return dominios

def parse_tramites(html):
    soup = bs(html)
    table = soup.find('tbody', {'id': 'misTramitesForm:tabla_data'})
    trs = table.findAll('tr')
    tramites = []
    for tr in trs:
        tds = tr.findAll('td',{'role': 'gridcell'})
        tra = {}
        tra['id'] = tds[1].div.string
        tra['tramite'] = tds[2].div.string
        tra['comienzo'] = tds[3].div.string
        tra['fin'] = tds[4].div.string
        tra['estado'] = tds[5].div.string
        tra['dominio'] = tds[6].div.string
        tramites.append(tra)
    return tramites

def parse_alertas(html):
    soup = bs(html)
    table = soup.find('tbody', {'id': 'tabla_data'})
    trs = table.findAll('tr')
    alertas= []
    for tr in trs:
        tds = tr.findAll('td',{'role': 'gridcell'})
        ale = {}
        ale['fecha'] = tds[1].div.span.string
        ale['tramite'] = tds[2].div.span.string
        ale['estado'] = tds[3].div.span.string
        alertas.append(ale)
    return alertas
