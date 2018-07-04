import json
import requests
from datetime import datetime, date, time, timedelta

#apikey de la aemet
apikey = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhaXJlYW5hbHl0aWNzQG91dGxvb2suZXMiLCJqdGkiOiI0OWM0NTBjMy1lM2U3LTQ3OGMtODhkOS1mNjg4N2QyNWIzZmQiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTUzMDcxNzk5NSwidXNlcklkIjoiNDljNDUwYzMtZTNlNy00NzhjLTg4ZDktZjY4ODdkMjViM2ZkIiwicm9sZSI6IiJ9.lOFwRMaV2YOefcEt6aVxGoXH-3HO-y3AuYt6NZw7Q7w"

#formato de las fechas y fecha inicial
dateFormat = "%Y-%m-%d"
dateIni = datetime.strptime("2010-01-01",dateFormat)
#ponemos fin en el 1 de junio de 2018
dateStop = datetime.strptime("2018-06-01",dateFormat)
#for i in range(1,12):
while (dateIni<dateStop):
	#sumo 30 dias
	dateEnd = dateIni+timedelta(days=30)
	# Aplica el formato
	fechaIni = dateIni.strftime(dateFormat)   
	fechaFin = dateIni.strftime(dateFormat)
	#paso la fecha final como incial para la siguiente iteración
	dateIni = dateEnd
	print(dateEnd)
	#consulto la api y recupero el json
	url="https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/"+fechaIni+"T00:00:00UTC/fechafin/"+fechaFin+"T23:59:59UTC/estacion/3195/?api_key="
	requestString=url+apikey

def consultaAEMET(requestString):
	res = requests.get(requestString)
	data = json.loads(res.text)

	#con el json de la primera consulta tengo la url de los datos, que es otro json
	res = requests.get(data['datos'])
	data = json.loads(res.text)
	return data
