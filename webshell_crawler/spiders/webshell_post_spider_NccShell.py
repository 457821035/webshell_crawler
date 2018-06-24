from webshell_crawler.spiders.spider.abstractWebshell_post_spider import AbstractWebshellPostSpider


class webshellPostSpiderNccShell(AbstractWebshellPostSpider):
    """
    webshell功能

    --  shell
    --  upload
    """
    name = "webshell_post_NCCShell"
    url = "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/NCC-Shell.php"

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
            payload = {'-cmd': cmd}
            yield self.submitPayload(url, payload)

