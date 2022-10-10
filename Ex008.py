distancia = float(input("Qual é a distância da sua viagem em Km? "))
print("Você está prestes a começar uma viagem de {}Km.".format(distancia))
if distancia <= 200:
    print("O preço  de sua passagem será de R${:.2f}".format(distancia * 0.50))
else:
    print("O preço de sua passagem será de R${:.2f}".format(distancia * 0.45))

