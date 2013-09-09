from BeautifulSoup import BeautifulSoup as bs

def parse_mis_dominios(html):
    soup = bs(html)
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
    print dominios


if __name__ == "__main__":
    f = open('index.html', 'r+')
    parse_mis_dominios(f.read())
