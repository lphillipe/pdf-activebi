# 📄 PDF ActiveBI — Analisador de Documentos com IA

Ferramenta de linha de comando que recebe um arquivo PDF e uma pergunta em linguagem natural,
e retorna insights estruturados usando a API da OpenAI.

## 🤖 Modelo utilizado

Foi utilizado o modelo `gpt-4o-mini` pelos seguintes motivos:

- **Custo-benefício**: significativamente mais barato que o `gpt-4o`, ideal para análise de documentos
- **Janela de contexto**: suporta até 128k tokens, comportando PDFs extensos
- **Qualidade**: inteligente o suficiente para análise de documentos de negócio e BI
- **JSON confiável**: segue instruções de formato com alta precisão via `response_format`

## 🚀 Como executar

### Pré-requisitos

- Python 3.11+
- [Poetry](https://python-poetry.org/docs/#installation) *(opcional)*

### Instalação com Poetry

```bash
git clone https://github.com/seu-usuario/pdf-activebi.git
cd pdf-activebi
poetry install
```

### Instalação sem Poetry (venv padrão)

```bash
git clone https://github.com/seu-usuario/pdf-activebi.git
cd pdf-activebi

python3 -m venv .venv
source .venv/bin/activate        # Linux/macOS
# ou
.venv\Scripts\activate           # Windows

pip install openai pymupdf python-dotenv
```

### Configuração

Crie um arquivo `.env` na raiz do projeto com sua chave da OpenAI:

```bash
cp .env.example .env
```

Edite o `.env`:

```
OPENAI_API_KEY=sua_chave_aqui
```

### Uso

```bash
# Com Poetry
poetry run python src/pdf_activebi/main.py <caminho_do_pdf> "<pergunta>"

# Com venv
python src/pdf_activebi/main.py <caminho_do_pdf> "<pergunta>"
```

### Exemplo

```bash
poetry run python src/pdf_activebi/main.py relatorio.pdf "Quais são os principais indicadores?"
```

### Saída

```json
{
  "type": "text",
  "text": "## Principais Indicadores\n...",
  "source": "relatorio.pdf",
  "suggestions": [
    "Qual o crescimento em relação ao período anterior?",
    "Quais regiões tiveram melhor desempenho?",
    "Quais metas não foram atingidas?"
  ]
}

--- Estimativa de custo ---
Tokens input:  945
Tokens output: 203
Custo total:   U$ 0.000264
```

## 📦 Dependências

| Biblioteca | Finalidade |
|---|---|
| `openai` | SDK oficial da OpenAI |
| `pymupdf` | Extração de texto de arquivos PDF |
| `python-dotenv` | Leitura de variáveis de ambiente |