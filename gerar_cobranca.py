from gerencianet import Gerencianet
from credenciais import CREDENTIALS
import base64

gn = Gerencianet(CREDENTIALS)

body = {
    'calendario': {
        'expiracao': 3600
    },
    'devedor': {
        'cpf': '17420896070',
        'nome': 'Fulano de Tal'
    },
    'valor': {
        'original': '0.01'
    },
    'chave': 'c1dcc7a1-1d7f-41c8-ad61-5c216bea1b91',#a chave pix que eu gerei
    'solicitacaoPagador': 'Cobrança dos serviços prestados.'
}

response =  gn.pix_create_immediate_charge(body=body)
print(response)

params = {
    'id': response['loc']['id']
}

response =  gn.pix_generate_QRCode(params=params)
print(response)

#Generate QRCode Image
if('imagemQrcode' in response):
    with open("qrCodeImage.png", "wb") as fh:
        fh.write(base64.b64decode(response['imagemQrcode'].replace('data:image/png;base64,', '')))