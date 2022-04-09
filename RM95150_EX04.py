#Algoritmo para obtenção da segunda parte da senha.
# LIBERDADE + Fatorial dos minutos digitados pelo usuário

minutos = int(input("Digite o valor dos minutos do horário atual de seu computador: "))
fatorial = 1

if minutos != 0:

    for valor in range(1, minutos + 1):
        fatorial *= valor

    print("A senha obtida é LIBERDADE{}".format(fatorial))
