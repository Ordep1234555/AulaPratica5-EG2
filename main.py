def calcular_media(numeros):
    if len(numeros) == 0:
        return 0
    soma = sum(numeros)
    media = soma / len(numeros)
    return media

# Exemplo de uso
lista_numeros = [1, 2, 3, 4, 5]
media = calcular_media(lista_numeros)
print("A média é:", media)
