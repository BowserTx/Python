cases = int(input())

for n in range(cases):

    linha = input().split(" ")

    h, d, g = linha

    h = int(h)
    d = int(d)
    g = int(g)

    if (h >= 200) and (h <= 300) and (d >= 50) and (g >= 150):
        print("Sim")

    else:
        print("Nao")
