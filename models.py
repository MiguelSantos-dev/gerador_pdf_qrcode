from pydantic import BaseModel
from typing import List

class Bem(BaseModel):
    conteudo: str
    qtd: str
    valor: str

class DadosPDF(BaseModel):
    nome_remetente: str
    endereco_remetente: str
    numero_remetente: str
    complemento_remetente: str
    cidade_remetente: str
    uf_remetente: str
    cep_remetente: str
    cpf_cnpj_remetente: str

    nome_destinatario: str
    endereco_destinatario: str
    numero_destinatario: str
    complemento_destinatario: str
    cidade_destinatario: str
    uf_destinatario: str
    cep_destinatario: str
    cpf_cnpj_destinatario: str

    bens: List[Bem]

    total_qtd: str
    total_valor: str
    peso_total: str

    url_qrcode: str