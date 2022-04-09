#ALGORITMO PARA CÁLCULO DO BÔNUS CONFORME A ASSINATURA DO CLIENTE

valor_bonus = 0
nivel_assinatura = input("Digite o tipo de assinatura do cliente: ")
faturamento_anual = float(input("Digite o faturamento anual do cliente: "))

if nivel_assinatura.upper() == "BASIC":
    valor_bonus = faturamento_anual * 0.3
elif nivel_assinatura.upper() == "SILVER":
    valor_bonus = faturamento_anual * 0.2
elif nivel_assinatura.upper() == "GOLD":
    valor_bonus = faturamento_anual * 0.1
elif nivel_assinatura.upper() == "PLATINUM":
    valor_bonus = faturamento_anual * 0.05

print("O cliente deve pagar um bônus no valor de {}".format(valor_bonus))
