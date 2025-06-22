"""
Gráfico de Barras - OBI 2025 Nível 2
Gera um gráfico de barras em texto a partir da popularidade de brinquedos.
"""
# Entrada: N (número de brinquedos) e lista X (popularidade de cada brinquedo)
N = int(input())
X = list(map(int, input().split()))
H = max(X)  # Altura máxima do gráfico

# Para cada linha do topo até a base
for i in range(H):
    linha = []
    for x in X:
        # Imprime '1' se a barra atinge aquela altura, '0' caso contrário
        if x >= H - i:
            linha.append('1')
        else:
            linha.append('0')
    print(' '.join(linha)) 