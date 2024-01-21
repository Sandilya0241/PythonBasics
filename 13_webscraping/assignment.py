from requests import get
import bs4

#TASK1: Use requests library and BeautifulSoup to connect to http://quotes.toscrape.com/ and get the HMTL text from the homepage.
def task1():
    res = get("http://quotes.toscrape.com/")
    print(res.text)

#TASK2: Get the names of all the authors on the first page.
def task2():
    res = get("http://quotes.toscrape.com/")
    soup = bs4.BeautifulSoup(res.text,"lxml")
    authors = set()
    authors_list = soup.select(".author")
    for author in authors_list:
        authors.add(author.getText())
    print(authors)

#TASK3: Create a list of all the quotes on the first page.
def task3():
    res = get("http://quotes.toscrape.com/")
    soup = bs4.BeautifulSoup(res.text,"lxml")
    quotes = []
    quotes_list = soup.select(".quote")
    for quote in quotes_list:
        quotes.append(quote.select("div>span.text")[0].getText())
    print(quotes)


#TASK4: Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text shown on the top right from the home page (e.g Love,Inspirational,Life, etc...). HINT: Keep in mind there are also tags underneath each quote, try to find a class only present in the top right tags, perhaps check the span.
def task4():
    res = get("http://quotes.toscrape.com/")
    soup = bs4.BeautifulSoup(res.text,"lxml")
    
    tag_box = soup.select(".tags-box")[0]
    tags = tag_box.select(".tag-item")
    for tag in tags:
        print(tag.getText())

# No quotes found!
# TASK5: Notice how there is more than one page, and subsequent pages look like this http://quotes.toscrape.com/page/2/. Use what you know about for loops and string concatenation to loop through all the pages and get all the unique authors on the website. Keep in mind there are many ways to achieve this, also note that you will need to somehow figure out how to check that your loop is on the last page with quotes. For debugging purposes, I will let you know that there are only 10 pages, so the last page is http://quotes.toscrape.com/page/10/, but try to create a loop that is robust enough that it wouldn't matter to know the amount of pages beforehand, perhaps use try/except for this, its up to you!
def task5():
    authors = set()
    base_url = "https://quotes.toscrape.com/page/{}/"
    page_count = 1
    while True:        
        res = get(base_url.format(page_count))
        if "No quotes found!" in res.text:
            break
        else:
            soup = bs4.BeautifulSoup(res.text,"lxml")
            authors_list = soup.select(".author")
            for author in authors_list:
                authors.add(author.getText()) 
        page_count+=1
    print(authors)
    print(len(authors))


if __name__=="__main__":
    task5()