import yfinance as yf
import pandas as pd
class IndicatorCalc:
    def __init__(self, company):
        self.ticker = yf.Ticker(company)
        self.df_stock = self.ticker.history(interval='1d', period='max')
 
    def calcular_rsi(self):
        # Calcula as variações diárias de fechamento
        change = self.df_stock["Close"].diff()
        change.dropna(inplace=True)

        # Cria duas cópias da série de mudanças
        change_up = change.copy()
        change_down = change.copy()

        # Define os valores negativos para 0
        change_up[change_up < 0] = 0
        change_down[change_down > 0] = 0

        # Calcula a média móvel exponencial (EMA) para os ganhos e perdas
        avg_up = change_up.ewm(span=14, adjust=False).mean()
        avg_down = change_down.ewm(span=14, adjust=False).mean().abs()

        # Calcula o RSI
        rsi = 100 - (100 / (1 + avg_up / avg_down))

        return rsi
    def calcular_MM(self,days):
        self.df_stock["SMA"] = self.df_stock["Close"].rolling(window=days).mean()
        return self.df_stock["SMA"]
    def calcular_pvp(self):
        pvp = self.ticker.info.get('priceToBook', None)
        if pvp==None:
            pvp=0
        
        return pvp
    def bollinger_bands(self,situation='d'):
        aux_stock=self.calcular_MM(20)
        if situation=='u':
            self.df_stock['UBB']=aux_stock + 2*self.df_stock['Close'].rolling(window=20).std()
            return self.df_stock['UBB']
        else:
            self.df_stock['LBB']=aux_stock - 2*self.df_stock['Close'].rolling(window=20).std()
            return self.df_stock['LBB']
    def last_price (self):
        self.lastprice = self.df_stock['Close'].iloc[-1]
        return self.lastprice