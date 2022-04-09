#Esse programa recebe a distância e o tempo e calcula a velocidade média
#Primeiro vamos pedir a distância e o tempo
print("Esse é o calculador de velocidade média")
distancia = input("Digite a distância percorrida: ")
tempo = input("Digite o tempo percorrido: ")
#Realizando o cálculo e exibindo a mensagem
valocidade_media = float(distancia) / float(tempo)
print("A velocidade média calculado foi de {:.2f} km/h".format(valocidade_media))