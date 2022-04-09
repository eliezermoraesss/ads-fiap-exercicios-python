#SISTEMA PARA CALCULAR E EXIBIR A MÉDIA DAS NOTAS DOS ALUNOS POR MATRÍCULAS PARES E ÍMPARES

notas_impares = []
notas_pares = []
for x in range(1, 51, 2):
    nota = float(input("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES\nPOR FAVOR INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(x)))
    notas_impares.append(nota)
    print()

for x in range(0, 51, 2):
    nota = float(input("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES\nPOR FAVOR INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(x)))
    notas_pares.append(nota)
    print()

media_impar = sum(notas_impares) / len(notas_impares)
print("A média da metade da sala ímpar é {}", format(media_impar))

media_par = sum(notas_pares) / len(notas_pares)
print("A média da metade da sala par é {}", format(media_par))

if media_impar > media_par:
    print("\nA metade ímpar obteve a maior média")
elif media_par > media_impar:
    print("\nA metade ímpar obteve a maior média")
else:
    print("\nAs metades ímpar e par obtiveram médias iguais")
