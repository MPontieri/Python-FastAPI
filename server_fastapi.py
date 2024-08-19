from fastapi import FastAPI, Body, HTTPException, status
from pydantic import BaseModel
from typing import List, Annotated
import json

class PixInfo (BaseModel):
    txid: str
    endToEndId : str
    chave : str
    valor : str
    horario : str
    infoPagador : str

app = FastAPI()

@app.post('/gerar_cobranca/{id_pedido}')
async def gerar_cobranca(id_pedido : int):
    return {
        'tx_id' : 'a4ebb0bffc534663abbd4feb1904cade',
        'link_qrcode' : '00020101021226830014BR.GOV.BCB.PIX2561qrcodespix.sejaefi.com.br/v2/b243c1492d9343679f9a6c111db3107c5204000053039865802BR5905EFISA6008SAOPAULO62070503***630484D7',
        'imagem_qrcode_b64' : 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOQAAADkCAYAAACIV4iNAAAAAklEQVR4AewaftIAAAxASURBVO3BQW4kQZIgQdUA//9lnbqtzcWBQCbZPr0mYv+w1rrCw1rrGg9rrWs8rLWu8bDWusbDWusaD2utazysta7xsNa6xsNa6xoPa61rPKy1rvGw1rrGw1rrGg9rrWs8rLWu8cOHVP5SxRsqU8V/kspUMalMFScqv6niRGWqmFSmim9SmSomlb9U8Ym...'
    }

'''
{'calendario': {'criacao': '2023-12-19T23:55:47.798Z', 'expiracao': 3600}, 'txid': 'a4ebb0bffc534663abbd4feb1904cade', 'revisao': 0, 'loc': {'id': 1, 'location': 'qrcodespix.sejaefi.com.br/v2/b243c1492d9343679f9a6c111db3107c', 'tipoCob': 'cob', 'criacao': '2023-12-19T23:55:47.926Z'}, 'location': 'qrcodespix.sejaefi.com.br/v2/b243c1492d9343679f9a6c111db3107c', 'status': 'ATIVA', 'devedor': {'cpf': '91361609036', 'nome': 'fulano'}, 'valor': {'original': '0.01'}, 'chave': 'c1dcc7a1-1d7f-41c8-ad61-5c216bea1b91', 'solicitacaoPagador': 'Cobrança dos serviços prestados.'}
'''

# endpoint para chamada do webhook PIX
@app.post('/pix')
async def webhook(pix : Annotated[List[PixInfo], Body(embed=True)]):
    L = []
    for p in pix :
        print (p.txid)
        L.append(p)
    
    return {'list' : L}
    

'''
{
  "pix": [
    {
      "endToEndId": "E1803615022211340s08793XPJ",
      "txid": "fc9a43k6ff384ryP5f41719",
      "chave": "2c3c7441-b91e-4982-3c25-6105581e18ae",     
      "valor": "0.01",
      "horario": "2020-12-21T13:40:34.000Z",
      "infoPagador": "pagando o pix"
    },
    {
      "endToEndId": "E1803615022211340s08793XPJ",
      "txid": "fc9a43k6ff384ryP5f41719",
      "chave": "zzz7441-b91e-4982-3c25-6105581e18ae",     
      "valor": "1.01",
      "horario": "2020-12-21T13:40:34.000Z",
      "infoPagador": "pagando o pix"
    },
    {
      "endToEndId": "E1803615022211340s08793XPJ",
      "txid": "abca43k6ff384ryP5f41719",
      "chave": "2c3c7441-b91e-4982-3c25-6105581e18ae",     
      "valor": "15.10",
      "horario": "2020-12-21T13:40:34.000Z",
      "infoPagador": "pagando o pix"
    }
  ]
}
'''