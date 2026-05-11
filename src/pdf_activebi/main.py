import fitz
import os
import json
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
cliente = OpenAI()


def extrair_texto_pdf(caminho_pdf: str) -> str:
    documento = fitz.open(caminho_pdf)
    texto_completo = ""

    for pagina in documento:
        texto_completo += pagina.get_text()

    documento.close()
    return texto_completo

def analisar_documento(texto_pdf: str, pergunta: str, nome_arquivo: str) -> dict:
    system_prompt = """Você é um analisador especialista em documentos de négocio e BI.
    Ao receber um documento e uma pergunta, você DEVE responder EXCLUSIVAMENTE com um JSON válido
    no seguinte formato, sem nenhum texto fora do objeto JSON:

    {
    "type": "text",
    "text": "<resposta em Markdown com títulos, listas e destaques>",
    "source": "<nome ou título do documento>",
    "suggestions": ["<pergunta 1>", "<pergunta 2>", "<pergunta 3>"]
    }
 
    Regras:
    - O campo "text" deve usar Markdown rico: use ## para títulos, ** para negrito, - para listas
    - O campo "source" deve conter o nome ou título identificado no documento
    - O campo "suggestions" deve ter EXATAMENTE 3 perguntas relevantes de acompanhamento
    - Responda sempre em português
    - Nunca inclua texto, explicação ou markdown fora do objeto JSON"""

    user_prompt = f"""Documento analisado: {nome_arquivo}

    Conteúdo do documento:
    {texto_pdf}

    Pergunta: {pergunta}"""

    resposta = cliente.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        response_format={"type": "json_object"},
        temperature=0.3,
    )

    conteudo = resposta.choices[0].message.content
    return json.loads(conteudo), resposta.usage

if __name__ == "__main__":
    texto = extrair_texto_pdf("/home/lphillipe/Downloads/luisphillipedevops.pdf")
    resultado, uso = analisar_documento(texto, "Qual é o tema principal deste documento?", "luisphillipedevops.pdf")
    print(json.dumps(resultado, indent=2, ensure_ascii=False))