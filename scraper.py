import requests
from scrapy.selector import Selector


class PikioScraper:

    def __init__(self, url_to_parse):
        self._url_to_parse = url_to_parse
        self._response = None
        self._article_content = "Article content: "
        self._article_title = "Article title: "
        self._date_published = "Date published: "

    def response_create_validate(self):
        """ Makes a request to web page. Return True if response code == 200, False otherwise """
        try:
            self._response = requests.get(url=self._url_to_parse)
            if self._response.status_code == 200:
                return True
        except requests.exceptions.ConnectionError:
            return False

    def get_article_content(self):
        """ Fetch article content. Update and return self._article_content variable"""
        divs = Selector(response=self._response).xpath("//div[@class='article-container']")
        for elem in divs.xpath("p/text() | h2/text()| div/p/strong/text() | p/strong/a/text() | p/a/strong/text()"):
            if "źródło" in elem.get().lower():
                continue
            self._article_content += elem.get()
        self._article_content = self._article_content.rstrip()
        return self._article_content

    def get_article_title(self):
        """ Fetch article title. Update and return self._article_title variable"""
        self._article_title += Selector(response=self._response).xpath("//h1[@class='page-heading']/text()").get()
        return self._article_title

    def get_article_date(self):
        """ Fetch article publish date. Update and return self._date_published variable"""
        self._date_published += Selector(response=self._response).xpath("//div[@class='article-date'] \
                                                                        /time/@datetime").get()
        return self._date_published

    def get_article_photos(self):
        """ Fetch photos from article and saves them into /downloaded_photos directory """
        url_list = [Selector(response=self._response).xpath("//div[@class='article-header'] \
                                                            /picture/source/source/img/@src").get()]
        divs = Selector(response=self._response).xpath("//div[@class='article-container']")
        for elem in divs.xpath("p/img/@src"):
            url_list.append(elem.get())
        for url in url_list:
            img_name = url.rsplit('/', 1)[1]
            with open(f'downloaded_photos/{img_name}', 'wb') as f:
                f.write(requests.get(url).content)
