from webshell_crawler.spiders.spider.abstractWebshell_post_spider import AbstractWebshellPostSpider


class webshellPostSpiderKA_uShell(AbstractWebshellPostSpider):
    """
    webshell功能

    --  shell
    """
    name = "webshell_post_cmd"
    url = "http://localhost/dvwa/hackable/uploads/php-webshells-master/KA_uShell%200.1.6.php"

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
            payload = {'c': cmd, 'ac': 'shell'}
            yield self.submitPayload(url, payload)
