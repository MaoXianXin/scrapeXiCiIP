import scrapy
import requests

class XiciSpider(scrapy.Spider):
	name = "xici2"
	allowed_domains = ["xicidaili.com",]

	def start_requests(self):
		url = "http://www.xicidaili.com/nn/2/"
		yield scrapy.Request(url,callback=self.parse)

	def parse(self,response):
		table = response.xpath("//table[@id='ip_list']")[0]
		trs = table.xpath("//tr")[1:]
		count = 1
		for tr in trs:
			count = count + 1
			if count == 30:
				break
			TEST_PROXY = "http://www.baidu.com.cn/"
			ip_ = tr.xpath("td[2]/text()").extract()[0]
			port_ = tr.xpath("td[3]/text()").extract()[0]
			PROXY = "http://" + str(ip_) + ":" + str(port_)
			proxies = {
					"http":PROXY
				}
			try:
				response = requests.get(TEST_PROXY,timeout=3,proxies=proxies)
				print(response.status_code)
				if response.status_code == 200:
					yield {
						'ip':tr.xpath("td[2]/text()").extract()[0],
						'port':tr.xpath("td[3]/text()").extract()[0],
					}
			except:
				print("connect failed!")
