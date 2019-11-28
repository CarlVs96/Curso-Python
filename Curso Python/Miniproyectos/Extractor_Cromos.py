from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

class Cartas(Item):
	cuantasTiene = Field()
	cuantasTengo = Field()

class CromosRepes(Spider):
	nombre = "Primer Spider"
	urlInicial = "https://www.cromosrepes.com/buscador/coleccion/107706/6294"
	def parse(self, response):
		sel = Selector(response)
		datos = sel.xpath('//div[@id="panel-footer"]')