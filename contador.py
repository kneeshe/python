# faça 5 perguntas
# =2, suspeita; =3 e =4, cumplice, =5, assassino
# <2, inocente

cont = 0; # faz a contagem de sim's

pg1 = input("telefonou para a vitima? "); # pergunta ao user
if pg1 == 's' or pg1 == 'sim':  # se a resposta for sim, conta +1 ao contador
    cont += 1;

pg2 = input("esteve no local do crime? ");
if pg2 == 's' or pg1 == 'sim':
    cont += 1;

pg3 = input("mora perto da vitima? ");
if pg3 == 's' or pg3 == 'sim':
    cont += 1;

pg4 = input("devia para a vitima? ");
if pg4 == 's' or pg4 == 'sim':
    cont += 1;

pg5 = input("ja trabalhou com a vitima? ");
if pg5 == 's' or pg5 == 'sim':
    cont += 1;

if cont == 2: # faz a comparação entre o contador e o resultado
    print("voce é suspeito");

elif cont == 3 or cont == 4:
    print("voce é cumplice");

elif cont == 5:
    print("voce é o assassino");

else:
    print("voce é inocente");