from BeautifulSoup import BeautifulSoup as bs

def parse_mis_dominios(html):
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
        dom['domain'] = tds[1].div.string
        dom['created_at'] = tds[2].div.string
        dom['expire'] = tds[3].div.string
        dom['state'] = tds[4].div.string
        dom['messages'] = tds[5].div.string
        dominios.append(dom)
    return dominios

def parse_mis_tramites(html):
    soup = bs(html)
    table = soup.find('tbody', {'id': 'misTramitesForm:tabla_data'})
    trs = table.findAll('tr')
    tramites = []
    for tr in trs:
        tds = tr.findAll('td',{'role': 'gridcell'})
        tra = {}
        tra['id'] = tds[1].div.string
        tra['tramite'] = tds[2].div.string
        tra['start'] = tds[3].div.string
        tra['end'] = tds[4].div.string
        tra['status'] = tds[5].div.string
        tra['domain'] = tds[6].div.string
        tramites.append(tra)
    return tramites
