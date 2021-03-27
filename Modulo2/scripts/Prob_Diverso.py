def listado(n):
    aux = 0
    aux2 = 0
    alumnos = []
    contador = 0
    notaacum = 0
    verificador = True
    for i in range(n):
        print("Ingrese los datos del alumno {}".format(i+1))
        repetidor = True
        while repetidor:
            alumno = {
                'nombre': input('Nombre Completo: '),
                'nota1': float(input('Nota 1: ')),
                'nota2': float(input('Nota 2: ')),
                'nota3': float(input('Nota 3: '))
                }
            if 0 <= alumno['nota1'] <= 10 and 0 <= alumno['nota2'] <= 10 and 0 <= alumno['nota3'] <= 10:
                repetidor = False
            else:
                print("Uno de las notas escogidas no se encuentra entre 0 y 10, ingresar denuevo")
                repetidor = True
        notaprom = (alumno['nota1']+alumno['nota2']+alumno['nota3'])/3
        if notaprom >= aux:
            notamay = alumno['nombre']
            aux = notaprom
            while verificador:
                aux2 = aux
                verificador = False
        if notaprom <= aux2:
            aux2 = aux
            notamen = alumno['nombre']
        if notaprom >= 4:
            contador = contador + 1
        notaacum = notaacum + notaprom
        alumnos.append(alumno)
    return alumnos,contador,notaacum,notamay,notamen
n = int(input("Ingrese la cantidad de alumnos del curso: "))
alumnos,contador,notaacum,notamay,notamen = listado(n)
notapromsalon = notaacum/n
print("El listado de alumnos es el siguiente: {}".format(alumnos))
print("La cantidad de alumnos aprobados es {} y desaprobados es {}: ".format(contador,n-contador))
print("La nota promedio del salón es {}".format(notapromsalon))
print("El alumno con mayor nota promedio es {} y con menor nota promedio es {}".format(notamay,notamen))