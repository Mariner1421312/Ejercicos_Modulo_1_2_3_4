lista = []

with open("personas.txt") as f:
	texto = f.readlines()
	for i in range(len(texto)):
		persona = {}

		linea = texto[i].split(";")
		persona.update({"nombres" : linea[1] + " " + linea[2]})
		persona.update({"fecha nacimiento" : linea[3]})
		lista.append(persona)

for i in range(len(lista)):
	print("Nombres: ", lista[i]["nombres"], "\tFecha de nacimiento: ", lista[i]["fecha nacimiento"])

