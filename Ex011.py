salario = float(input("Qual é o seu salário? R$"))
s1 = salario + (salario * 0.01)
s2 = salario + (salario * 0.15)
if salario > 1250:
    print("O salário de R${} passará a ser de R${:.2f}".format(salario, s1))
else:
    print("O salário de R${} passará a ser de R${:.2f}".format(salario, s2))
