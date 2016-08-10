# coding: utf-8

import xmltodict
from suds.client import Client
from suds.transport.http import HttpAuthenticated


def get_dados(cpf):
    url_wsdl = 'http://maismedicos.saude.gov.br/new/web/app.php/services/profissional?wsdl'
    transport = HttpAuthenticated(username='MaisMedicos', password='YAWEqASpuvE7PuB2nEteSpuSt44ufRef')
    client = Client(url_wsdl, transport=transport, retxml=True, timeout=10)

    xml_data = client.service.getProfissional(cpf)
    data = xmltodict.parse(xml_data)['SOAP-ENV:Envelope'] \
                                    ['SOAP-ENV:Body'] \
                                    ['ns1:getProfissionalResponse'] \
                                    ['return']
    if 'erro' in data:
        return dict()
    parsed_data = dict()
    for key, value in data.items():
        if key.startswith('@xsi:type'):
            continue
        if '#text' in value:
            parsed_data[key] = value['#text']
        elif 'date' in value:
            parsed_data[key] = value['date']['#text'].split()[0]  # A hora sempre vem 00:00:00, o que é irrelevante

    return parsed_data
