import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

def obter_cliente_gemini():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("A chave GOOGLE_API_KEY não foi encontrada!")
    return genai.Client(api_key=api_key)


def classificar_documento_gemini(texto_documento):
    """
    Usa o SDK do Google GenAI para classificar o documento.
    """
    client = obter_cliente_gemini()
    
    # Prompt de Sistema (Configuração do Modelo)
    instrucoes = """
    Você é um assistente jurídico brasileiro especializado em classificação de documentos.
    Analise o texto fornecido e retorne APENAS a categoria do documento.
    CCategorias aceitas: 
- PETIÇÃO INICIAL
- CONTRATO
- SENTENÇA  
- PROCURAÇÃO
- OUTRO.
    Se for OUTRO, descreva em no máximo 3 palavras (ex: OUTRO - Comprovante de Residência).
    """

    try:
        response = client.models.generate_content(
            model="models/gemini-2.5-flash",
            config={
                "system_instruction": instrucoes,
                "temperature": 0.1 # Baixa temperatura para manter a classificação rígida
            },
            contents=texto_documento
        )
        return response.text.strip()
    
    except Exception as e:
        return f"Erro na API do Google: {e}"
    
   
        

def gerar_checklist_juridico(texto_documento):
    """
    Analisa o documento e extrai um checklist de informações vitais.
    """
    client = obter_cliente_gemini()
    
    instrucoes = """
    Você é um analista jurídico. Sua tarefa é extrair informações estruturadas para um checklist.
    Retorne um objeto JSON com os seguintes campos:
    - partes_envolvidas: lista com nomes dos autores/réus ou contratantes.
    - data_documento: data principal identificada.
    - valor_causa_ou_contrato: valor monetário, se houver.
    - resumo_curto: resumo de 2 frases do objetivo do documento.
    - acao_recomendada: qual o próximo passo lógico para um advogado.
    """

    try:
        response = client.models.generate_content(
            model="models/gemini-2.5-flash",
            config={
                "system_instruction": instrucoes,
                "temperature": 0.1,
                "response_mime_type": "application/json" # Força o retorno em JSON
            },
            contents=texto_documento
        )
        # O SDK retorna uma string JSON, vamos convertê-la para dicionário Python
        import json
        return json.loads(response.text)
    
    except Exception as e:
        return {"erro": f"Erro na geração do checklist: {e}"}
    

