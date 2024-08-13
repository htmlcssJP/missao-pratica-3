from operacoes import Operacoes

alunos = [
        {'nome': 'Maria', 'matricula': '26', 'notas': [8.0, 7.0, 5.0, 9.0]},
        {'nome': 'Ana', 'matricula': '101', 'notas': [9.0, 9.0, 8.0, 9.0]},
        {'nome': 'Joao', 'matricula': '13', 'notas': [6.0, 5.0, 5.0, 5.0]},
        {'nome': 'Agatha', 'matricula': '37', 'notas': [8.0, 6.0, 7.5, 9.0]},
        {'nome': 'Joaquim', 'matricula': '72', 'notas': [6.0, 5.5, 5.0, 7.0]},
        {'nome': 'Felix', 'matricula': '5', 'notas': [10.0, 8.0, 8.0, 8.0]},
    ]

operacoes = Operacoes()
matriculas_reprovados = []


for aluno in alunos:
    media = operacoes.calcular_media(aluno['notas'])
    
    if operacoes.verificar_reprovacao(media):
      
        matriculas_reprovados.append(aluno['matricula'])


relatorio = operacoes.relatorio_reprovados(alunos, matriculas_reprovados)


for linha in relatorio:
    print(linha)
