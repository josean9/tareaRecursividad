numeros = [-3, 2, -5]
n = 0

for i in numeros:
    numeros[n] = abs(numeros[n])
    n += 1
print(min(numeros))