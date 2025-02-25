def notas(situacao=False):
    """ 
    Calcula estatísticas das notas de um aluno.

    Esta função recebe múltiplas notas, calcula a quantidade total, a maior e a menor nota, além da média. Opcionalmente, pode indicar a situação do aluno com base na média.

    :param situacao: (opcional) Se True, adiciona a situação do aluno ('BOA', 'RAZOÁVEL' ou 'RUIM'). Se False, não exibe a situação. Padrão: False.

    :return: Um dicionário com as seguintes chaves:
        - 'total': total de notas inseridas
        - 'maior': maior nota
        - 'menor': menor nota
        - 'media': média das notas
        - 'situacao' (opcional): classificação da média (aparece apenas se situacao=True)
    """

    alunos = {}
    tdsNotas = []
    soma = 0
    
    alunos['total'] = int(input('Quantidade de notas? '))

    if alunos['total'] == 0:
        alunos['maior'] = alunos['menor'] = alunos['media'] = None

        return alunos

    soma = 0

    for c in range(alunos['total']):
        nota = int(input(f'Digite a {c+1}° nota: '))

        tdsNotas.append(nota)
        soma += nota
    
    alunos['maior'] = max(tdsNotas)
    alunos['menor'] = min(tdsNotas)
    alunos['media'] = soma / alunos['total']

    if situacao:
        if alunos['media'] >= 7:
            alunos['situacao'] = 'BOA'
        elif alunos['media'] >= 5:
            alunos['situacao'] = 'RAZOÁVEL'
        else:
            alunos['situacao'] = 'RUIM'
    
    return alunos


print('-' * 30)
result = notas(situacao=False)
print(result)
print()
    


