texto = input("Ingrese la frase: ").upper()


n = int(input("Ingrese el nivel de cifrado: "))

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


cifrado = ""


for i in texto:
    if i in abc:
        pos_letra = abc.index(i)
        nueva_pos = (pos_letra + n) % len(abc)
        cifrado+= abc[nueva_pos]
    else:
        cifrado= cifrado + i

print("Mensaje cifrado: {}".format(cifrado))