a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
if a > b:
    print("O valor {} é MAIOR.".format(a))
elif b > a:
    print("O valor {} é MAIOR".format(b))
elif a == b:
    print("Os valores são IGUAIS.")