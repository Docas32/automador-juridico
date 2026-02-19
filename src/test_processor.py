from processor import executar_pipeline_completo
import os


def rodar_teste_integrado():
    # 1. Configuração do caminho do arquivo de teste
    # Busca um PDF na pasta 'data' na raiz do projeto
    pasta_projeto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    caminho_pdf = os.path.join(pasta_projeto, "data", "Orig_142_Report.pdf")

    print(" [TESTE] Iniciando validação do pipeline...")

    # 2. Verificação de existência do arquivo
    if not os.path.exists(caminho_pdf):
        print(f" [ERRO] Arquivo não encontrado em: {caminho_pdf}")
        print(" Dica: Coloque um PDF real na pasta 'data' e nomeie como 'contrato_teste.pdf'.")
        return

    # 3. Execução do Pipeline (Extração + Chunking + Gemini)
    try:
        resultado = executar_pipeline_completo(caminho_pdf)

        if "erro" in resultado:
            print(f" [FALHA NO PIPELINE] {resultado['erro']}")
            return

        # 4. Exibição dos Resultados (O que brilha no portfólio)
        print("\n" + "="*40)
        print(" TESTE CONCLUÍDO COM SUCESSO")
        print("="*40)
        print(f" Arquivo:      {resultado['arquivo']}")
        print(f"  Classificação: {resultado['classificacao']}")
        print(f" Chunks (Eng): {resultado['quantidade_chunks']} pedaços gerados")
        print(f" Amostra lida:  {resultado['texto_analisado']}...")
        print("="*40 + "\n")

    except Exception as e:
        print(f" [ERRO CRÍTICO] Ocorreu uma falha inesperada: {e}")

if __name__ == "__main__":
    rodar_teste_integrado()