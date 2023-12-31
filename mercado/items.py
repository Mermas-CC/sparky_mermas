# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MercadoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #info de producto
    titulo = scrapy.Field()
    valoracion = scrapy.Field()
    precio = scrapy.Field()
    ventas = scrapy.Field()
    disponibles = scrapy.Field()
    envio = scrapy.Field()
    tienda = scrapy.Field()
    valorizacion = scrapy.Field()
    ventas_vendedor = scrapy.Field()
   