import pandas as pd
import os
from datetime import datetime

def consolidar_planilhas_vendas(pasta_entrada, arquivo_saida): #pasta_entrada: pasta com arquivos excel"
                                                            #arquivos_saida: nome do arquivo consolidado"
    lista_dfs = [] #Lista para armazenar datas frames"
    print("Procurando arquivso")
    for arquivo in os.listdir(pasta_entrada):
        if arquivo.endswith(('.xlsx', 'xls')):
            caminho_completo = os.path.join(pasta_entrada, arquivo)

            try:
                print(f"lendo: {arquivo}")
                df = pd.read_excel(caminho_completo)
                df.columns = range(len(df.columns))
                df["arquivo_origem"] = arquivo

                lista_dfs.append(df) #Adiciona a lista"

            except Exception as e:
                print(f"Erro ao ler {arquivo}: {e}")

    if not lista_dfs:
        print("Nenhum arquivo encontrado")
        return

    print(f"\n consolidando {len(lista_dfs)} arquivos...")
    df_consolidado = pd.concat(lista_dfs, ignore_index=True)

    df_consolidado["data_processamento"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    df_consolidado.to_excel(arquivo_saida, index=False)

    print(f"\n Consolidação Concluída")
    print(f"Arquivo salvo: {arquivo_saida}")
    print(f"Total de registros: {len(df_consolidado)}")
    print(f"COlunas: {','.join(map(str, df_consolidado.columns))}")

    return df_consolidado

def analise_basica(df):
    print(f"\n" + "="*50)
    print(f"Analise dos dados")
    print("="*50)

    print(f"\n Total de linhas: {len(df)}")
    print(f" Total de colunas: {len(df.columns)}")

    print("\n Valores nulos por coluna:")
    nulos = df.isnull().sum()
    if nulos.sum() > 0:
        print(nulos[nulos > 0])
    else:
        print("Nenhum valor nulo encontrando")
    
    colunas_valor = [col for col in df.columns if "valor" in str(col).lower() or 'preco' in str(col).lower()]
    if colunas_valor:
        print(f"\n Estatisticas de {colunas_valor[0]}:")
        print(f" Total: R$ {df[colunas_valor[0]].sum():,.2f}")
        print(f" Media: R$ {df[colunas_valor[0]].mean():,.2f}")
        print(f"Minimo: R$ {df[colunas_valor[0]].min():,.2f}")
        print(f" Maximo: R$ {df[colunas_valor[0]].max():,.2f}")

if __name__ == "__main__":

    pasta_vendas = "/home/alan/Downloads/files/"
    arquivo_final = "vendas_consolidadas.xlsx"

    df_resultado = consolidar_planilhas_vendas(pasta_vendas, arquivo_final)

    if df_resultado is not None:
        analise_basica(df_resultado)
