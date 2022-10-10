from random import choice
num = 1, 2, 3, 4, 5
lista = num
jogo = choice(lista)
print("Vou pensar em um número de 0 a 5. Tente adivinhar!")
print("-=-" * 10)
n = int(input("Em que número eu pensei? "))

if jogo == n:
    print("Parabéns, você escolheu o número em que eu estava pensando!!")
else:
    print("Tente novamente. Eu pensei no número {} e não no {}".format(jogo, n))