import pandas as pd


# cores para saida
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CEND = '\033[0m'


# Opções de entrada
op = 0
while op != 6:
    print(15 * '__')
    print('[1] Consultar média de idade dos pacientes')
    print('[2] Consultar internações por ano')
    print('[3] Consultar hospitais')
    print('[4] Calcular tempo de internação')
    print('[5] Determinar tempos de espera na fila')
    print('[6] Sair do programa')
    print(15 * '__')

    # Entrada do usuário
    op = int(input('Escolha uma opção: '))

    # le os dados contidos no CSV
    dados = pd.read_csv('gerint_solicitacoes_mod.csv', encoding="utf-8", sep=";")

    # 1. [Consultar média de idade dos pacientes]
    if op == 1:
        # verifica se o municipio existe
        municipio_very = 0
        while municipio_very == 0:
            municipio = str(input('Digite o município residencial: '))
            cidade_df = dados[["municipio_residencia", "idade", "sexo"]][dados["municipio_residencia"] == municipio.upper()]
            municipio_very = cidade_df.shape[0]
            if municipio_very == 0:
                print(bcolors.FAIL + f'\nNão encontramos {municipio.title()}, digite um municipio valido!' + bcolors.CEND)
            else:

                # filtra os dados pelo municipio, idade e sexo
                cidade_df = dados[["municipio_residencia", "idade", "sexo"]][dados["municipio_residencia"] == municipio.upper()]

                # total dos pacientes
                total_df = cidade_df.shape[0]

                # separa pacientes por gênero
                sexo_f_df = cidade_df[cidade_df["sexo"] == "FEMININO"]
                sexo_m_df = cidade_df[cidade_df["sexo"] == "MASCULINO"]

                # média das idades por gênero e total
                mean_df_f = sexo_f_df['idade'].mean()
                mean_df_m = sexo_m_df['idade'].mean()
                mean_df_g = cidade_df['idade'].mean()

                # imprime o resultado por gênero

                print(bcolors.OKGREEN + '\nO número total de pacientes do município do {} é de: {:.0f}'.format(municipio.title(), total_df))
                print('\nA média de idade:\nmulheres {:.2f} anos.\nHomens {:.2f} anos.' .format(mean_df_f, mean_df_m))
                print('\nA média de idade de todos os pacientes é de {:.2f} anos.' .format(mean_df_g) + bcolors.CEND)

    # 2. [Consultar internações por ano]
    if op == 2:
        # verifica se o municipio existe
        municipio_very = 0
        while municipio_very == 0:
            municipio = str(input('Digite o município residencial: '))
            cidade_df = dados[["municipio_residencia", "idade", "sexo"]][dados["municipio_residencia"] == municipio.upper()]
            municipio_very = cidade_df.shape[0]
            if municipio_very == 0:
                print(bcolors.FAIL + f'\nNão encontramos {municipio.title()}, digite um municipio valido!' + bcolors.CEND)
            else:

                # converte datas para formato 'datetime64'
                dados['data_internacao'] = dados['data_internacao'].astype('datetime64')
                # dados.dtypes
                cidade_df = dados[["municipio_residencia", "data_internacao" ]][dados["municipio_residencia"] == municipio.upper()]
                # filtra as internações por ano
                ano_2018 = cidade_df[["data_internacao"]][cidade_df["data_internacao"].dt.year == 2018]
                ano_2019 = cidade_df[["data_internacao"]][cidade_df["data_internacao"].dt.year == 2019]
                ano_2020 = cidade_df[["data_internacao"]][cidade_df["data_internacao"].dt.year == 2020]
                ano_2021 = cidade_df[["data_internacao"]][cidade_df["data_internacao"].dt.year == 2021]

                # imprimi o resultado da consulta
                print(bcolors.OKGREEN + f"\nInternações em {municipio.title()}:\n2018: {ano_2018.shape[0]} \n2019: {ano_2019.shape[0]} \n2020: {ano_2020. shape[0]} \n2021: {ano_2021. shape[0]}" + bcolors.CEND)

    # 3. [Consultar hospitais]
    if op == 3:
        # verifica se o executante existe
        executante_very = 0
        while executante_very == 0:
            # entrada do usuário
            executante = str(input('Digite o nome do executante' + bcolors.OKBLUE + '\nEx.: Hospital Sao Lucas Da PUCRS ou Sao Lucas: ' + bcolors.CEND))
            executante_df = dados[["idade", "municipio_residencia", "solicitante", "data_autorizacao", "data_internacao", "data_alta", "executante"]][dados["executante"].str.contains(executante.upper())]
            executante_very = executante_df.shape[0]
            if executante_very == 0:
                print(bcolors.FAIL + f'\nNão encontramos {executante.upper()}, digite um executante valido!' + bcolors.CEND)
            else:

                # converte datas para formato 'datetime64'
                dados['data_autorizacao'] = dados['data_autorizacao'].astype('datetime64')
                dados['data_internacao'] = dados['data_internacao'].astype('datetime64')
                dados['data_alta'] = dados['data_alta'].astype('datetime64')

                # filtra idade, municipio de residencia, solicitante, data da autorizacao, internação e alta, executante
                executante_df = dados[["idade", "municipio_residencia", "solicitante", "data_autorizacao", "data_internacao", "data_alta", "executante"]]#[dados["executante"].str.contains(executante.upper)]

                # filtra os Hospitais por nomes ou parte dos nomes
                filter_executante_df = executante_df[executante_df["executante"].str.contains(executante.upper())]

                # resultado da consulta
                print(bcolors.OKGREEN + f"\nNo total o {executante.title()} teve {filter_executante_df.shape[0]} pacientes." + bcolors.CEND)

                print(filter_executante_df.head())
    # 4. [Calcular tempo de internação]
    if op == 4:
        # verifica se o solicitante existe
        solicitante_very = 0
        while solicitante_very == 0:
            # entrada do usuário
            solicitante = str(input('Digite o nome do solicitante' + bcolors.OKBLUE + '\nEx.: Hospital Sao Lucas Da PUCRS ou Sao Lucas: ' + bcolors.CEND))
            solicitante_df = dados[["executante", "solicitante", "data_solicitacao", "data_alta"]][dados["solicitante"].str.contains(solicitante.upper())]
            solicitante_very = solicitante_df.shape[0]
            if solicitante_very == 0:
                print(bcolors.FAIL + f'\nNão encontramos {solicitante.upper()}, digite um solicitante valido!' + bcolors.CEND)
            else:

                # converte datas para formato 'datetime64'
                dados['data_solicitacao'] = dados['data_solicitacao'].astype('datetime64')
                dados['data_autorizacao'] = dados['data_autorizacao'].astype('datetime64')
                dados['data_internacao'] = dados['data_internacao'].astype('datetime64')
                dados['data_alta'] = dados['data_alta'].astype('datetime64')

                # filtra as colunas que seram exibidas
                tempo_df = dados[["executante", "data_solicitacao", "data_alta"]][dados["solicitante"].str.contains(solicitante.upper())]
                # calcula dos dias de internação
                dias_internacao = tempo_df["data_alta"] - tempo_df['data_solicitacao']
                # inseri os dias de internação na tebela de saida
                tempo_df["dias_internados"] = dias_internacao

                print(bcolors.OKGREEN + f'\nTempo de internação, total de {tempo_df.shape[0]} pacientes' + bcolors.CEND)
                print(tempo_df)
    
    # 5. [Determinar tempos de espera na fila]
    if op == 5:
        # converte datas para formato 'datetime64'
        dados['data_solicitacao'] = dados['data_solicitacao'].astype('datetime64')
        dados['data_autorizacao'] = dados['data_autorizacao'].astype('datetime64')
        dados['data_internacao'] = dados['data_internacao'].astype('datetime64')
        dados['data_alta'] = dados['data_alta'].astype('datetime64')

        # filtra os dados por data
        espera_df = dados[["data_solicitacao", "data_internacao"]]
        # calcula dias na fila
        dias_espera = espera_df["data_internacao"] - espera_df['data_solicitacao']
        # inseri na tabela a nova coluna com dias na fila
        espera_df.insert(2, "dias_na_fila", dias_espera) 
        # separa o maoires tempos de internação imprimi
        print(bcolors.OKGREEN + "\nO cinco maiores tempos de internção são" + bcolors.CEND)
        print(espera_df[espera_df["dias_na_fila"].between('1200 days', '3000 days')])
    else:
        print(bcolors.FAIL + '\nDigite uma opção valida, para continuar!' + bcolors.CEND)

print('FIM!')
