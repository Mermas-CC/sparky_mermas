# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from mercado.items import MercadoItem

class MercadoSpider(CrawlSpider):
	name = 'mercado'
	item_count = 0
	allowed_domain = ['www.mercadolibre.com.pe']
	start_urls = ['https://listado.mercadolibre.com.pe/laptops#menu=categories']

	rules = {
		# Para cada item
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//a[@class="andes-pagination__link shops__pagination-link ui-search-link"]'))),
		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//a[@class="ui-search-item__group__element shops__items-group-details ui-search-link"]')),
							callback = 'parse_item', follow = False)
	}

	def parse_item(self, response):
		ml_item = MercadoItem()
		#info de producto
		ml_item['titulo'] = response.xpath('normalize-space(//h1[@class="ui-pdp-title"]/text())').extract()
		ml_item['valoracion'] = response.xpath('normalize-space(//span[@class="ui-pdp-review__rating"]/text())').extract()
		ml_item['precio'] = response.xpath('normalize-space(//div[@class="ui-pdp-price__second-line"]/span/span[@class="andes-visually-hidden"]/text())').extract()
		ml_item['ventas'] = response.xpath('normalize-space(//span[@class="ui-pdp-subtitle"]/text())').extract()
		ml_item['disponibles'] = response.xpath('normalize-space(//span[@class="ui-pdp-buybox__quantity__available"]/text())').extract()
		ml_item['envio'] = response.xpath('normalize-space(//span[@class="ui-pdp-color--GREEN ui-pdp-family--SEMIBOLD"]/text())').extract()
		ml_item['tienda'] = response.xpath('normalize-space(ui-pdp-family--SEMIBOLD/text())').extract()
		ml_item['valorizacion'] = response.xpath('normalize-space(//p[@class="ui-seller-info__status-info__title ui-pdp-seller__status-title"]/text())').extract()
		ml_item['ventas_vendedor'] = response.xpath('normalize-space(//strong[@class="ui-pdp-seller__sales-description"]/text())').extract()

		self.item_count += 1
		if self.item_count > 250:
			raise CloseSpider('item_exceeded')
		yield ml_item
