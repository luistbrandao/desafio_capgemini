import sqlite3

conn = sqlite3.connect('sessao_cadastro.db')
cursor = conn.cursor()


class Cadastro:
    def __init__(self):
        pass

    def insert(self, anuncio, cliente, data_inicio, data_termino, investimento):
        cursor.execute("insert into cadastro (anuncio, cliente, data_inicio, data_termino, investimento) values" 
            (anuncio, cliente, data_inicio, data_termino, investimento)

        conn.commit()
        print('Inserção confirmada!')

        conn.close()


    def realizar_consulta(self):
        try:
            nome = input('Insira o nome do cliente: ')
            consulta = ('select * from cadastro where cliente = {}'.format(nome))
            cursor.execute(consulta)
            conn.commit()
            linhas = cursor.fetchone()

            for linha in linhas:
                print(linha)

        except Exception as erro:
            print('Erro')

        finally:
            conn.close()

    def realizar_consulta_data(self, data1, data2):
        try:
            consulta = ('select * from cadastro where data_inicio = ' data1 'and data_termino = ' data2)
            cursor.execute(consulta)
            conn.commit()
            linhas = cursor.fetchone()

            for linha in linhas:
                print(linha)
        except Exception as erro:
            print('Erro ao consultar')
        
        finally:
            conn.close()