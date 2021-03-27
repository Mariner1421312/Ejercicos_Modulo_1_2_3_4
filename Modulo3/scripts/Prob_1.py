def suma_digitos(numero):
    return sum([int(c) for c in str(numero)])

tarjeta = input("Ingrese el número de tarjeta: ")
tarjeta_numero = int(tarjeta)
tarjeta = list(tarjeta)
suma = 0

for i in range(len(tarjeta)):
    tarjeta[i] = int(tarjeta[i])

if len(tarjeta) % 2 == 0:
    for i in range(1,int((len(tarjeta)+2)/2)):
        if tarjeta[-2*i]*2 >= 10:
            suma = suma + suma_digitos(tarjeta[-2*i]*2)
        else:
            suma = suma + 2*tarjeta[-2*i]

    for i in range(int(len(tarjeta)/2)):
        suma = suma + tarjeta[(2*i)+1]
else:
    for i in range(1,int((len(tarjeta)+1)/2)):
        if tarjeta[-2*i]*2 >= 10:
            suma = suma + suma_digitos(tarjeta[-2*i]*2)
        else:
            suma = suma + 2*tarjeta[-2*i]

    for i in range(1,int((len(tarjeta)+3)/2)):
        suma = suma + tarjeta[-(2*i-1)]

if suma % 10 == 0:
    print("¡SU TARJETA SI ES VÁLIDA!")
    if tarjeta_numero == 378282246310005 or tarjeta_numero == 371449635398431:
        print("Su tarjeta es AMEX")
    elif tarjeta_numero == 5555555555554444 or tarjeta_numero == 5105105105105100:
        print("Su tarjeta es MASTERCARD")
    elif tarjeta_numero == 4111111111111111 or tarjeta_numero == 4012888888881881:
        print("Su tarjeta es VISA")
else:
    print("¡INVALIDO!")