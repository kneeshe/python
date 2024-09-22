# em python, a função se chama def. voce não precisa estipular o tipo

def soma(x, y): # chamei a função de soma. dentro dos parenteses estão os parametros.
    resultado = x + y # variavel que soma os parametros
    return resultado # a função retorno retorna o valor de resultado para onde a função soma for invocada

# funções não conseguem transmitir os valores dela, por isso é preciso que existam parametros, 
# para que elas saibam quais valores usar nas funções principais onde forem chamadas.

# vamos calcular algumas coisas:

#variavel basica. em python, as variaveis surgem como char
# por isso é preciso converter elas. converti para int
num1 = int(input("digite um numero: ")) 
num2 = int(input("digite o segundo numero: "))

#vamos chamar a função e informar a ela que os parametros dela serão equivalentes as variaveis anteriores
print(f"{soma(num1, num2)}") # print imprime o resultado na tela

