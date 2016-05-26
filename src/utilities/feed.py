# -*- coding: utf-8 -*-

import urllib2
import xmltodict

class Feed(object):
     
    def __init__(self,_type=None):
        pass
         
         
 
 
    def read(self):
        _file = urllib2.urlopen('http://www.pfconcept.com/portal/datafeed/globalstockfeed.xml')
        data = _file.read()
        _file.close()
        
        data = xmltodict.parse(data)
        skus=[]
        for index,row in enumerate(data['StockList']['Stock']):
            brand= row['@BU']
            sku=row['@SKU']
            avail=int(row['@Avail'])
            loc=row['@Loc']
            _next=row['@Next']
            if avail<=0:
                continue
            if brand not in ['BL','LE']:
                continue
            skus.append({'brand':brand,'sku':sku,'avail':avail,'loc':loc,'_next':_next})
            
        return skus
    