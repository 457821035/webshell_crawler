from webshell_crawler.spiders.spider.abstractWebshell_post_spider import AbstractWebshellPostSpider


class webshellPostSpiderC99locus(AbstractWebshellPostSpider):
    """
    webshell功能

    --  shell
    --  Tool
    --  很多很多
    """
    name = "webshell_post_C99locu"
    url = "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/c99_locus7s.php"

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
            payload = {'cmd': cmd, 'act': 'cmd', 'd': AbstractWebshellPostSpider.task_path, 'cmd_txt': '1', 'submit': 'Execute'}
            yield self.submitPayload(url, payload)

