# main_gerador_pdf_qrcode.py
from fastapi import FastAPI
from fastapi.responses import FileResponse
from models import DadosPDF
from services.gerador_template import gerar_template
from services.preencher_pdf import preencher_dados_pdf
import os

app = FastAPI()

@app.post("/gerar-pdf")
def gerar_pdf(dados: DadosPDF):
    base_dir = os.path.dirname(__file__)
    pasta_saida = os.path.join(base_dir, "saida_pdfs")
    os.makedirs(pasta_saida, exist_ok=True)

    # 1️⃣ Gerar template em branco
    caminho_template = os.path.join(pasta_saida, "template_declaracao_corrigido.pdf")
    gerar_template(caminho_template)

    # 2️⃣ Preencher o template com os dados recebidos
    caminho_pdf_final = os.path.join(pasta_saida, "declaracao_preenchida.pdf")
    preencher_dados_pdf(caminho_template, dados, caminho_pdf_final)

    # 3️⃣ Retornar o arquivo gerado
    return FileResponse(path=caminho_pdf_final, filename="declaracao_preenchida.pdf", media_type="application/pdf")
