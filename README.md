**# Projeto de Análise de Dados

Este projeto demonstra um exemplo básico de análise de dados utilizando Python e Pandas. Ele inclui a carga de dados a partir de arquivos CSV, limpeza dos dados, análise exploratória, análise detalhada e visualização dos resultados.

## Estrutura do Projeto

O projeto está estruturado da seguinte forma:

**# Projeto de Análise de Dados - Desafio DIO

Este projeto foi desenvolvido como parte do Desafio da Digital Innovation One (DIO), onde estou estudando análise de dados utilizando Python e bibliotecas como pandas, matplotlib e outras.

## Descrição

Este projeto consiste em um sistema de análise de dados que carrega informações de vendas, clientes e produtos a partir de arquivos CSV. Ele realiza limpeza dos dados, análises exploratórias e gera visualizações gráficas para facilitar a interpretação dos resultados.

## Funcionalidades

- **Carregamento de Dados:** Os dados são carregados a partir de arquivos CSV (`orders.csv`, `customers.csv`, `products.csv`). Caso os arquivos não existam, eles são criados com dados de exemplo.
  
- **Limpeza de Dados:** Remove duplicatas e converte colunas de datas para o formato apropriado (datetime).
  
- **Análise Exploratória:** Calcula estatísticas descritivas e gera gráficos de séries temporais das vendas.
  
- **Análise Detalhada:** Realiza análises mais profundas, como identificação de sazonalidade nas vendas e segmentação de clientes.
  
- **Visualização:** Utiliza gráficos para visualizar as vendas mensais e outras métricas relevantes.

## Pré-requisitos

- Python 3.x instalado
- Bibliotecas Python: pandas, matplotlib

## Como Usar

1. Clone o repositório para sua máquina local:

https://github.com/daniiel-fernando/Analise-Dados-Com-Pandas-Python.git


2. Instale as bibliotecas necessárias:

pip install -r requirements.txt


3. Execute o script principal `main.py`:

python main.py


## Estrutura de Arquivos

- `main.py`: Script principal que orquestra o carregamento de dados, limpeza, análises e visualizações.
- `data_loader.py`: Funções para carregar os dados a partir dos arquivos CSV, criando-os se necessário.
- `data_cleaner.py`: Classe `DataCleaner` para a limpeza e preparação dos dados.
- `eda.py`: Módulo para Análise Exploratória de Dados (EDA), como estatísticas descritivas e gráficos.
- `analysis.py`: Módulo para análises mais detalhadas, como sazonalidade e segmentação de clientes.
- `visualization.py`: Funções para criação de gráficos utilizando matplotlib.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para propor melhorias através de pull requests.

## Autor

Seu Nome - [Seu GitHub](https://github.com/seu-usuario)

## Licença

Este projeto está licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT).
