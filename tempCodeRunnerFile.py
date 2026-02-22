import pandas as pd
import os
from datetime import datetime

def consolidar_planilhas_vendas(pasta_entrada, arquivo_saida): "pasta_entrada: pasta com arquivos excel"
                                                            "arquivos_saida: nome do arquivo consolidado"
    lista_dfs = [] "Lista para armazenar datas frames"
    print("Procurando arquivso")
    for arquivo in os.listdir(pasta_entrada):
        if arquivo.endswith(('.xlsx', 'xls')):
            caminho_completo = os.path.join(pasta_entrada, arquivo)

            try:
                print(f"lendo: {arquivo}")
                df = pd.read_excel(caminho_completo):

                df["arquivo_origem"] = arquivo

                lista_dfs.append(df) "Adiciona a lista"

            except Exception as e:
                print(f"Erro ao ler {arquivo}: {e}")

    if not list_dfs
        print("Nenhum arquivo encontrado")\
        return

    print(f"\n consolidando {len(lista_dfs)} arquivos...")
    df_consolidado = pd.concat(lista_dfs, ignore_index=True)

    df_consolidado["data_processamento"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    df_consolidado.to_excel(arquivo_saida, index=False)

    print(f"\n Consolidação Concluída")
    print(f"Arquivo salvo: {arquivo_saida}")
    print(f"Total de registros: {len(df_consolidado)}")
    print(f"COlunas: {','.join(df_consolidado.columns)}")

    return df_consolidado