try:
	#precio actual del hormigon y sus materiales
	precio_hormigon = 50
	precio_cemento = 10
	precio_arena = 0.350
	precio_grava = 0.450
	precio_agua = 0.6
	# pedimos al usuario el nombre del cliente
	solicitante = input("ingrese el nombre del cliente: ")
	#creamos los nombres para los archivos (si son iguales se sobreescriben)
	archivo_cliente = f"{solicitante}.txt"
	archivo_empresa = f"{solicitante}_empresa.txt"
	# le pedimos al usuario que elija el tipo de medida.
	tipo_medida = 0
	print("unidad de medida a utilizar:")
	while tipo_medida < 1 or tipo_medida > 3:
		tipo_medida = int(input("[1] - Metros.\n[2] - Pies.\n[3] - centimetros.\n"))
		if tipo_medida < 1 or tipo_medida > 3:
			print("por favor, ingrese una de las opciones ofrecidas.")
	# le pedimos al usuario la longitud, anchura y altura.
	longitud = float(input("ingrese la longitud del area: "))
	if tipo_medida == 1 and longitud == round(longitud):
		longitud = round(longitud)
	anchura = float(input("ingrese la anchura del area: "))
	if tipo_medida == 1 and anchura == round(anchura):
		anchura = round(anchura)
	altura = float(input("ingrese la altura del area: "))
	if tipo_medida == 1 and altura == round(altura):
		altura = round(altura)
	# convertimos a metros.
	if tipo_medida == 2:
		longitud = round((longitud * 0.3048), 2)
		if longitud == (round(longitud)):
			longitud = round(longitud)
		anchura = round((anchura * 0.3048), 2)
		if anchura == (round(anchura)):
			anchura = round(anchura)
		altura = round((altura * 0.3048), 2)
		if altura == (round(altura)):
			altura = round(altura)
	elif tipo_medida ==3:
		longitud = round((longitud * 0.01), 2)
		if longitud == (round(longitud)):
			longitud = round(longitud)
		anchura = round((anchura * 0.01), 2)
		if anchura == (round(anchura)):
			anchura = round(anchura)
		altura = round((altura * 0.01), 2)
		if altura == (round(altura)):
			altura = round(altura)
	tipo_hormigon = 0
	# le pedimos al usuario que ingrese el tipo de hormigon a utilzar.
	print("ingrese el tipo de hormigon para este trabajo:")
	while tipo_hormigon < 1 or tipo_hormigon > 5:
		tipo_hormigon = int(input("[1] - 1:2:2\n[2] - 1:2:3\n[3] - 1:2:4\n[4] - 1:3:4\n[5] - 1:3:6\n"))
		if tipo_hormigon < 1 or tipo_hormigon > 5:
			print("por favor, ingrese una de las opciones ofrecidas.")
	# segun el tipo de hormigon seleccionedos, tomamos diferentes cantidades de materiales.
	if tipo_hormigon == 1:
		cemento_por_M = 420
		arena_por_M = 0.67
		grava_por_M = 0.67
		agua_por_M = 220
	elif tipo_hormigon == 2:
		cemento_por_M = 350
		arena_por_M = 0.56
		grava_por_M = 0.84
		agua_por_M = 180
	elif tipo_hormigon == 3:
		cemento_por_M = 300
		arena_por_M = 0.48
		grava_por_M = 0.96
		agua_por_M = 170
	elif tipo_hormigon == 4:
		cemento_por_M = 260
		arena_por_M = 0.63
		grava_por_M = 0.84
		agua_por_M = 170
	elif tipo_hormigon == 5:
		cemento_por_M = 210
		arena_por_M = 0.5
		grava_por_M = 1.0
		agua_por_M = 160
except ValueError:
	print("error")
else:
	# calculo del area en metros cubicos.
	area = round((longitud * anchura * altura), 2)
	if area == (round(area)):
			area = round(area)
	print(f"el area designada de {longitud}M de longitud, {anchura}M de largo, {altura}M de alto.\nrequiere una cantidad de {area} metros cubicos de hormigon.")
	# calculo de los materiales a utilizar segun el area total.
	cemento = cemento_por_M * area
	# el cemento se calcula por sacos de 50Kg. y se prevee un desperdicio aproximado del 5%.
	sacos_cemento = round((cemento / 50) * 1.05)
	arena = round((arena_por_M * area), 2)
	if arena == (round(arena)):
		arena = round(arena)
	grava = round((grava_por_M * area), 2)
	if grava == (round(grava)):
		grava = round(grava)
	agua = round((agua_por_M * area), 2)
	if agua == (round(agua)):
		agua = round(agua)
	print(f"para la preparacion del hormigon se nesesitaran:\n{round(sacos_cemento)} sacos de cemento.\nUn volumen de arena de: {arena} metros cubicos.\nUn volumen de grava de {grava} metros cubicos.\n{agua} litros de agua.")
	# abrir y completar con la informacion el archivo para la empresa.
	empresa = open(archivo_empresa, "w")
	empresa.write(f"Pedido para {solicitante}\n")
	empresa.write(f"El cliente {solicitante} ah realizado un pedido de {area} metros cubicos de hormigon tipo {tipo_hormigon}.\n")
	empresa.write(f"Para este pedido se nesesitaran las siguientes materias primas: \n")
	empresa.write(f" {sacos_cemento} sacos de cemento.\n {arena} metros cubicos de arena.\n {grava} metros cubicos de grava.\n {agua} litros de agua.\n")
	empresa.write(f"el costo de los materiales sera un aproximado de: U$D{round((sacos_cemento * precio_cemento)+(arena * precio_arena)+(grava * precio_grava)+(agua * precio_agua))}.")
	empresa.close()
	# abrir y completar con la informacion el archivo para el cliente.
	cliente = open(archivo_cliente, "w")
	cliente.write(f"{solicitante} a solicitado hormigon con las siguientes medidas:\n")
	cliente.write(f" {longitud} metros de profundidad.\n {anchura} metros de ancho.\n {altura} metros de alto.")
	cliente.write(f"de acuerdo con el calculo realizado a continuacion se le entregaran {area} metros cubicos de hormigon.\n (metros de profundidad)X(metros de ancho)X(metros de alto)=(metros cubicos de hormigon)\n {longitud} X {anchura} X {altura} = {area}.\n")
	cliente.write(f"la totalidad tendra un costo aproximado de U$D{area * precio_hormigon}.")
	cliente.close()
finally:
	print("findel programa")