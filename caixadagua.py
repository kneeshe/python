# dimensões do reservatorio - altura, largura, comprimento
# consumo medio = litros/dia
# informar capacidade total do reservatorio, autonimia do reserv em dias
# <2, consumo elevado; >2 e <7, consumo moderado; >7, consumo reduzido

altRes = float(input("qual a altura em cm? "));
largRes = float(input("qual a largura em cm? "));
compRes = float(input("qual o comprimento em cm? "));

tamanhoCubico = (largRes * compRes) * altRes; # calcula o tamanho cubido do reservatorio

consMed = float(input("quantos litros voce gasta por dia? ")); # pede ao usuario o consumo medio de agua - litro/dia

capTotal = tamanhoCubico * 0.001; #converte os cm3 em litros.

autonomia = capTotal/consMed; # calcula a autonomia dividindo os litros pelo gasto medio do dia

if autonomia < 2:
    print("consumo elevado");

elif autonomia > 2 and autonomia <= 7:
    print("consumo moderado");

elif autonomia > 7:
    print("consumo reduzido");

else:
    print("entrada invalida");