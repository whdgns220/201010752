activate py27

scrapy shell "https://www.google.com/finance/historical?q=KRX:KOSPI200&ei=Ujr_V8mvEsLY0gSWlIjACA"

a = response.xpath('//*[@id="prices"]/table/tr/td[1]/text()').extract()

a

b = response.xpath('//*[@id="prices"]/table/tr/td[2]/text()').extract()

b

c = response.xpath('//*[@id="prices"]/table/tr/td[3]/text()').extract()

c

d = response.xpath('//*[@id="prices"]/table/tr/td[4]/text()').extract()

d

e = response.xpath('//*[@id="prices"]/table/tr/td[5]/text()').extract()

e

f = response.xpath('//*[@id="prices"]/table/tr/td[6]/text()').extract()

f

for k in range(0,30):
	print a[k].strip(),
	print "-",
	print b[k].strip(),
	print "-",
	print c[k].strip(),
	print "-",
	print d[k].strip(),
	print "-",	
	print e[k].strip(),
	print "-",
	print f[k].strip()
	

