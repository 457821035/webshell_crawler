# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WebshellCrawlerPipeline(object):

    def process_item(self, item, spider):
        return item


class WriterPipeline(object):
    """
    父类，所有写pipeline都从这继承
    """
    def __init__(self):
        self.store_path = '/Users/gavia/File/Gavia/Lab/work/webshell_crawler/webshell_pages/'
        self.filename = 'webshell_test'
        # self.file = self.openFile(self.store_path, self.filename, 'w')
        self.column_list = ['request_url', 'post', "response_header", "response_body", 'response_status']
        self.sep = '<--->'
        # self.writeColumnName(self.column_list, self.file)

        # self.file = self.openFile(self.store_path, self.filename, 'a')


    def process_item(self, item, spider):
        if spider.name != "webshell_test":
            return item

        return self.output(spider, item)

    def output(self, spider, item):
        print("==="*40)
        print("[", spider.name, "] :", item['request_url'])
        print("==="*40)

        transHeader = {key.decode('utf-8'): [x.decode("utf-8") for x in value] for (key, value) in item['response_header'].items()}

        try:
            transBody = item['response_body'].decode("utf-8")
        except UnicodeDecodeError:
            transBody = str(item['response_body']).replace("b\'", "'")

        if transBody.strip() == "":
            transBody = str(None)

        if "post" not in item.keys() or str(item['post']).replace("{","").replace("}","").strip() == "":
            item['post'] = str(None)

        line = str(item['request_url']) + self.sep + str(item['post']) + self.sep +str(transHeader) + self.sep \
               + transBody.replace("\n","").replace("\r","") + self.sep + str(item['response_status']) + "\n"
        self.file.write(line)
        return item
    
    def writeColumnName(self, column_list, file):
        first_line = ""
        for colName in column_list:
            first_line += colName + self.sep

        first_line = first_line.strip(self.sep)
        first_line += "\n"
        file.write(first_line)

    def openFile(self, store_path, filename, mode):
        return open(store_path + filename, mode)


class WriterIndexPipeline(WriterPipeline):
    """
    写一般get的
    """
    def __init__(self):
        super(WriterIndexPipeline, self).__init__()
        self.filename = 'webshell_index'
        self.file = self.openFile(self.store_path, self.filename, 'w')
        self.writeColumnName(self.column_list, self.file)

        self.file = self.openFile(self.store_path, self.filename, 'a')

    def process_item(self, item, spider):
        if spider.name != "webshell_index":
            return item

        return self.output(spider, item)


class WriterSafePipeline(WriterPipeline):
    """
    写只爬两层的
    """
    def __init__(self):
        super(WriterSafePipeline, self).__init__()
        self.filename = 'webshell_safe'
        self.file = self.openFile(self.store_path, self.filename, 'w')
        self.writeColumnName(self.column_list, self.file)

        self.file = self.openFile(self.store_path, self.filename, 'a')

    def process_item(self, item, spider):
        if spider.name != "webshell_safe":
            return item

        return self.output(spider, item)


class WriterPostPipeline(WriterPipeline):
    """
    写Post的
    """
    def __init__(self):
        super(WriterPostPipeline, self).__init__()
        self.filename = 'webshell_post'
        self.file = self.openFile(self.store_path, self.filename, 'w')
        self.writeColumnName(self.column_list, self.file)

        self.file = self.openFile(self.store_path, self.filename, 'a')


    def process_item(self, item, spider):
        if spider.name.find("webshell_post") < 0:
            return item

        return self.output(spider, item)
