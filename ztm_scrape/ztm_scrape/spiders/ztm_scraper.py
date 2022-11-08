import scrapy


class ZtmScraperSpider(scrapy.Spider):
    name = 'ztm_scraper'
    allowed_domains = ['academy.zerotomastery.io']
    start_urls = ['http://academy.zerotomastery.io/']

    course_title = ""
    section_title = ""


    def parse(self, response):
        course_title = response.xpath('//*[@class="course-sidebar-head"]/h2/text()').extract()



    academy.zerotomastery.io/courses/learn-tensorflow/lectures/30635969