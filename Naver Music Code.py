
scrapy shell "http://music.naver.com/search/search.nhn?query=%EB%B9%84+%EC%98%A4%EB%8A%94&x=0&y=0"

a=response.xpath('//*[@id="content"]/div[4]/div[2]/table/tbody/tr/td[3]/a[3]/@title').extract()
a

b=response.xpath('//*[@id="content"]/div[4]/div[2]/table/tbody/tr/td[4]/a/@title').extract()
b

c=response.xpath('//*[@id="content"]/div[4]/div[2]/table/tbody/tr/td[5]/a/@title').extract()
c

for k in range(0,14):
	print a[k].strip(),
	print "-",
	print b[k].strip(),
	print "-",
	print c[k].strip()
