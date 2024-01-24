for num in range(101):
    div = 0
    for x in range(1, num+1):
        resto = num % x
        if resto == 0:
            div += 1

    if div == 2:
        print(num)


#----------------------------------------------
# n1 = int(input('Digite um número: '))

# div = 0
# for x in range(1, n1+1):
#     resto = n1 % x
#     if resto == 0:
#         div += 1

# if div == 2:
#     print('O número {} é primo'.format(n1))
# else:
#     print('O número {} não é primo'.format(n1))