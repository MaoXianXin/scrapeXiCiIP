import scrapy
import requests

class XiciSpider(scrapy.Spider):
	name = "xici"
	allowed_domains = ["xicidaili.com",]
	
	def start_requests(self):
		url = "http://www.xicidaili.com/nn/1/"
		yield scrapy.Request(url,callback=self.parse)
	def parse(self,response):
		table = response.xpath("//table[@id='ip_list']")[0]
		trs = table.xpath('//tr')[1:]
		for tr in trs:
			TEST_PROXY = 'http://icanhazip.com'
			ip_ = tr.xpath('td[2]/text()').extract()[0]
			port_ = tr.xpath('td[3]/text()').extract()[0]
			PROXY = "http://" + str(ip_) + ":" + str(port_)
			proxies = {
				"http":PROXY
				}
			try:
				html = requests.get(TEST_PROXY, timeout=3, proxies=proxies).text
				print(html)
				yield {
					'ip':tr.xpath('td[2]/text()').extract()[0],
					'port':tr.xpath('td[3]/text()').extract()[0],
				}
			except:
				print('connect faild!')
			
		
