"""
Cafeteria - OBI 2025 Nível 2
Verifica se é possível preparar uma bebida com a quantidade de leite desejada, dado o volume da xícara e doses de café.
"""
# Entrada: A (mínimo de leite), B (máximo de leite), C (capacidade da xícara), D (volume de cada dose de café)
A = int(input())  # Volume mínimo de leite
B = int(input())  # Volume máximo de leite
C = int(input())  # Capacidade da xícara
D = int(input())  # Volume de cada dose de café

possivel = False
# Testa todas as quantidades possíveis de doses de café
for doses in range(0, C // D + 1):
    cafe = doses * D
    leite = C - cafe
    if A <= leite <= B:
        possivel = True
        break

# Saída: 'S' se possível, 'N' caso contrário
print('S' if possivel else 'N') 