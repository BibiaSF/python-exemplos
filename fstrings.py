#Formatação de Strings
from datetime import datetime
ano_atual = datetime.now().year
clube = 'Palmeiras'
ano_fundacao = 1914
campeonato_mundial = 0
print(f"{clube} possui {campeonato_mundial} títulos mundiais. ")
print(f" São {ano_atual - ano_fundacao} anos de existencia. ")
