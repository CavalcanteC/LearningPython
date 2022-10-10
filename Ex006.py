velocidade = int(input("Qual a velocidade atual do carro? "))
limite = 80
multa = (velocidade - limite) * 7
if velocidade > limite:
    print("Você foi multado! O limite de 80km/h foi excedido e o valor da multa é de R${:.2f}".format(multa))
else:
    print("Tenha um bom dia! Dirija em segurança.")