#codigo que esta criando uma chave pix
from gerencianet import Gerencianet
from credenciais import CREDENTIALS

gn = Gerencianet(CREDENTIALS)

response =  gn.pix_create_evp()
print(response) #execultar isso depois de pegar as credenciais