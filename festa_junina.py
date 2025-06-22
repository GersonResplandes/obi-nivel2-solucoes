"""
Festa Junina - OBI 2025 Nível 2
Calcula a menor distância total que Luísa precisa percorrer para visitar o supermercado e a lojinha, em qualquer ordem, e retornar à escola.
"""
# Entrada: três inteiros representando as posições da escola, supermercado e lojinha
E = int(input())  # Posição da escola
S = int(input())  # Posição do supermercado
L = int(input())  # Posição da lojinha

# Calcula todas as distâncias possíveis entre os pontos
lista = []
lista.append(E - S)
lista.append(E - L)
lista.append(S - E)
lista.append(S - L)
lista.append(L - S)
lista.append(L - E)

r = 0
# Soma apenas as distâncias positivas (caminhos reais)
for i in range(len(lista)):
    if lista[i] >= 0:
        r = lista[i] + r

print(r)  # Saída: menor distância total 