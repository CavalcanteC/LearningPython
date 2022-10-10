valor = float(input("Qual é o valor da casa? R$"))
salario = float(input("Qual é o seu salário? R$"))
anos = int(input("Em quantos anos você quer fazer o financiamento? "))
meses = anos * 12
prestacao = (valor / meses)
if prestacao < salario * 0.3:
    print("Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}\nEmpréstimo pode ser CONCEDIDO".format(valor, anos, prestacao))
else:
    print("Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}\nEmpréstimo NEGADO!".format(valor, anos, prestacao))