"""
Dieta do Garfield - OBI 2025 Nível 2
Calcula quantas calorias Garfield ainda pode consumir sem ultrapassar o limite diário.
"""
# Entrada: N (número de refeições) e M (limite de calorias)
N, M = map(int, input().split())

total = 0
# Para cada refeição, lê as quantidades de proteína, gordura e carboidrato
for _ in range(N):
    P, G, C = map(int, input().split())
    # Calcula as calorias da refeição
    total += P*4 + G*9 + C*4
# Imprime o quanto ainda pode consumir sem ultrapassar o limite
print(max(0, M - total)) 