class Operacoes:
    
    def calcular_media(self, notas):
    
        return sum(notas) / len(notas)
    
    def verificar_reprovacao(self, media):
      
        return media < 6
    
    def relatorio_reprovados(self, dados_alunos, matriculas_reprovados):
       
        relatorio = []
        for aluno in dados_alunos:
            if aluno['matricula'] in matriculas_reprovados:
                media = self.calcular_media(aluno['notas'])
                relatorio.append(
                    f"Aluno Reprovado: {aluno['nome']} – Matrícula: {aluno['matricula']} – Média Final: {media:.2f}"
                )
        return relatorio


if __name__ == "__main__":
   
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
