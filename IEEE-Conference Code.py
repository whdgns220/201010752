
scrapy shell "https://www.ieee.org/conferences_events/index.html"

a=response.xpath('//*[@id="inner-container"]/div[5]/div[2]/div[2]/div[2]/div[1]/div/div[1]/p/a/text()').extract()
a

b=response.xpath('//*[@id="inner-container"]/div[5]/div[2]/div[2]/div[2]/div[1]/div/div[1]/p/text()').extract()
b

for k in range(0,4):
	print a[k].strip(),
	print b[k].strip()
