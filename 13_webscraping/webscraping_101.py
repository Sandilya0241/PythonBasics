#########################################################################################
# Web scraping is a general term for techniques involving of data from a web site.
# Let us grab a page title
#   
#   Selector                            Match Results
#----------------------------------------------------------------------------------------
#   select('div')                       All elements with 'div' tag
#   select('#some_id')                  Elements containing id = 'some_id'
#   select('.some_class')               Elements containing class = 'some_class'
#   select('div span')                  Any elements named span within a div element
#   select('div>span')                  Any elements named span directly within a div
#                                       element, with nothing in between.
#
#########################################################################################

import requests
import bs4


def getTitle():
    result = requests.get("https://example.com")
    soup = bs4.BeautifulSoup(result.text,"lxml")
    print(soup.select("title")[0].getText())
    site_paragraphs = soup.select('p')
    print(type(site_paragraphs[0]))
    print(site_paragraphs[0].getText())    


def getBasedOnClass():
    # result = requests.get("https://en.wikipedia.org/wiki/A._P._J._Abdul_Kalam")
    result = requests.get("https://en.wikipedia.org/wiki/India")
    # if(requests.Response.ok)
    print(requests.Response.ok)
    soup = bs4.BeautifulSoup(result.text,"lxml")
    # print(soup.findAll(attrs={"title" : "Bharat Ratna"}))
    for elm in soup.select('.infobox-label'):
        print(elm.getText())
    

def downloadImages():
    result = requests.get("https://en.wikipedia.org/wiki/India")
    soup = bs4.BeautifulSoup(result.text,"lxml")
    computer = soup.select('span.mw-image-border>a.mw-file-description>img.mw-file-element')[0]
    print(computer['src'])

    image_link = requests.get("https:"+computer['src'])
    with open("india_flag.jpg","wb") as fp:
        fp.write(image_link.content)


def webscrape_multipage_website():
    two_star_rating_books = []
    base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
    
    for page_num in range(1,51):
        res = requests.get(base_url.format(page_num))
        soup = bs4.BeautifulSoup(res.text,"lxml")
        books = soup.select(".product_pod")
        for book in books:
            if len(book.select(".star-rating.Two")) != 0:
                book_title = book.select("a")[1]['title']
                two_star_rating_books.append(book_title)
        print(f'{page_num/(len(range(1,51))) * 100}% completed...')
    print(two_star_rating_books)


if __name__ == "__main__":
    # getTitle()
    # getBasedOnClass()
    # downloadImages()
    webscrape_multipage_website()