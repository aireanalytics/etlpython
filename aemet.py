import json
import requests
import time
from datetime import datetime, timedelta

#función de consulta a la aemet que recoge la url de la api para sacar el json de datos
def consultaAEMET(requestString):
    try:
        res = requests.get(requestString)
        data = json.loads(res.text)
        #con el json de la primera consulta tengo la url de los datos, que es otro json
        if ('datos' in data):
            res = requests.get(data['datos'])
            try:
                data = json.loads(res.text)
            except:
                 data = {}            
    except:
       data = {} 

    return data      

#apikey de la aemet
apikey = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhaXJlYW5hbHl0aWNzQG91dGxvb2suZXMiLCJqdGkiOiI0OWM0NTBjMy1lM2U3LTQ3OGMtODhkOS1mNjg4N2QyNWIzZmQiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTUzMDcxNzk5NSwidXNlcklkIjoiNDljNDUwYzMtZTNlNy00NzhjLTg4ZDktZjY4ODdkMjViM2ZkIiwicm9sZSI6IiJ9.lOFwRMaV2YOefcEt6aVxGoXH-3HO-y3AuYt6NZw7Q7w'

#formato de las fechas y fecha inicial
dateFormat = '%Y-%m-%d'
dateIni = datetime.strptime('2010-01-01',dateFormat)
#ponemos fin en el 1 de junio de 2018
dateStop = datetime.strptime('2018-06-01',dateFormat)
#dateStop = datetime.strptime('2010-10-01',dateFormat)


#códigos de las estaciones metereológicas
estaciones = ['3100B','3110C','3191E','3200','3129','3194U','3196','3195','3266A','2462','3338','3111D','3175']
#estaciones = ['3100B','3110C','3191E']


#url de consulta
urlBase = 'https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/'

for estacion in estaciones:
    #fecha inicial para cada estacion
    dateIniEst = dateIni
    while (dateIniEst<dateStop):
        #año de la fecha inicial
        anyo1 = dateIniEst.year
        #sumo 30 dias
        dateEndEst = dateIniEst+timedelta(days=30)
        #año de la fecha final
        anyo2 = dateEndEst.year 
        #si hay cambio de año espero un minuto para no saturar la api
        if (anyo1 != anyo2):
            time.sleep(60)
        # Aplica el formato
        fechaIni = dateIniEst.strftime(dateFormat)   
        fechaFin = dateEndEst.strftime(dateFormat)
        #paso la fecha final como incial para la siguiente iteración
        dateIniEst = dateEndEst
        #consulto la api y recupero el json
        url=urlBase+'fechaini/'+fechaIni+'T00:00:00UTC/fechafin/'+fechaFin+'T23:59:59UTC/estacion/'+estacion+'/?api_key='
        requestString=url+apikey
        #lanza la consulta y guarda en el fichero con el nombre de la estación
        print('consulta de estación = ' + estacion + ' con fecha inicio = ' + fechaIni)
        data = consultaAEMET(requestString)
        fichero = estacion + 'data.json'
        with open(fichero, mode='a') as f:
            f.write(json.dumps(data, indent=2))



