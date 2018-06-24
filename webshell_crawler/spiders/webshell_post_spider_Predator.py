from webshell_crawler.spiders.spider.abstractWebshell_post_spider import AbstractWebshellPostSpider


class webshellPostSpiderPredator(AbstractWebshellPostSpider):
    """
    webshell功能

    --  shell
    --  Spammer
    --  FTP-Brute
    --  Flooder
    --  md5
    --  Bind port
    --  Back Connect
    --  Download
    """
    name = "webshell_post_Predator"
    url = "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/Predator.php"

    # 允许爬取的域名
    allowed_domains = AbstractWebshellPostSpider.allowed_domains
    # 这里存放要爬取的种子队列
    if url in AbstractWebshellPostSpider.available_urls:
        start_urls = [url]
    else:
        start_urls = []


    def submitPost(self, url):
        command_list = self.get_command_list()
        for cmd in command_list:
            payload = {'value': cmd, 'type': '2'}
            yield self.submitPayload(url, payload)

