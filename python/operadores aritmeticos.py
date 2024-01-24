n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
soma = n1+n2
subtracao = n1-n2
multiplicacao = n1*n2
divisao = n1/n2
resto = n1 % n2
resultado = ('Soma: {soma} \nsubtração: {subtracao}.'          #usar o .format() sempre que quiser mostrar um resultado vindo do {}.
'\nMultiplicação: {multiplicacao}'                             #usar o \n para ir pro próximo parágrafo(linha)
'\nDivisão: {divisao}'
'\nResto: {resto}'.format(soma=soma,
                          subtracao=subtracao,
                          multiplicacao=multiplicacao,
                          divisao=divisao,
                          resto=resto))
print(resultado)
                          


# print('soma: {}'.format(soma))
# print(subtracao)
# print(multiplicacao)
# print(divisao)
# print(resto)
    # x = '1'
    # soma2= int(x) + 1
    # print(soma2)