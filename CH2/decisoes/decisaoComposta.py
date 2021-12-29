nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectiocontagiosa=input("Suspeita de doença infectio-contagiosa?").upper()
if idade >= 65:
    print("O paciente " + nome + " POSSUI atendimento prioritário!")
elif doenca_infectiocontagiosa == "SIM":
    print("O paciente " + nome + " deve ser direcionado para sala de espera reservada.")
else:
    print("O paciente " + nome + " NÃO possui atendimento prioritário e pode aguardar na sala comum!")