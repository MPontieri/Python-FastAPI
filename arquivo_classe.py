from gerencianet import Gerencianet
from credenciais import CREDENTIALS
import base64

class sistema_restaurante:
    def __init__(self):    
        self.certificate = 'producao-531263-apirestaurante_cert.pem'
        self.client_secret = 'Client_Secret_87943b7980436a31a8c51bcfe3dd203a62edb1e1'
        self.headers = {'x-skip-mtls-checking': 'false'}
        self.id = 'Client_Id_e5d13262e8dbd4d8ab686448afc34ce9223cd83c'
        self.pix_chave = ''  # Armazenar a chave Pix gerada

    def cria_chave_pix(self):
        gn = Gerencianet(CREDENTIALS)
        response = gn.pix_create_evp()
        self.pix_chave = response['chave']
        print(response)

    def gerar_cobranca(self):
        gn = Gerencianet(CREDENTIALS)

        body = {
            'calendario': {'expiracao': 3600},
            'devedor': {'cpf': '', 'nome': ''},
            'valor': {'original': '0.01'},
            'chave': self.pix_chave,
            'solicitacaoPagador': 'Cobrança dos serviços prestados.'
        }

        response = gn.pix_create_immediate_charge(body=body)
        print(response)

        params = {'id': response['loc']['id']}

        response = gn.pix_generate_QRCode(params=params)
        print(response)

        # Gerar QRCode Image
        if 'imagemQrcode' in response:
            with open("qrCodeImage.png", "wb") as fh:
                fh.write(base64.b64decode(response['imagemQrcode'].replace('data:image/png;base64,', '')))

    def vincular_url(self, webhook_url):
        gn = Gerencianet(CREDENTIALS)

        headers = {'x-skip-mtls-checking': 'false'}

        params = {'chave': self.pix_chave}

        body = {'webhookUrl': webhook_url}

        response = gn.pix_config_webhook(params=params, body=body, headers=headers)
        print(response)


# Exemplo de uso
sistema = SistemaRestaurante()
sistema.cria_chave_pix()

# Após a criação da chave Pix, você pode gerar a cobrança e vincular a URL do webhook.
sistema.gerar_cobranca()
sistema.vincular_url('https://codft.me/webhookgn')

#


                

        