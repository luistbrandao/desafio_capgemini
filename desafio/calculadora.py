# 1ª Parte - Considere os seguintes critérios fictícios para desenvolver a calculadora de alcance de anúncio:

# Baseados em dados de análise de anúncios anteriores, a agência tem os seguintes dados:

#    a cada 100 pessoas que visualizam o anúncio 12 cliquesm nele.
#    a cada 20 pessoas que cliquesm no anúncio 3 compartilham nas redes sociais.
#    cada compartilhamento nas redes sociais gera 40 novas visualizações.
#    30 pessoas visualizam o anúncio original (não compartilhado) a cada R$ 1,00 investido.
#    o mesmo anúncio é compartilhado no máximo 4 vezes em sequência


class Calculadora:

    def __init__(self, visualizacoes, pessoas, valor_investido):
        self.visualizacoes = visualizacoes
        self.pessoas = pessoas
        self.valor_investido = valor_investido

    def definir_visualizacoes(self):
        clique_anuncio = 0

        if self.definir_visualizacoes >= 100:
            quantidade = self.definir_visualizacoes / 100
            return int (quantidade * 12)
            
        else:
            return print('Quantidade de vizualizações é menor que 100')

    def shares(self):
        quant_shares = 0
        cliques = 0
        sequencia = 0
        visualizacao_rede_compartilhada = 0

        if self.pessoas >= 20:
            cliques = self.pessoas / 20
            quant_shares = int(cliques * 3)
            visualizacao_rede_compartilhada = int(quant_shares * 40)

            if visualizacao_rede_compartilhada >= 100:
                 self.definir_visualizacoes = int (visualizacao_rede_compartilhada)
                 self.definir_visualizacoes()

            if quant_shares <= 4:
                 self.shares()

            return visualizacao_rede_compartilhada
            
        else:
            return print('A quantidade de pessoas é menor que 20')

    def valor_total(self):
        anuncio_valor = float(self.valor_investido * 30)
        return round(anuncio_valor + 0.5)


visu = int(input("Digite a quantidade de visualizações: "))
pes = int(input("Digite a quantidade de pessoas: "))
valor = float(input("Digite o valor investido: "))

calc = Calculadora(visu, pes, valor)

print(calc.shares())
print(calc.valor_total())