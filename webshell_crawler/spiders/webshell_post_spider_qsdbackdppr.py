from webshell_crawler.spiders.spider.abstractWebshell_post_spider import AbstractWebshellPostSpider


class webshellPostSpiderqsdBackdoor(AbstractWebshellPostSpider):
    """
    webshell功能

    --  shell
    """
    name = "webshell_post_qsdBackdoor"
    url = "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/qsd-php-backdoor.php"

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
            payload = {'c': cmd}
            yield self.submitPayload(url, payload)

