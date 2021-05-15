import datetime

info = {

}

class Cadastro:
    def __init__(self, nome_anuncio, cliente, data_inicio, data_termino, investimento_dia):
        self.nome_anuncio = nome_anuncio
        self.cliente = cliente
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.investimento_dia = investimento_dia

    def cadastrar(cliente, inicio, fim, investimento, nome_anuncio):
        info.update({
            "Cliente": cliente,
            "Valor investido": investimento,
            "Data início": inicio,
            "Data Final": fim,
            "Nome do anúncio": nome_anuncio
        })

    def converter_data(dia, mes, ano):
        data_inicio = datetime.datetime(
            year = ano, 
            month = mes,
            day = dia)
        return data_inicio

    def dif_dias(data1, data2):
        diferenca = data2 - data1
        return diferenca

    op = 0
    while op != 3:
        print("1- Cadastro de anúncios")
        print("2- Relatórios")
        print("3- Sair")
        op = int(input("Digite sua opção: "))

        if op == 1:
            nome_cliente = input("Digite o nome do cliente: ")
            nome_anuncio = input("Digite o nome do anúncio: ")
            dia_inicio = input("Digite o dia de início: ")
            mes_inicio = input("Digite o mês de início: ")
            ano_inicio = input("Digite o ano de início: ")

            data1 = converter_data(dia_inicio, mes_inicio, ano_inicio)

            dia_fim = input("Digite o dia de fim: ")
            mes_fim = input("Digite o mês de fim: ")
            ano_fim = input("Digite o ano de fim: ")

            data2 = converter_data(dia_fim, mes_fim, ano_fim)

            #verifica diferença de dias para cálculo
            dif = dif_dias(data1, data2) 

            total_investo = dif * investimento_por_dia
            visual = total_invest * 30
            clique = visual * 0.12
            compartilhamentos = clique * 0.15
            visualiz = compartilhamentos * 40

            cadastrar(nome_cliente, data1, data2, total_investo, nome_anuncio)
            banco.insert(self, nome_anuncio, nome_cliente, data1, data2, investimento)


        elif op == 2:
            op2 = 0
            while op2 != 3:
                print("1- Pesquisar por nome")
                print("2- Pesquisar por data")
                print("3- Sair")
                op2 = input("Digite sua opção: ")
                
                if op2 == 1:
                    nome_pesquisa = input("Digite o nome do cliente a ser procurado: ")
                    banco.realizar_consulta()
                
                else:
                    data_pesquisa = input("Digite a data inicial a ser pesquisada: ")
                    dia = input("Digite o dia de inicio: ")
                    mes = input("Digite o mês de inicio: ")
                    ano = input("Digite o ano de inicio: ")

                    data1 = converter_data(dia, mes, ano)

                    dia2 = input("Digite o dia de fim: ")
                    mes2 = input("Digite o mês de fim: ")
                    ano2 = input("Digite o ano de fim: ")

                    data2 = converter_data(dia2, mes2, ano2)
                    banco.realizar_consulta_data(data1, data2)

                    data3 = converter_data(dia, mes, ano)
                    dif = dif_dias(data3, data2)
                    total_investo = dif * investimento_por_dia
                    visual = total_invest * 30
                    clique = visual * 0.12
                    compartilhamentos = clique * 0.15
                    visualiz = compartilhamentos * 40

                    print("Total investido foi de: R$ ", total_investo)
                    print("Quantidade máxima de visualizações: ", visualiz)
                    print("Quantidade máxima de cliques: ", clique)
                    print("Quantidade máxima de compartilhamentos: ", compartilhamentos)
        
        else:
            return
