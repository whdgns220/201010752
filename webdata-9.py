%%writefile src/ds_web_data_textpost.py
import scrapy

class TextPostItem(scrapy.item.Item):
    title = scrapy.item.Field()
    url = scrapy.item.Field()
    submitted = scrapy.item.Field()

class RedditCrawler(scrapy.spiders.CrawlSpider):
    name = 'reddit_crawler'
    allowed_domains = ['reddit.com']
    start_urls = ['https://www.reddit.com/r/learnpython/new']
    custom_settings = {
        'BOT_NAME': 'reddit-scraper',
        'DEPTH_LIMIT': 3,
        'DOWNLOAD_DELAY': 3
    }
    def parse(self, response):
        s = scrapy.selector.Selector(response)
        next_link = s.xpath('//span[@class="nextprev"]//a/@href').extract()[0]
        if len(next_link):
            print "--> visiting ",next_link
            yield self.make_requests_from_url(next_link)
        posts = scrapy.selector.Selector(response).xpath('//div[@id="siteTable"]/div[@onclick="click_thing(this)"]')
        for post in posts:
            i = TextPostItem()
            i['title'] = post.xpath('div[2]/p[1]/a/text()').extract()[0]
            i['url'] = post.xpath('div[2]/ul/li[1]/a/@href').extract()[0]
            i['submitted'] = post.xpath('div[2]/p[2]/time/@title').extract()[0]
            print "crawling ",i['title']
            yield i


!scrapy runspider src/ds_web_data_textpost.py -o src/ds_web_data_textpost.json -t json --logfile src/ds_web_data_textpost.logfile
