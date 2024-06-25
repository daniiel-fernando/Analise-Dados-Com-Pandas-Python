import pandas as pd
import os

def load_data(file_path, create_if_not_exist=True, data_if_empty=None):
    if not os.path.exists(file_path):
        if create_if_not_exist:
            # Cria o arquivo se ele não existir
            with open(file_path, 'w') as f:
                if data_if_empty:
                    f.write(data_if_empty)
            print(f'Arquivo {file_path} criado.')
        else:
            raise FileNotFoundError(f'O arquivo {file_path} não existe.')

    # Carrega os dados do arquivo CSV
    df = pd.read_csv(file_path)

    # Se o arquivo estiver vazio e data_if_empty não for None, adicione os dados
    if df.empty and data_if_empty is not None:
        with open(file_path, 'w') as f:
            f.write(data_if_empty)
        print(f'Dados adicionados ao arquivo {file_path}.')

    return df
