import streamlit as st
import os
from processor import executar_pipeline_completo




# Configuração da página
st.set_page_config(page_title="Automador Jurídico MVP", page_icon="⚖️", layout="wide"  )

st.title("⚖️ Automador Jurídico")
st.markdown("---")

st.sidebar.header("Configurações")
st.sidebar.info("Este MVP processa PDFs e utiliza o Gemini para classificação.")

# 1. Upload do Arquivo
uploaded_file = st.file_uploader("Carregue o documento PDF (Petição, Contrato, etc.)", type="pdf")

if uploaded_file is not None:
    # Salva temporariamente o arquivo na pasta data/ para o processador ler
    caminho_temp = os.path.join("data", uploaded_file.name)
    with open(caminho_temp, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"Arquivo '{uploaded_file.name}' carregado com sucesso!")

    # 2. Botão para Iniciar Processamento
    if st.button("Analisar Documento"):
        with st.spinner("🤖 O Gemini está analisando o documento..."):
            # Chama o pipeline que você construiu e validou
            resultado = executar_pipeline_completo(caminho_temp)

        if "erro" in resultado:
            st.error(f"Erro no processamento: {resultado['erro']}")
        else:
            # 3. Exibição dos Resultados
            st.markdown("### 📋 Resultado da Análise")
            
            with st.container():
                col1, col2, col3 = st.columns([2, 1, 1]) # Define proporções fixas para as colunas
                with col1:
                    st.metric(label="Classificação", value=resultado["classificacao"])
                with col2:
                    st.metric(label="Blocos", value=resultado["quantidade_chunks"])
                with col3:
                    st.metric(label="Status", value="✅ Processado")

            st.subheader("📝 Resumo da Amostra Analisada")
            st.text_area("Texto extraído (primeiro bloco):", 
                         value=resultado["texto_analisado"], 
                         height=200)
            
            # 4. Simulação de Organização em Pastas (Requisito da vaga)
            st.info(f"Sugestão de destino: `/documentos/juridico/{resultado['classificacao'].replace(' ', '_').lower()}/`")

            if "erro" not in resultado:
                st.subheader("📋 Checklist do Documento")
                checklist = resultado["checklist"]
                
                # Layout em colunas para o checklist
                c1, c2, c3 = st.columns(3)
                c1.write(f"**Partes:** {', '.join(checklist.get('partes_envolvidas', ['Não encontrado']))}")
                c2.write(f"**Data:** {checklist.get('data_documento', 'N/A')}")
                c3.write(f"**Valor:** {checklist.get('valor_causa_ou_contrato', 'N/A')}")
                
                st.write(f"**Resumo:** {checklist.get('resumo_curto')}")
                st.warning(f"💡 **Ação Recomendada:** {checklist.get('acao_recomendada')}")



# Rodapé
st.markdown("---")
st.caption("Desenvolvido por João Nogueira Clemente - 2026")