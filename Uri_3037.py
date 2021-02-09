cases = int(input())

for n in range(cases):

     linha1 = input().split(" ")
     
     x = 1
     joao = 0
     maria = 0

     x, d = linha1
     x = int(x)
     d = int(d)

     joao = (x*d) + joao

     linha2 = input().split(" ")

     x, d = linha2
     
     x = int(x)
     d = int(d)
     joao = (x*d) + joao

     linha3 = input().split(" ")

     x, d = linha3
     
     x = int(x)
     d = int(d)
     joao = (x*d) + joao

     linha4 = input().split(" ")

     x, d = linha4
     
     x = int(x)
     d = int(d)
     maria = (x*d) + maria

     linha5 = input().split(" ")

     x, d = linha5
     
     x = int(x)
     d = int(d)
     maria = (x*d) + maria

     linha6 = input().split(" ")

     x, d = linha6
     
     x = int(x)
     d = int(d)
     maria = (x*d) + maria

     if maria > joao:
        print("MARIA")

     elif joao > maria:
        print("JOAO")
