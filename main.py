from email_sender import EmailSender 
from indicators_calc import IndicatorCalc

janela_aberta = []
oportunidade = []
compra = []
companies = ['KO','IAU', 'JNJ', 'VOO', 'TAEE4.SA', 'ITSA4.SA', 'TRPL4.SA', 'TOTS3.SA', 'WEGE3.SA', 'AGRO3.SA',
             'MCCI11.SA', 'BCFF11.SA', 'XPLG11.SA', 'BTAL11.SA', 'MXRF11.SA', 'TRXF11.SA', 'SNAG11.SA', 'XPML11.SA',
             'STAG', 'O', 'GOOGL', 'NVDA', 'NKE', 'SHY', 'IEI', 'IEF', 'BIL','BTC-USD','^BVSP','BRL=X','EURBRL=X']

for company in companies:
    indicators = IndicatorCalc(company)

    # Calculo dos indicadores
    rsi = indicators.calcular_rsi()
    media_movel_5= indicators.calcular_MM(5)
    media_movel_200 = indicators.calcular_MM(200)
    upper_bb=indicators.bollinger_bands('u')
    lower_bb=indicators.bollinger_bands()
    pvp=float(indicators.calcular_pvp())
    last_price=indicators.last_price()

    # Obtém o último valor do RSI
    last_rsi = rsi.iloc[-1]
    last_mm5 = media_movel_5.iloc[-1]
    last_mm200 = media_movel_200.iloc[-1]
    last_ubb= upper_bb.iloc[-1]
    last_lbb=lower_bb.iloc[-1]
    
    
    if  last_rsi < 43 and last_rsi> 37 and last_mm200>last_mm5:
        janela_aberta.append(company)
    elif 37 >= last_rsi > 30 and last_mm200>last_mm5:
        oportunidade.append(company)
    elif (last_rsi <= 30 and last_mm200>last_mm5 and last_lbb>last_price) or (last_rsi <= 30 and 0>pvp<1 and last_mm200>last_mm5 and last_lbb>last_price):
        compra.append(company)

print(janela_aberta,oportunidade,compra)

compra_condicao="O RSI está abaixo de 30, Média Móvel 200 dias é maior que a Média Móvel de 5 dias, Preço está abaixo da Lower Bollinger Band e/ou P/VA abaixou de 1"
oportu_condicao='O RSI está entre 37 e 30 e Média Móvel 200 dias é maior que a Média Móvel de 5 dias'
janela_condicao='O RSI está entre 43 e 37 e Média Móvel 200 dias é maior que a Média Móvel de 5 dias ou P/VPA < 1.'

email_sender = EmailSender(compra, oportunidade, janela_aberta,'andrecamposlu@gmail.com',compra_condicao,oportu_condicao,janela_condicao)
email_sender.enviar_email()