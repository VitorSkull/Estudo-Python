
a = int(input('Primeiro bimestre: '))
if a > 10:
    a = int(input('Você digitou errado, insira o valor novamente: '))
b = int(input('Segundo bimestre: '))
if b > 10:
    b = int(input('Você digitou errado, insira o valor novamente: '))
c = int(input('Terceiro bimestre: '))
if c > 10:
    c = int(input('Você digitou errado, insira o valor novamente: '))
d = int(input('Quarto bimestre: '))
if d > 10:
    d = int(input('Você digitou errado, insira o valor novamente: '))
media = (a + b + c + d) / 4
if media <= 10:
    print('Média do aluno: {}'.format(media))
else:
    print('Os valores não foram inseridos corretamente, tente novamente.')

# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('A média do aluno foi: {}'.format(media))
# else:
#     print('Foi informado um valor incorreto.')


#-------------------------------------------
# n1 = int(input('Primeiro valor: '))
# n2 = int(input('Segundo valor: '))

# resto_1 = n1 % 2
# resto_2 = n2 % 2
# if resto_1 == 0 or resto_2 == 0:
#     print('Foi digitado um número par')
# else:
#     print('Foi digitado um número impar')


#--------------------------------------------

# a = int(input('Primeiro número: '))
# b = int(input('Segundo número: '))
# c = int(input('Terceiro número: '))

# if a > b and a > c:
#     print('O maior numero é: {}'.format(a))
# elif b > a and b > c:
#     print('O maior numero é: {}'.format(b))
# else:
#     print('O maior numero é: {}'.format(c))
# print('cabo')