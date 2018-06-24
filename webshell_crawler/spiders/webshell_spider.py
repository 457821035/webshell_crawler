import scrapy
from scrapy.contrib.spiders import CrawlSpider

from webshell_crawler import items


class WebshellSpider(CrawlSpider):
    """
    爬取深度：1
    """
    name = "webshell_index"

    # 允许爬取的域名
    allowed_domains = ["10.108.114.132"]
    # 这里存放要爬取的种子队列
    start_urls = [
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/Macker's%20Private%20PHPShell.php",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/nshell.php",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/simattacker.php",

    ]


    def parse(self, response):
        webshell_item = items.WebshellCrawlerItem()

        webshell_item['request_url'] = response.url
        webshell_item['response_header'] = response.headers
        webshell_item['response_body'] = response.body
        webshell_item['response_status'] = response.status

        yield webshell_item


        url_prefix = "http://10.108.114.132"

        # 存入url种子库
        for url in response.xpath('//tr/td/a/@href').extract():
            url = response.url + url
            yield scrapy.Request(url, method="GET", callback=self.parse)



            # doc = ''
            # for sel in response.xpath('//div[2]/article/div/header/h1'):
            #     webshell_item['title'] = sel.xpath('a/text()').extract()[0]
            #     webshell_item['link'] = sel.xpath('a/@href').extract()[0]
            #     doc = doc + str(webshell_item['title']) + "\t" + str(webshell_item['link']) + "\n"