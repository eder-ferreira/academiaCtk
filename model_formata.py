from datetime import datetime    
import random
import string

class Formata:
    def obter_data_formatada(self):
        agora = datetime.now()
        data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
        return data_formatada

    def gerar_matricula():
        # Gere uma sequência aleatória de 7 dígitos
        matricula = ''.join(random.choices(string.digits, k=7))
        return matricula