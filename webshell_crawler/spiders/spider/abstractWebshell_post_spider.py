import scrapy
from scrapy.spiders import CrawlSpider

from webshell_crawler import items


class AbstractWebshellPostSpider(CrawlSpider):
    """
    只提交post的抽象类，从此继承
    重写parse方法
    """

    # 允许爬取的域名
    allowed_domains = ["10.108.114.132"]
    # 这里存放要爬取的种子队列
    available_urls = [
        "http://localhost/dvwa/hackable/uploads/php-webshells-master/KA_uShell%200.1.6.php",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/DTool%20Pro.php",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/Dive%20Shell%201.0%20-%20Emperor%20Hacking%20Team.php",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/GRP%20WebShell%202.0%20release%20build%202018%20(C)2006,Great.php",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/KA_uShell%200.1.6.php",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/Liz0ziM%20Private%20Safe%20Mode%20Command%20Execuriton%20Bypass%20Exploit.php",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/Loaderz%20WEB%20Shell.php",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/Moroccan%20Spamers%20Ma-EditioN%20By%20GhOsT.php",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/NCC-Shell.php",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/PhpSpy%20Ver%202006.php",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/Predator.php",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/Safe_Mode%20Bypass%20PHP%204.4.2%20and%20PHP%205.1.2.php",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/SimAttacker%20-%20Vrsion%201.0.0%20-%20priv8%204%20My%20friend.php",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/Web-shell%20(c)ShAnKaR.php",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/Worse%20Linux%20Shell.php",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/c99_locus7s.php",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/dC3%20Security%20Crew%20Shell%20PRiV.php",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/erne.php",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/ex0shell.php",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/fatal.php",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/g00nshell-v1.3.php",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/lamashell.php",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/lolipop.php",
        "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/megabor.php",

    ]


    def parse(self, response):
        yield self.homepageParse(response)
        post_gen = self.submitPost(response.url)
        for eachPost in post_gen:
            yield eachPost

    # 第一页访问
    def homepageParse(self, response):
        webshell_item = items.WebshellCrawlerItem()

        webshell_item['request_url'] = response.url
        webshell_item['response_header'] = response.headers
        webshell_item['response_body'] = response.body
        webshell_item['response_status'] = response.status


        return webshell_item

    # 重写此方法
    def submitPost(self, url):
        payload = {}
        yield self.submitPayload(url, payload)

    def submitPayload(self, url, payload):
        # 存入url种子库
        return scrapy.FormRequest(
            url=url,
            method='POST',
            formdata=payload,
            meta={'post': payload},
            callback=self.parse_post,
            dont_filter=True
        )

    def parse_post(self, response):
        webshell_item = items.WebshellCrawlerItem()

        webshell_item['request_url'] = response.url
        webshell_item['response_header'] = response.headers
        webshell_item['response_body'] = response.body
        webshell_item['response_status'] = response.status
        webshell_item['post'] = response.meta['post']

        return webshell_item

    def get_command_list(self):
        return ["ls", "pwd", "whoami", "ifconfig", "cat /etc/passwd", "ps", "ls -la",  "df"]
