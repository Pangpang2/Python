from lxml import etree


class Order(object):

    def __init__(self):
        pass

    def order(self):
        root = etree.parse(r'E:\Git\Python\tools\Reversion\data\dental -parser.xml')

