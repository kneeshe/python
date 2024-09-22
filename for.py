#codigo com for em python

for i in range(0, 10, 1): # em python, o escopo é o range. o primeiro numero é o inicio da contagem;
    print(f"{i}")         # o segundo numero é ate onde vai ser contado e o terceiro, a passada da contagem

# for tambem  funciona com vetores

vetor = [1, 2, 3, 4, 5]
for i in vetor: # neste caso, o for percorreu o espaço definido dentro do vetor
    print(f"{i}")

vetorTexto = ['agatha', 'bruno', 'cristian', 'diogo', 'eduardo'] # vetor de strings
for i in vetorTexto:
    print(f"{i}")
