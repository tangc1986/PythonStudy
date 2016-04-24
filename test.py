# -*- coding: utf-8 -*-
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
from SOAPpy import structType
from SOAPpy import headerType
from SOAPpy import SOAPProxy
n = 'http://WebXml.com.cn'
url = 'http://ws.webxml.com.cn/WebServices/WeatherWebService.asmx?wsdl'
ct = structType(data = {'Host' : 'www.webxml.com.cn',
                        'Content-Type':'text/xml; charset=utf-8',
                        'SOAPAction': "http://WebXml.com.cn/getWeatherbyCityName"})
ct._validURIs = []
ct._ns = ("ns1", "https://www.xxxxx.com/xxxx")
hd = headerType(data = {"AuthHeader" : ct})
server = SOAPProxy(url, namespace=n, soapaction="http://WebXml.com.cn/getWeatherbyCityName")
server.soapproxy.header = hd
server.config.dumpSOAPOut = 1
server.config.dumpSOAPIn = 1
server.getWeatherbyCityName(theCityName='58367')