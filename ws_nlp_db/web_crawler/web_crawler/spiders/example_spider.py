import scrapy
from web_crawler.items import ProductItem  # Import your item here

class ExampleSpiderSpider(scrapy.Spider):
    name = "example_spider"
    allowed_domains = ["wikipedia.org"]
    start_urls = [
        'https://en.wikipedia.org/wiki/List_of_military_aid_to_Ukraine_during_the_Russo-Ukrainian_War'
    ]

    def parse(self, response):
        # Iterate through products on the page
        for product in response.css('div.product'):  # Modify this selector based on the website's structure
            item = ProductItem()
            item['name'] = product.css('h2.product-name::text').get()  # CSS selector for product name
            item['price'] = product.css('span.product-price::text').get()  # CSS selector for product price
            item['description'] = product.css('div.product-description::text').get()  # CSS selector for product description
            yield item
        
        # Optional: Follow pagination links and repeat the parsing process
        next_page = response.css('a.next-page::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
