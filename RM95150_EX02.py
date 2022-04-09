# Votação para escolha do melhor dia da semana para realização das lives.

lista_dias = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]
lista_votos = []
valor_temp = 0
posicao = 0
valor_maximo = 0

for x in range(0, 5):
    valor = int(input("Digite a quantidade de votos da " + lista_dias[x] + ": "))
    lista_votos.append(valor)

    if valor > valor_temp:
        valor_maximo = valor
        posicao = x

    valor_temp = valor_maximo

print("\nO dia escolhido foi {} com {} votos".format(lista_dias[posicao], lista_votos[posicao]))
