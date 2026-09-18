


    # with open('betinhas.csv','w', enconding ="utf-8") as arquivo:
    # arquivo.write("nome,departamento,salario,anos_empresa\n")
    # arquivo.write("Jhesyel,Tecnologia,4500.00,3\n")
    # arquivo.write("Kauan,Engenheiro,6000.00,10\n")
    # arquivo.write("Felipe,Empresario,50000.00,11\n")
    # arquivo.write("Isabella,Analista,5000.00,23\n")
    # arquivo.write("Pietro,QA,7000.00,14\n")
    # arquivo.write("Leonardo,Pedreiro,17000.00,10\n")
    # arquivo.write("Alpha,Sigma,88888.00,10\n")


import csv
with open('betinhas.csv','r', encoding ="utf-8") as arquivo:
    leitor = csv.reader(arquivo)

    #next(leitor)

    for linha in leitor:
       nome = linha[0]
       nome = linha[1]
       nome = linha[2]
       nome = linha[3]

import csv
 
funcionarios = []
 
with open("funcionarios.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
 
    next(leitor)
 
    for linha in leitor:
        nome = linha[0]
        departamento = linha[1]
        salario = float(linha[2])
        anos = int(linha[3])
 
        if anos > 3:
            funcionarios.append([nome, departamento, salario, anos])
 
total_salarios = sum(funcionario[2] for funcionario in funcionarios)
 
media = total_salarios / len(funcionarios)
 
for funcionario in funcionarios:
    nome = funcionario[0]
    salario = funcionario[2]
 
    if salario > media:
        faixa = "Acima da média"
    else:
        faixa = "Abaixo da média"
 
    print(nome, "-", faixa)