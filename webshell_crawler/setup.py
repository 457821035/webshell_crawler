from setuptools import setup

setup(name='scrapy-mymodule',
      entry_points={
          'scrapy.commands': [
              'crawl_webshell=webshell_crawler.commands:crawl_webshell',
          ],
      },
      )