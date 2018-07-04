from datetime import datetime, date, time, timedelta

dateFormat = "%Y-%m-%d"
dateIni = datetime.strptime("2018-07-01",dateFormat)

for i in range(1,10):
	# Aplica el formato
	cadena1 = dateIni.strftime(dateFormat)   
	# Muestra fecha1
	print("Fecha:", cadena1)
	#resto 30 dias
	dateIni = dateIni-timedelta(days=30)

