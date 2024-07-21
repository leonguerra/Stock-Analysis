from io import StringIO
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.backends.backend_pdf import PdfPages

stocks = [
    {"name": 'Apple Inc.', "symbol": 'AAPL'},
    {"name": 'Microsoft Corporation', "symbol": 'MSFT'},
    {"name": 'Amazon.com', "symbol": 'AMZN'},
    {"name": 'XP Inc.', "symbol": 'XP'},
]

with PdfPages('stock_analysis.pdf') as pdf:

    for stock in stocks:
        symbol = stock["symbol"]
        name = stock["name"]
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=compact&apikey={YOUR_API_KEY}&datatype=csv'
        response = requests.get(url)
        data = response.content.decode('utf-8')

        df = pd.read_csv(StringIO(data), delimiter=',')
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df.set_index('timestamp', inplace=True)

        close_today = df['close'].iloc[0]
        media_60 = df['close'][1:61].mean()
        percentage = ((close_today - media_60) / media_60) * 100

        if close_today > media_60:
            line_color = 'green'
        else:
            line_color = 'red'

        plt.figure(figsize=(10, 5))
        plt.plot(df.index, df['close'], label=f'{name} - Fechamento', color=f'{line_color}')
        plt.axhline(y=media_60, xmin=0.4, xmax=0.95, color='blue', linestyle='--', label=f'Média Últimos 60 Dias: ${media_60:.2f}')
        plt.title(f'Histórico de Preços da Ação {name} ({symbol})')
        plt.xlabel('Data')
        plt.ylabel('Preço de Fechamento (USD)')
        plt.legend()
        plt.grid(True)
        pdf.savefig()
        plt.close()
        
        fig, ax = plt.subplots(figsize=(10, 2))
        ax.axis('off')
        if close_today > media_60:
            text = f'A ação {name} fechou hoje em ALTA ({percentage:.2f}% | ${close_today}) em relação ao período analisado'
            ax.text(0.5, 0.5, text, transform=ax.transAxes, ha='center', va='center', color='green')
        else:
            text = f'A ação {name} fechou hoje em BAIXA ({percentage:.2f}% | ${close_today}) em relação ao período analisado'
            ax.text(0.5, 0.5, text, transform=ax.transAxes, ha='center', va='center', color='red')
        
        pdf.savefig(fig)
        plt.close(fig)
