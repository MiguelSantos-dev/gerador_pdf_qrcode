# gerador_pdf_qrcode
 Projeto em Python 3.13 com FastAPI que transforma JSON em PDFs automáticos com layout padronizado, QR Code, e dados dinâmicos. Ideal pra gerar declarações de conteúdo ou documentos comerciais com estilo e praticidade. Tudo 100% via API!
# Gerador de PDFs com QRCodes via API - FastAPI + ReportLab

Este projeto é uma API REST desenvolvida com FastAPI que gera PDFs dinâmicos a partir de dados enviados via JSON. Os documentos simulam **Declarações de Conteúdo** com layout personalizado, preenchimento automático e inserção de QR Code.

## Tecnologias Utilizadas

- **Python 3.13**
- **FastAPI** para a criação da API
- **ReportLab** para manipulação de PDFs
- **Pydantic** para validação de dados
- **PyPDF (pypdf)** para manipulação de arquivos PDF como templates
- **dotenv** para gerenciamento de variáveis de ambiente

##  Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repo.git
   ```

2. Ative o ambiente virtual (já vem configurado):
   ```bash
   .\venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Inicie o servidor:
   ```bash
   uvicorn main_gerador_pdf_qrcode:app --reload
   ```

5. Acesse a documentação interativa:
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Exemplo de JSON

```json
{
  "nome_remetente": "João da Silva",
  "endereco_remetente": "Rua A, 123",
  "cidade_remetente": "São Paulo",
  "uf_remetente": "SP",
  "cep_remetente": "01000-000",
  "bens": [
    { "conteudo": "Camisa Polo", "qtd": "2", "valor": "100.00" },
    { "conteudo": "Tênis", "qtd": "1", "valor": "250.00" }
  ]
}
```

## Objetivo

O projeto foi desenvolvido com o objetivo de demonstrar domínio na criação de APIs modernas, geração de documentos dinâmicos e organização de código limpo e modularizado. Também serve como solução para empresas que precisam gerar documentos de transporte ou declarações comerciais com validação visual via QR Code.
