import os, csv

def timegenerator(dp):
	tiempo = float(input("Tiempo del caballo en segundos: "))
	dhc = int(input("Distancia en la que hizo el tiempo: ")) #Distancia historia caballo
	dcp = dp #Distancia caballo pista, distancia pista

	if dcp < dhc:
		dcp = dhc - dcp
		while dcp != 0:
			dcp = dcp - 100
			tiempo -= 7

	elif dcp > dhc:
		dcp = dcp - dhc
		while dcp != 0:
			dcp = dcp - 100
			tiempo += 7

	else:
		pass

	meses = int(input("Meses que el caballo lleva sin correr: "))
	if meses >= 10:
		tiempo += 0.8

	elif meses >= 6:
		tiempo += 0.2
	
	else:
		pass

	round(tiempo, 1)
	return tiempo

while True:
	print("********DATA ADDER********")
	print("\nAgregue los datos de cada caballo por carrera para ingresarlos en la base de datos.")
	fecha = input("Indique la fecha de la carrera (dd-mm-aa): ")
	numeroCarrera = input("Indique el numero de la carrera: ")
	print("\n(No ganadores: 1, Ganadores de 1 o 2: 2, Ganadores de 2 o 3: 3,Ganadores de 3 o 4: 4, Ganadores de 4 o 5: 5,Ganadores de 5+: 6, Clasico: 7)")
	grupocarrera = int(input("Escoja el lote especificado para la carrera: "))	
	distp = int(input("\nDistancia de la pista: "))

	numberofhorses = int(input("Numero de caballos: "))

	fechadata, numeroCdata, distanciadata, claseCdata = [], [], [], []
	
	for i in range(numberofhorses):
		fechadata.append(fecha)
		numeroCdata.append(numeroCarrera)
		distanciadata.append(distp)
		claseCdata.append(grupocarrera)

	listacaballos = []
	nombrecaballos = []
	divUlt = []
	divPenult = []
	ultposicion = []
	cuerposultlista = []
	cuerpospenultlista = []
	puntoslote = []
	puntosposicion = []
	actjinete = []
	ganadasjinete = []
	jineterepmonta = []
	acttrainer = []
	ganadostrainer = []
	resultadodummy = []

	for number_horses in range(numberofhorses):
		print("\nPara caballo %s:" % (number_horses + 1))
		name_horse = input("Indique el nombre del caballo: ")
		nombrecaballos.append(name_horse)
		listacaballos.append(timegenerator(distp))

		ultipos = int(input("\nUltima posicion de llegada: "))
		ultposicion.append(ultipos)

		cuerposult = float(input("A cuantos cuerpos llego del ganador en su ultima actuacion: "))
		cuerposultlista.append(cuerposult)
		cuerpospenult = float(input("A cuantos cuerpos llego del ganador en su penultima actuacion: "))
		cuerpospenultlista.append(cuerpospenult)

		subidobajado = input("\nEl caballo esta subido o bajado de lote? s/b: ")
		if subidobajado.lower() == 's':
			subida = input('Grados de subida? g1/g2/g3: ')
			if subida == 'g1':
				puntoslote.append(1)
			elif subida == 'g2':
				puntoslote.append(2)
			elif subida == 'g3':
				puntoslote.append(3)

		elif subidobajado.lower() == 'b':
			puntoslote.append(4)
		
		div1 = int(input("\nDividendo ultimo: "))	
		divUlt.append(div1)	
		div2 = int(input("Dividendo penultimo: "))
		divPenult.append(div2)

		print("\n")

		if distp <= 1200:
			caballo = input("Ha corrido el caballo en distancia menor o igual a 1200? ")
			if caballo.lower() == "si":
				posicion = input("Ha ocupado las tres primeras posiciones? ")
				if posicion.lower() == "si":
					puntosposicion.append(3)
				else:
					puntosposicion.append(1)
			else:
				posicion = input("Ha ocupado las tres primeras posiciones en sus ultimas actuaciones? ")
				if posicion.lower() == "si":
					puntosposicion.append(1)
				else:
					puntosposicion.append(0)

		elif distp >= 1300:
			if distp <= 1500:
				caballo = input("Ha corrido el caballo en distancias en rango 1300-1500? ")
				if caballo.lower() == "si":
					posicion = input("Ha ocupado las tres primeras posiciones? ")
					if posicion.lower() == "si":
						puntosposicion.append(3)
					else:
						puntosposicion.append(1)
				else:
					posicion = input("Ha ocupado las tres primeras posiciones en sus ultimas actuaciones? ")
					if posicion.lower() == "si":
						puntosposicion.append(2)
					else:
						puntosposicion.append(0)
				

			elif distp >= 1600:
				caballo = input("Ha corrido el caballo en distancias mayores " + str(distp) + "? ")
				if caballo.lower() == "si":
					posicion = input("Ha ocupado las tres primeras posiciones? ")
					if posicion.lower() == "si":
						puntosposicion.append(3)
					else:
						puntosposicion.append(1)
			
				else:
					posicion = input("Ha ocupado las tres primeras posiciones en sus ultimas actuaciones? ")
					if posicion.lower() == "si":
						puntosposicion.append(2)
					else:
						puntosposicion.append(0)


		numactj = int(input("\nNumero de actuaciones del jinete: "))
		actjinete.append(numactj)
		ganado = int(input("Numero de veces que ha ganado el jinete: "))
		ganadasjinete.append(ganado)
		repitemonta = input("El caballo repite monta? ")
		if repitemonta == 'si':
			jineterepmonta.append(3)
		else:
			jineterepmonta.append(1)

		EntC = int(input("\nNumero de carreras del trainer: "))
		acttrainer.append(EntC)
		EntG = int(input("Numero de carreras Ganadas: "))
		ganadostrainer.append(EntG)

	for i in range(numberofhorses):
		resultadodummy.append(i + 1)
	
	zipped_data_list_runs = zip(fechadata, numeroCdata, distanciadata, claseCdata, nombrecaballos, listacaballos, divUlt, divPenult, ultposicion, cuerposultlista, cuerpospenultlista, puntosposicion, puntoslote, actjinete, ganadasjinete, jineterepmonta, acttrainer, ganadostrainer,resultadodummy)

	file_name_runs = "datacarrerasagregar.csv"
	directory_data = "./AddData/"

	file_path_runs = os.path.join(directory_data, file_name_runs)

	if not os.path.exists(directory_data):
		directory = os.makedirs("AddData", exist_ok=True)

	with open(file_path_runs, 'a', newline='') as file_object:
		writer = csv.writer(file_object)
		for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s in zipped_data_list_runs:
			writer.writerow([a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s])

		file_object.close()

	print("*********Data guardada********")
	break