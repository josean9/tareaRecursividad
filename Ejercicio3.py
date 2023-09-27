numero = "554"
lista=[]
def cadena(lista):
    long = int(lista[2])
    global cadena
    cadena=input("Ingrese una cadena de longitud"+" "+str(long)+":")
def inicio():
    for i in range(len(str(numero))):
        lista.append(numero[i])
    print(cadena(lista)) 
    contadorMases = 0
    ContadorMenos = 0
    for caracter in cadena:
        if caracter == '+':
            contadorMases += 1 
        elif caracter == '-':
            ContadorMenos += 1
    if lista[0]<=lista[1]or lista[0]<lista[1]+contadorMases-ContadorMenos:
        print("Yes")
    elif lista[0]==lista[1]+contadorMases-ContadorMenos:
        print("Maybe")
        
    else:
        print("No")
print(inicio())
