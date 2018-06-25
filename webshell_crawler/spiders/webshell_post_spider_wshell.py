from webshell_crawler.spiders.spider.abstractWebshell_post_spider import AbstractWebshellPostSpider


class webshellPostSpiderWshell(AbstractWebshellPostSpider):
    """
    webshell功能

    --  shell
    """
    name = "webshell_post_Wshell"
    url = "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/php-include-w-shell.php"

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
            payload = {'cmd': cmd}
            yield self.submitPayload(url+"?mysql_web_admin_username=&mysql_web_admin_password=&security=high&PHPSESSID=91e8abcd474afa30fde7949238823dea&cmdln=1&", payload)

