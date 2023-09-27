def min_movimientos(a, b, c):
    diferencia = abs(a - b)
    movimientos = (diferencia + c - 1) // c
    return movimientos


t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    resultado = min_movimientos(a, b, c)
    print(resultado)