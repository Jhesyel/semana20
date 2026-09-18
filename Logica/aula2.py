aviso_1 = "LearnNow informa:seu prazo de entrega venca em 3 dias. "
aviso_2 = "LearnNow informa: atividade enviada com sucesso."
aviso_3 = "Atenção: o prazo foi encerrado. Contate o surporte LearnNow."

print(aviso_1.find("LearnNow"))
print(aviso_2.find("LearnNow"))
print(aviso_3.find("LearnNow"))

print('prazo' in aviso_1)
print('prazo' in aviso_2)
print('prazo' in aviso_3)

novo_aviso_1 = aviso_1.replace ("LearnNow", "EduTech")
print(novo_aviso_1)

novo_aviso_2 = aviso_2.replace ("LearnNow", "EduTech")
print(novo_aviso_2)

novo_aviso_3 = aviso_3.replace ("LearnNow", "EduTech")
print(novo_aviso_3)

avisos = [aviso_1, aviso_2, aviso_3]

for aviso in avisos:
    aviso_atualizados = aviso.replace ("LearnNow", "Edutech")
    prazo_posicao = aviso_atualizados.find ("LearnNow")
    if prazo_posicao != -1:
        print (f"[PEDAGÓGICO] prazo encpntrado na posição {prazo_posicao}:")
    print(f"[GERAL] {aviso_atualizados}")