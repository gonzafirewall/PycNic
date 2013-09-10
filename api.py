from mechanize import Browser
import webbrowser
import sys
from parser import parse_dominios, parse_tramites, parse_alertas

def guardar(html):
    name = 'index.html'
    f = open(name, 'w+')
    f.write(html)
    f.close()
    webbrowser.open(name)


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

