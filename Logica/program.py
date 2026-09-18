#entrada de dados
nota1=float(input("digite a primeira nota: "))
nota2=float(input("digite a segunda nota: "))
nota3=float(input("digite a terceira nota: "))
frequencia=float(input("digite a frequencia 0 a 100(%): "))


#validação(notas invalidas<0 ou >10)
if (nota1<0 or nota1>10 or
 nota2 <0 or nota2>10 or
 nota3<0 or nota3>10):
 print("Erro: nota(s) invalida, por favor digite uma nota(s) de 0 a 10")
#validação da frequência
elif frequencia <0 or frequencia>100:
 print("Erro: Frequência invalida por favor digite uma frequência de 0 a 100")
#cacular media
else:
  media=(nota1+nota2+nota3)/3
print(f"Média final:{media:.2f})")

if frequencia <75:
print("situação:Reprovado por faltas")
elif media>=7:
print("situação:Aprovado na media")
elif media>=4:
 print("situação:Exame")
  print(f"faltaram: {7-media:.2f} pontos para ser aproado direto")
 else:
        print("situação:reprovado")
        print(f"faltam: {7-media:.2f} pontos para ser aprovado")