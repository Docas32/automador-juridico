# ⚖️ Automador Jurídico MVP: AI-Driven Document Processing

Este projeto é um MVP (Mínimo Produto Viável) desenvolvido para automatizar a triagem e análise de documentos em escritórios de advocacia. O foco é resolver o gargalo de casos com grande volume de PDFs, transformando dados não estruturados em informações acionáveis.

## 🚀 Funcionalidades
- **Ingestão de Dados:** Sistema de upload de documentos PDF via interface web.
- **Extração com LangChain:** Uso de PyPDFLoader para captura de texto e metadados.
- **Chunking Estratégico:** Segmentação de documentos longos com RecursiveCharacterTextSplitter para otimização de contexto e custo.
- **Classificação Inteligente:** Identificação automática de tipos de documentos (Petições, Contratos, Sentenças, etc.) via Gemini.
- **Extração Estruturada (JSON):** Geração automática de checklists contendo nomes das partes, datas, valores da causa e resumos executivos.

## 🛠️ Tech Stack
- **Linguagem:** Python 3.10+
- **IA Generativa:** Google GenAI SDK (Gemini 2.5 Flash)
- **Framework de Dados:** LangChain (Community & Text Splitters)
- **Interface:** Streamlit
- **Ambiente de Desenvolvimento:** Pop!_OS (Linux)

## 📦 Estrutura do Projeto
- `src/app.py`: Interface de usuário e orquestração da UI.
- `src/processor.py`: Lógica de extração de texto, tratamento de PDFs e chunking.
- `src/llm_engine.py`: Integração com a API do Gemini e engenharia de prompts.
- `data/`: Diretório para armazenamento temporário e testes de arquivos.

## 🔧 Como Executar
1. Clone este repositório.
2. Crie e ative seu ambiente virtual:
   `python3 -m venv .venv && source .venv/bin/activate`
3. Instale as dependências:
   `pip install -r requirements.txt`
4. Configure sua chave de API do Google em um arquivo `.env` na raiz:
   `GOOGLE_API_KEY=sua_chave_aqui`
5. Inicie a aplicação:
   `streamlit run src/app.py`

## 📈 Diferenciais Técnicos
Este projeto foi construído seguindo princípios de Engenharia de IA:
- **Modularidade:** Separação clara entre processamento de arquivos e lógica de LLM.
- **Eficiência de Tokens:** Classificação baseada no primeiro chunk relevante, reduzindo latência e custo de API.
- **Robustez:** Tratamento de documentos em múltiplos idiomas e formatos jurídicos variados.

---
Desenvolvido por João Nogueira Clemente - 2026