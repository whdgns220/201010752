activate py27

scrapy shell "https://www.google.com/finance/historical?q=KRX%3AKOSPI200&ei=Igf_V4HVN5CF0gSP4K-IBw"

a = response.xpath('//*[@id="prices"]/table/tr/td/text()').extract()

a

