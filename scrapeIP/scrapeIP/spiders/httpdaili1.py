import scrapy
import requests

class XiciSpider(scrapy.Spider):
	name = "youdaili1"
	allowed_domains = ["www.youdaili.net",]

	def start_requests(self):
		url = "http://www.youdaili.net/Daili/http/25081_2.html"
		yield scrapy.Request(url,callback=self.parse)

	def parse(self,response):
		ips = response.css("div.content p")
		count = 1
		for ip in ips:
#			print(ip.xpath("span/text()").extract_first())
			count = count + 1
			if count == 30:
				break
			TEST_PROXY = "http://www.baidu.com.cn/"
			ip_port = ip.xpath("span/text()").re(r'[\.0-9\:]+')
#			print(type(ip_port))
#			print(ip_port)
			PROXY = "http://" + str(ip_port[0])
#			print(PROXY)
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
			
