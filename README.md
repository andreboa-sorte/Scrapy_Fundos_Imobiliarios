# Scrapy_Fundos_Imobiliarios

<strong>Itens ultilizados e versoniamentos:</strong>
* Python 3.9.0
* Scrapy 2.4.1 

<strong>Preciso baixar algo?</strong><br>
É necessario ter o Python instalado e o Scrapy (*pip install scrapy*).<br>
Por ultimo, ter uma IDE de sua preferencia, para rodar o projeto.<br>

<strong>Como faço para funcionar o codigo?</strong>
* Basta baixar ou clonar o codigo, caso não tenha instalado o <strong>Scrapy</strong>, instale ele.
* Abra o terminal e esteja dentro da pasta do projeto, depois basta rodar o comando: <br>
* scrapy crawl procuraFII -o (*nome do arquivo a ser gerado* + .csv ou qualquer extensão desejada).<br>
 **Exemplo**: scrapy crawl procuraFII -o DadosFundosImobiliarios.csv

### Onde vejo o codigo que foi criado e posso alteralo?
#### Caso deseja alterar a esturua do codigou ou A estrutura do site seja alterada e o Xpaht não funione mais.

* Entre na pasta *Spiders*, abra o arquivo **procuraFII** e lá será encontrado todos o codigo feito e seu comentario explicando cada função. 

