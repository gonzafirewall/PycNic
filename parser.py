from BeautifulSoup import BeautifulSoup as bs

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
        dom['dominio'] = tds[1].div.string
        dom['creado'] = tds[2].div.string
        dom['vencimiento'] = tds[3].div.string
        dom['estado'] = tds[4].div.string
        dom['mensajes'] = tds[5].div.string
        dominios.append(dom)
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
    table = soup.find('tbody', {'id': 'alertasForm:tabla_data'})
    trs = table.findAll('tr')
    alertas= []
    for tr in trs:
        tds = tr.findAll('td',{'role': 'gridcell'})
        ale = {}
        ale['fecha'] = tds[1].div.string
        ale['tramite'] = tds[2].div.string
        ale['estado'] = tds[3].div.string
        alertas.append(ale)
    return alertas
