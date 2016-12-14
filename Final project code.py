##item.py 정의


import scrapy


class RTItem(scrapy.Item):
    a = scrapy.Field()


##spider.py 정의




import scrapy
from rttt_crawler.items import RTItem

class RTSpider(scrapy.Spider):
    name = "Predict"
    allowed_domains = ["go.kr"]
    start_urls = [
        "http://www.kma.go.kr/weather/observation/past_table.jsp?stn=108&yy=2015&obs=07&x=18&y=9"
    ]
    
    def parse(self,response):
        item = RTItem()
        item['a'] = response.xpath('//*[@id="content_weather"]/table/tbody/tr/td/text()').extract()
        yield item


위에 코딩은 생략된 것으로써 뽑아내고자 하는 9개의 변수(평균기온,최저기온,최고기온,강수량,평균풍속,상대습도,일조시간,운량,날씨) 중에서 1개 변수만 선정하여 
5년치 중에서 1년치에 해당하는 양이기 때문에 실제로는 이와 같은 과정을 총 9개의 변수 * 5년치 = 45번을 반복하였습니다.
Scrapy project를 만들어 item.py와 spiders만 이용하였습니다.
또한 csv파일로 변환하는 것은 Scrapy Pipeline이 아닌 Anaconda Prompt를 통해서 만들었으며 R을 활용한 머신러닝 코드는 파이썬이 아니므로 올리지 않았습니다. 
