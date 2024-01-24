print("hello world\n\n")
print("DIGITAR UM VALOR NEGATIVO ENCERRA O LAÇO")
qnt = 0
soma = 0
media = 0
valor = float(input("Digite um valor: "))

while valor > 0.0:
    soma = soma + valor
    qnt = qnt + 1
    valor = float(input("Digite um valor: "))

#LAÇO ENCERRADO
media = soma / qnt

print("Quantidade de valores: ", qnt)
print("Soma total dos valores: ", soma)
print("Media dos valores: ", media)