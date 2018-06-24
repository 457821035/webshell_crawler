from webshell_crawler.spiders.spider.abstractWebshell_post_spider import AbstractWebshellPostSpider


class webshellPostSpiderDc3(AbstractWebshellPostSpider):
    """
    webshell功能

    --  shell
    --  mails
    --  php
    --  env
    -- file
    """
    name = "webshell_post_Dc3"
    url = "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/dC3%20Security%20Crew%20Shell%20PRiV.php"

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
            payload = {'sub': 'Execute', 'command': cmd, 'method': '1'}
            yield self.submitPayload(url+"??&secret&exec_st", payload)

