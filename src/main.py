import pandas as pd 
import os 
import glob

# caminho para ler os arquivos 
folder_path = 'src\\data\\raw'

#lista todos os arquivos de excel
excel_files = glob.glob(os.path.join(folder_path,'*.xlsx'))

if not excel_files:
    print("Nenhum arquivo compativel encontrado")
else:
    
    #dataframe = tabela na memoria para guardar conteudos dos arquivos
    dfs = []

    for excel_file in excel_files:
        
        try:
            #leio o arquivo de excel
            df_temp = pd.read_excel(excel_file)

            #pega o nome do arquivo
            file_name = os.path.basename(excel_file)

            df_temp['file_name'] = file_name
            
            #tratamento de criacao de coluna location
            if 'brasil' in file_name.lower():
                df_temp['location'] = 'br'
            elif 'france' in file_name.lower():
               df_temp['location'] = 'fr'
            elif 'italian' in file_name.lower():
                df_temp['location'] = 'it'
           

            #criar uma coluna de campanha
            df_temp['campaign'] = df_temp['utm_link'].str.extract(r'utm_campaign=(.*)')

            #guardar os dados tratados de uma dataframe comum
            dfs.append(df_temp)
            

        except Exception as e:
            print(f"Erro ao ler o Arquivo {excel_file} : {e}")

if dfs:
    #concatena as tabelas salvas em uma unica tambem
    result = pd.concat(dfs, ignore_index=True)

    #caminho de saida
    output_file = os.path.join('src','data', 'ready', 'clean.xlsx')

    #configuracao do motor de escrita (alteracao de engine)
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter')

    #leva os dados do resultado para serem escritos no excel
    result.to_excel(writer, index=False)
    #salva o arquivo
    writer._save()
else:
    print("nenhum dado para ser salvo")