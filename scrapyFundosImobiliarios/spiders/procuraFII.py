import scrapy
#pip install scrapy


class ProcurafiiSpider(scrapy.Spider):
    name = 'procuraFII'
    #allowed_domains = ['https://www.fundamentus.com.br/fii_resultado.php']
    start_urls = ['http://www.fundamentus.com.br/fii_resultado.php/']  #o link q sera "scrapydo".
                                                                            #como é somente vamos pegar os dados de um dominio,
                                                                            #então não vamos usar o allowed_domains

    def parse(self, response):
        lista = response.xpath('//*[@id="tabelaResultado"]/tbody/tr')
        i = 0
        for itemlita in lista: #um laço de repetição para pegar todos os dados da "caixa grande"
            i = int(i)
            i = i + 1
            i = str(i)
            # aqui nesse metodo é pego os dados que se deseja exrair e é botado nas variaveis
            Papel = itemlita.xpath('//*[@id="tabelaResultado"]/tbody/tr['+i+']/td[1]/span/a/text()').extract_first()
            Segmento = itemlita.xpath('//*[@id="tabelaResultado"]/tbody/tr['+i+']/td[2]/text()').extract_first()
            Cotacao = itemlita.xpath('//*[@id="tabelaResultado"]/tbody/tr['+i+']/td[3]/text()').extract_first()
            FFOYield = itemlita.xpath('//*[@id="tabelaResultado"]/tbody/tr['+i+']/td[4]/text()').extract_first()
            DividendYield = itemlita.xpath('//*[@id="tabelaResultado"]/tbody/tr['+i+']/td[5]/text()').extract_first()
            P_VP = itemlita.xpath('//*[@id="tabelaResultado"]/tbody/tr['+i+']/td[6]/text()').extract_first()
            ValorMercado = itemlita.xpath('//*[@id="tabelaResultado"]/tbody/tr['+i+']/td[7]/text()').extract_first()
            Liquidez = itemlita.xpath('//*[@id="tabelaResultado"]/tbody/tr['+i+']/td[8]/text()').extract_first()
            QtdImoveis = itemlita.xpath('//*[@id="tabelaResultado"]/tbody/tr['+i+']/td[9]/text()').extract_first()
            PrecoP_M2 = itemlita.xpath('//*[@id="tabelaResultado"]/tbody/tr['+i+']/td[10]/text()').extract_first()
            AlugelP_M2 = itemlita.xpath('//*[@id="tabelaResultado"]/tbody/tr['+i+']/td[11]/text()').extract_first()
            CapRate = itemlita.xpath('//*[@id="tabelaResultado"]/tbody/tr['+i+']/td[12]/text()').extract_first()
            VacanciaMed = itemlita.xpath('//*[@id="tabelaResultado"]/tbody/tr['+i+']/td[13]/text()').extract_first()

            # o "yield" é o comando ultilizado para ele fazer uma função ou interação
            yield {#depois de coletados, as informações são organizadas para q possão ser salvas e são salvas depois
                'Papel' : Papel,
                'Segmento' : Segmento,
                'Cotacao' : Cotacao,
                'FFOYield' : FFOYield,
                'DividendYield' : DividendYield,
                'P/VP' : P_VP,
                'ValorMercado' : ValorMercado,
                'Liquidez' : Liquidez,
                'QuantidadeDeImoveis' : QtdImoveis,
                'PrecoPorM2' : PrecoP_M2,
                'AlugelPorM2': AlugelP_M2,
                'CapRate' : CapRate,
                'VacanciaMedia' : VacanciaMed,
            }

