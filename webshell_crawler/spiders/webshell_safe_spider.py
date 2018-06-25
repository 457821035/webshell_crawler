import scrapy
from scrapy.spiders import CrawlSpider

from webshell_crawler import items


class WebshellSafeSpider(CrawlSpider):
    """
    爬取深度：安全起见建议 2
    这里的webshell都是安全的，不会删除文件系统
    """
    name = "webshell_safe"

    # 允许爬取的域名
    allowed_domains = ["10.108.114.132"]
    # 这里存放要爬取的种子队列
    start_urls = [
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/AK-74%20Security%20Team%20Web%20Shell%20Beta%20Version.php",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/CrystalShell%20v.1.php",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/GRP%20WebShell%202.0%20release%20build%202018%20(C)2006,Great.php",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/KA_uShell%200.1.6.php",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/NCC-Shell.php",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/Small%20Web%20Shell%20by%20ZaCo.php",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/cpanel.php",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/ex0shell.php",

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
        for url in response.xpath('//a/@href').extract():
            url = response.url + url
            yield scrapy.Request(url, method="GET", callback=self.parse)
