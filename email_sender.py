import smtplib
import email.message

class EmailSender:
    def __init__(self, compra, oportunidade, janela_aberta,email_to,condition_compra,condition_oportunidade,condition_janela_aberta):
        self.compra = compra
        self.oportunidade = oportunidade
        self.janela_aberta = janela_aberta
        self.email_to=email_to
        self.condition_compra = condition_compra
        self.condition_oportunidade = condition_oportunidade
        self.condition_janela_aberta = condition_janela_aberta


    def enviar_email(self):  
        corpo_email = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{
            font-family: Arial, sans-serif;
            color: #333;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }}
        h2 {{
            border-bottom: 2px solid;
            padding-bottom: 10px;
        }}
        .compra h2 {{
            color: #e74c3c; /* Vermelho */
            border-color: #e74c3c;
        }}
        .oportunidade h2 {{
            color: #f39c12; /* Laranja */
            border-color: #f39c12;
        }}
        .janela-aberta h2 {{
            color: #2ecc71; /* Verde */
            border-color: #2ecc71;
        }}
        ul {{
            list-style-type: none;
            padding: 0;
        }}
        li {{
            background-color: #fff;
            margin-bottom: 5px;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }}
        .container {{
            max-width: 600px;
            margin: auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }}
        .explanation {{
            font-size: 14px;
            color: #555;
            margin-bottom: 20px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="compra">
            <h2>Compra</h2>
            <div class="explanation">
                {self.condition_compra}
            </div>
            <ul>
                {''.join([f'<li>{item}</li>' for item in self.compra])}
            </ul>
        </div>
        <div class="oportunidade">
            <h2>Oportunidade</h2>
            <div class="explanation">
                {self.condition_oportunidade}
            </div>
            <ul>
                {''.join([f'<li>{item}</li>' for item in self.oportunidade])}
            </ul>
        </div>
        <div class="janela-aberta">
            <h2>Janela Aberta</h2>
            <div class="explanation">
                {self.condition_janela_aberta}
            </div>
            <ul>
                {''.join([f'<li>{item}</li>' for item in self.janela_aberta])}
            </ul>
        </div>
    </div>
</body>
</html>
"""
        msg = email.message.Message()
        msg['Subject'] = "[ Oportunidades de Compras ] - Invest Bot"
        msg['From'] = 'avcl@cin.ufpe.br'
        msg['To'] = self.email_to
        password = 'qubvvfbuqykioaqh' 
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email )

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        # Login Credentials for sending the mail
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print('Email enviado')