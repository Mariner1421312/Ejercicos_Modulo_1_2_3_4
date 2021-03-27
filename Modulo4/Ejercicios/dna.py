def funcion(csv, txt):
	adn = {"AGATC" : 0, "AATG" : 0, "TATC" : 0}
	agat = 0
	aatg = 0
	tatc = 0
	f = open(csv) 
	personas = []

	while True:
		line = f.readline()
		
		if line == "":
			break
		line = line.split(",")
		line[3] = line[3].replace("\n", "")

		personas.append(line)
	f2 = open(txt)

	sequence = f2.readlines()

	agat += sequence[0].count("AGAT")
	aatg += sequence[0].count("AATG")
	tatc += sequence[0].count("TATC")
	print(personas)
	
	adn.update({"AGAT" : agat})
	adn.update({"AATG" : aatg})
	adn.update({"TATC" : tatc})

	mensaje = "no match"
	p = {"nombre" : "", "coincidencias" : 0}
	
	for i in range(len(personas)):
		coincidencias = 0
		
		if i > 0:
			if int(personas[i][1]) == adn["AGAT"]:
				coincidencias += 1
			if int(personas[i][2]) == adn["AATG"]:
				coincidencias += 1
			if int(personas[i][3]) == adn["TATC"]:
				coincidencias += 1
		
			if p["coincidencias"] < coincidencias:
				p.update({"nombre" : personas[i][0]})
				p.update({"coincidencias" : coincidencias})	
				mensaje = personas[i][0]
	
	print(mensaje)
	

csv = "./data/dna/databases/small.csv"
txt = "./data/dna/sequences/4.txt"


funcion(csv, txt)