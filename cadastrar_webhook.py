#codico para vincular uma url de notificaçao

from gerencianet import Gerencianet
from credenciais import CREDENTIALS

gn = Gerencianet(CREDENTIALS)

headers = {
    'x-skip-mtls-checking': 'false'
}

params = {
    'chave': 'c1dcc7a1-1d7f-41c8-ad61-5c216bea1b91'#colocacar a chave pix que o codigo anterior vai gerar
}

# body = {
#     'webhookUrl': ''#configurar o webhook https://codft.me/webhookgn
# }

response =  gn.pix_config_webhook(params=params,  headers=headers)#body=body,
print(response)