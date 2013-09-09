from mechanize import Browser
import webbrowser
import sys


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
        guardar(res.read())

if __name__ == "__main__":
    p = Pycnic("user", "pass")
