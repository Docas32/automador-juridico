#Loading Libraries
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from llm_engine import classificar_documento_gemini, gerar_checklist_juridico




caminho_pdf = "/home/docas32/Documentos/automador-juridico/data/Orig_142_Report.pdf",
    # headers = None
    # password = None,
mode = "single",
pages_delimiter = ""
    # extract_images = True, # images_parser = RapidOCRBlobParser(),


def extrair_texto_juridico(caminho_pdf):
    """Extrai o texto bruto do PDF."""
    try:
        loader = PyPDFLoader(caminho_pdf)
        paginas = loader.load()
        return "\n".join([p.page_content for p in paginas])
    except Exception as e:
        return f"Erro na extração: {e}"


def dividir_texto(texto):
    """Divide o texto em pedaços (chunks) para processamento eficiente."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=3000,    # Tamanho ideal para capturar o contexto inicial
        chunk_overlap=300,   # Garante que termos jurídicos não sejam cortados ao meio
        separators=["\n\n", "\n", ".", " "]
    )
    return splitter.split_text(texto)


def executar_pipeline_completo(caminho_pdf):
    texto_bruto = extrair_texto_juridico(caminho_pdf)
    if "Erro" in texto_bruto:
        return {"erro": texto_bruto}

    chunks = dividir_texto(texto_bruto)
    
    # Executamos as duas tarefas de IA
    classificacao = classificar_documento_gemini(chunks[0])
    
    # Usamos o primeiro chunk (ou os dois primeiros) para o checklist
    checklist = gerar_checklist_juridico(chunks[0])
    
    return {
        "arquivo": os.path.basename(caminho_pdf),
        "classificacao": classificacao,
        "checklist": checklist,
        "quantidade_chunks": len(chunks),
        "texto_analisado": chunks[0][:500]
    }