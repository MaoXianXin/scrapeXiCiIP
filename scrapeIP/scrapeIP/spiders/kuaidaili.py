import scrapy
import requests

class XiciSpider(scrapy.Spider):
	name = "kuaidaili"
	allowed_domains = ["kuaidaili.com",]

	def start_requests(self):
		url = "http://www.kuaidaili.com/free/inha/1/"
		yield scrapy.Request(url,callback=self.parse)

	def parse(self,response):
		table = response.xpath("//div[@id='list']/table")[0]
		trs = table.xpath("//tbody/tr")
		count = 1
		for tr in trs:
			count = count + 1
			if count == 14:
				break
			TEST_PROXY = "http://www.baidu.com.cn/"
			ip_ = tr.xpath("td[1]/text()").extract()[0]
			port_ = tr.xpath("td[2]/text()").extract()[0]
			PROXY = "http://" + str(ip_) + ":" + str(port_)
			proxies = {
					"http":PROXY
				}
			try:
				response = requests.get(TEST_PROXY,timeout=3,proxies=proxies)
				print(response.status_code)
				if response.status_code == 200:
					yield {
						'ip':tr.xpath("td[1]/text()").extract()[0],
						'port':tr.xpath("td[2]/text()").extract()[0],
					}
			except:
				print("connect failed!")
