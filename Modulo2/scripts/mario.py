while True:
    try:
        altura = int(input("Ingresar la altura, este debe ser un valor entre 1 y 8: "))
        break
    except ValueError:
        print("Ingrese un valor válido porfavor")
        
if 0 < altura < 9:
    for i in range(altura):
        print(" "*(altura - i - 1) + "#" * (i + 1))
else:
    print("Ingresar nuevamente el valor porfavor")