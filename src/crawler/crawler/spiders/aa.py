import scrapy
from bs4 import BeautifulSoup
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import HtmlResponse
from scrapy.selector import Selector
from bs4 import BeautifulSoup


# class AaSpider(scrapy.Spider):
#allowed_domains = ["toscrapea.com"]
    #start_urls = ["http://books.toscrape.com/"]
    # rules = (
    #     Rule(LinkExtractor(allow="catalogue/category")),
    # )
    # rules = (scrapy.Spider.Rule(LinkExtractor(allow="price")))
    # rules = (
    #     Rule(LinkExtractor(allow="price")),
    # )
class AaSpider(scrapy.Spider):
    name = "aa"
    allowed_domains = ["wollersheim.com"]
    #start_urls = ["https://www.aa.com/booking/search?locale=en_US&pax=1&adult=1&child=0&type=OneWay&searchType=Award&cabin=&carriers=ALL&slices=%5B%7B%22orig%22:%22MSN%22,%22origNearby%22:true,%22dest%22:%22DFW%22,%22destNearby%22:true,%22date%22:%222024-07-30%22%7D%5D&maxAwardSegmentAllowed=2"]
    start_urls = ["https://www.wollersheim.com/shop/"]
    # handle_httpstatus_list = [301, 302]
    def parse(self, response):
        #Deal with the response and be ready for jump to next page and get information
        #extrct()是用来导出数据的   `
        node_list = response.xpath('//h2[@class="woocommerce-loop-product__title"]')

        for node in node_list:
            temp = {}
            temp['name'] = BeautifulSoup(node.extract(),'html.parser').get_text()
            # print(temp)
            yield temp
            with open('page2.html', 'a', encoding='utf-8') as file:
                file.write(node.extract()+"\n")
        # html = response.bodyexi
        #
        # # Parse HTML using BeautifulSoup
        # soup = BeautifulSoup(html, 'html.parser')
        #
        # # Find all flight elements
        # flight_elements = soup.find_all("div", class_="grid-x grid-padding-x ng-star-inserted")
        #
        # # Process each flight element
        # for flight in flight_elements:
        #     # Extract flight details
        #     flight_info = {
        #         'flight_number': flight.find('span', class_='flight-number').text.strip(),0.
        #         'departure_time': flight.find('span', class_='departure-time').text.strip(),
        #         'arrival_time': flight.find('span', class_='arrival-time').text.strip(),
        #         # Add more fields as needed
        #     }
        #
        #     yield flight_info

    #     #Check if Redirected
    #     if response.status in self.handle_httpstatus_list:
    #         redirected_url = response.headers.get('Location')
    #         yield Request(redirected_url, callback=self.parse_final)
    #     else:
    #         yield self.parse_final(response)
    #
    # def parse_final(self,response):
    #     page_title = response.xpath('//title/text()').get()
    #     self.logger.info(f"Page Title: {page_title}")
    #     self.logger.info(f"URL: {response.url}")
    #     self.logger.info(f"HTML Content: {response.text}")
    #     yield {
    #         'url': response.url,
    #         'title': page_title,
    #         'content': response.text  # or response.body if you need raw bytes
    #     }

