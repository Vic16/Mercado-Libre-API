
#Para hacer llamados HTTP

import requests

#Para tener la data en formato tabla
import pandas as pd

#Para trabajar con el output de la llamada
import json

#Para agregar la fecha de la consulta
from datetime import date

#### Tendencias generales de ML


### Con el método get hacemos un llamado a la API para obtener los trends de búsqueda de Celulares
request = requests.get('https://api.mercadolibre.com/trends/MLA/MLA1055')

## Esperamos 200 como respuesta del servidor
print(request.status_code)

#request = json.loads(request.content)
#print(request)
#request = dict(request)
#request = pd.DataFrame(request)


#### Tomamos el contenido del json, quitando los headers y lo pasamos a DF de Pandas
request = pd.read_json(request.content)

#### Le agregamos la fecha
request["fecha"] =  date.today()
#request.head()


### Lo salvamos en formato csv.
request.to_csv("ML_trends.csv", index = False, header=False, mode = 'a', encoding = 'utf-8 sig')
