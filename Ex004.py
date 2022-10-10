n1 = float(input("Qual foi a sua primeira nota? "))
n2 = float(input("Qual foi a sua segunda nota? "))
media = (n1 + n2) /2
if media >= 7:
    print("A sua média foi de {}.\nParabéns, você passou!!".format(media))
else:
    print("A sua média foi de {}.\nSinto muito, você está de recuperação.".format(media))