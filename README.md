# Stock Analysis

Este projeto realiza uma análise de ações utilizando dados da API Alpha Vantage. Ele gera gráficos e um relatório em PDF que mostra o histórico de preços de fechamento, a média dos últimos 60 dias e indica se a ação fechou em alta ou baixa em relação a essa média.

## Requisitos

- Python 3.x
- Bibliotecas:
  - `requests`
  - `pandas`
  - `matplotlib`

Você pode instalar as bibliotecas necessárias com:
```bash
pip install requests pandas matplotlib
```

## Explicação do Código
O script realiza as seguintes etapas:

Define um dicinário (stocks) com chaves (name e symbol) para serem analisadas, incluindo o nome e o símbolo de cada uma.
Para cada ação, faz uma requisição à API Alpha Vantage para obter os dados diários de fechamento.
Converte os dados recebidos em um DataFrame do pandas.
Calcula o preço de fechamento atual e a média dos últimos 60 dias.
Gera gráficos de preços de fechamento e adiciona uma linha horizontal para representar a média dos últimos 60 dias.
Cria um relatório em PDF que inclui os gráficos e uma mensagem indicando se a ação fechou em alta ou baixa em relação à média dos últimos 60 dias.

## Arquivo PDF Gerado
O script gera um arquivo PDF chamado stock_analysis.pdf que inclui:

Gráficos do histórico de preços de fechamento para cada ação.
Uma linha horizontal representando a média dos últimos 60 dias.
Mensagens indicando se a ação fechou em alta ou baixa em relação à média.

## Personalização
Você pode adicionar ou remover ações da lista stocks no código:
```python
stocks = 
    {"name": 'Apple Inc.', "symbol": 'AAPL'},
    {"name": 'Microsoft Corporation', "symbol": 'MSFT'},
    {"name": 'Amazon.com', "symbol": 'AMZN'},
    {"name": 'XP Inc.', "symbol": 'XP'},
```
## API Key
O script utiliza a API Alpha Vantage para obter os dados das ações. Substitua YOUR_API_KEY pela sua chave de API:

```python
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=compact&apikey={YOUR_API_KEY}&datatype=csv'
```
