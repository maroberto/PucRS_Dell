import pandas as pd

print(10 * '__')
print('[1] Média de idade dos pacientes')
print('[2] Novos números')
print('[5] Sair do programa')
print(10 * '__')

op = 0
while op != 5:
    op = int(input('Qual é sua opção: '))

    if op == 1:
        municipio = str(input('Digite a cidade: '))
        dados = pd.read_csv('gerint_solicitacoes_mod.csv', encoding="utf-8", sep=";")
        dados.head()
        dados.shape
        idade_sexo = dados[["idade", "sexo", "municipio_residencia"]]
        idade_sexo.head()
        cidade = dados[dados["municipio_residencia"] == municipio.upper()]
        print(cidade.head())
        print(cidade.shape)
    if op == 2:
        op = int(input('Digite outra Opção: '))
print('FIM!')
