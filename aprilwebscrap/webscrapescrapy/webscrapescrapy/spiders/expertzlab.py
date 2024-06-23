import scrapy
from bs4 import BeautifulSoup as bs
from ..items import WebscrapescrapyItem

class ExpertzlabSpider(scrapy.Spider):
    name = "expertzlab"
    allowed_domains = ["www.expertzlab.com"]
    start_urls = ["https://www.expertzlab.com"]

    def parse(self, response):
        val=bs(response.text,"lxml")
        result=val.findAll('div',attrs={'class':'course'})
        print(len(result))
        # print(result[0])
        for i in result:
            item=WebscrapescrapyItem()
            item['name']=i.h4.text
            item['duration']='6 months'
            yield item
# xpath is an alternative method instead of beautiful soup.
    # def parse(self,response):
    #     # print(response.xpath("//div[@class=\"row\"]/div/div//div/div/div/text()").get())
    #     # print(response.xpath("//div[@class='row']/div/div/div/div/div/div/div/h4/a/text()").get())

    #     val=bs(response.text,"lxml")
    #     result=val.findAll('div',attrs={'class':'course'})
    #     # print(result)
    #     for i in result:
    #         yield scrapy.Request(self.start_urls[0]+i.h4.a['href'],callback=self.takendata)
    #         # print(i.h4.a['href'])
    
    # def takendata(self,response):
    #     print(response.xpath("//div[@class='row']/div/div[@class='col-lg-12 col-md-12 col-sm-12']/h2/text()").get())
