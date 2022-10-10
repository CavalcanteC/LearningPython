a1 = str(input("Qual é o primeiro aluno? "))
a2 = str(input("Qual é o segundo aluno? "))
a3 = str(input("Qual é o terceiro aluno? "))
a4 = str(input("Qual é o quarto aluno? "))
lista = [a1, a2, a3, a4]
ordem = sorted(lista)
print("A ordem de apresentação será {}".format(ordem))