from webshell_crawler.spiders.spider.abstractWebshell_post_spider import AbstractWebshellPostSpider


class webshellPostSpiderSimAttacker(AbstractWebshellPostSpider):
    """
    webshell功能

    --  shell
    --  File
    --  mail-dos
    --  connect back
    """
    name = "webshell_post_SimAttacker"
    url = "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/SimAttacker%20-%20Vrsion%201.0.0%20-%20priv8%204%20My%20friend.php"

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
            payload = {'cmd': cmd, 'id': 'cmd'}
            yield self.submitPayload(url+"?id=cmd", payload)

