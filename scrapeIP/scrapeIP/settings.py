# -*- coding: utf-8 -*-

# Scrapy settings for scrapeIP project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapeIP'

SPIDER_MODULES = ['scrapeIP.spiders']
NEWSPIDER_MODULE = 'scrapeIP.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapeIP (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0'
# Obey robots.txt rules
ROBOTSTXT_OBEY = True

COOKIES_ENABLED = False

AJAXCRAWL_ENABLED = True

ITEM_PIPELINES = {
	'scrapeIP.pipelines.ScrapeipPipeline':400,
}
