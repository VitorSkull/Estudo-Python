print("hello world")

nome = input("Nome do Funcionario: ")
codigo = int(input("Codigo do funcionario: "))
salario = float(input("Salario do funcionario: "))
situacao = True

tipo = type(salario)

#print("Codigo:", codigo , "salario:", salario, "nome:", nome)
#print("Codigo:" + str(codigo) + "\nsalario:" + str(salario) + "\nnome:" + nome)
print("Nome: %s" % nome)
print("Salario: %.3f" % salario)
print("codigo: %d" % codigo)
print("situacao: %r" % situacao)

'''registro = (input("Digite o nome de alguma coisa ou um numero: "))
tipo = type(registro)

print(registro)
print(tipo)'''