import scrapy
import requests

class XiciSpider(scrapy.Spider):
	name = "xici"
	allowed_domains = ["xicidaili.com",]

	def start_requests(self):
		urls = ["http://www.xicidaili.com/nn/1/",
			"http://www.xicidaili.com/nn/2",
		      ]
		for url in urls:
			yield scrapy.Request(url,callback=self.parse)

	def parse(self,response):
		table = response.xpath("//table[@id='ip_list']")[0]
		trs = table.xpath("//tr")[1:]
		for tr in trs:
			pagetest = "http://www.baidu.com.cn/"
			ip = tr.xpath("td[2]/text()").extract()[0]
			port = tr.xpath("td[3]/text()").extract()[0]
			PROXY = "http://" + ip + ":" + port
			proxies = {
					"http":PROXY
				}
			try:
				response = requests.get(pagetest,timeout=1,proxies=proxies)
				print(response.status_code)
				if response.status_code == 200:
					yield {
						'ip':ip,
						'port':port,
					}
			except:
				print("connect failed!")
