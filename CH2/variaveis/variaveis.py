nome = input("Digite o nome do funcionário: ")
empresa = input("Digite o nome da instituição: ")
qtd_funcionarios = int(input("Digite a qtd de funcionários: "))
mediaMensalidade = float(input("Digite a média da mensalidade: "))
print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtd_funcionarios, " funcionarios.")
print("A média da mensalidade é de: " + str(mediaMensalidade))
print("- - - - - - - Verifique os tipos de dados abaixo: - - - - - - -")
print("O tipo de dado da variável [nome] é: ", type(nome))
print("O tipo de dado da variável [empresa] é: ", type(empresa))
print("O tipo de dado da variável [qtd_funcionarios] é: ", type(qtd_funcionarios))
print("O tipo de dado da variável [mediaMensalidade] é: ", type(mediaMensalidade))