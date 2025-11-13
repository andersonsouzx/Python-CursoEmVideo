''' Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota 
- A media da turma
- A situação (opcional) 

Adicione também as docstrings da função '''

def notas(*n, sit= False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :param return: dicionário com várias informações sobre a situação da turma.
    '''
    r = {}
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / r['Total']

    if sit: # se a situação for True.
        if r['Média'] >= 7:
            r['Situação'] = 'Aprovado'
        elif r['Média'] >= 5:
            r['Situação'] = 'Recuperação'
        else:
            r['Situação'] = 'Reprovado'
    return r
    
resp = notas(5.5, 2.5, 9, 8.5, sit= True)
print(resp)
help(notas)