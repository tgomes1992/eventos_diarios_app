import pandas as pd
import requests
from datetime import datetime


df = pd.read_excel("eventos_diarios.xlsx").to_dict('records')

for item in df:
    item['emissor'] = "na"
    # item['data_liquidacao'] = datetime.strptime(item['data_liquidacao'] , "%d/%m/%Y")
    requests.post("http://127.0.0.1:5000/adicionar_eventos" ,  json=item)