
# coding: utf-8

# In[1]:

#!/usr/bin/python3

# coding: utf-8

# !Py3.5.2


# # Archive ArtificialLawyer.com
# 
# A script to save all the articles currently hosted on artificiallawyer.com as PDF to allow train reading.
# 
# Method:
# * Take the url to an article
# * Print that article to PDF in a new folder
# * Find the next article automatically
# * Repeat
# 
# How to do this:
# 1 Ask user for url using input
# 2 Use Beautiful Soup to gather metadata (title, date)
# 3 Use <a href="https://pypi.python.org/pypi/pdfkit/0.4.1">pdfkit</a> to print url to pdf.
# Name should be the name of the article and the date.
# 4 Use Beautiful Soup to find url to next article.
# 
# Ideas for further development:
# 5 Use PyPDF to combine the PDFs into many large volumes

# dependencies / housekeeping
from bs4 import BeautifulSoup
from pdfkit import from_url
from urllib.request import urlopen
from time import sleep, gmtime, strftime

def convert_to_pdf(url):
    print("Function called. URL: {}".format(url))
    html = urlopen(url, timeout=30)
    soup = BeautifulSoup(html, "html.parser")
    article_title = soup.find("meta", property="og:title").get("content")
    article_date = soup.find("meta", property="article:published_time").get("content")[0:10]
    time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    print("{}: Article title is {}, date is {}".format(time, article_title, article_date))
    soup_div = soup.find(class_="mh-post-nav-next")
    next_article = soup_div.a.get('href')
    print("Next article is {}".format(next_article))

    # Step 3: Print to PDF

    output = "PDF/{}".format(article_date + " " + article_title + ".pdf")
    options = {
        'quiet': ''
    }
    from_url(url, output, options=options)
    print("Printed and Finished!")
    return next_article


# Step 1: Get URL
first_url = input("Please enter URL: ")

# Step 2: Get Title, Date, and Next Article URL
next_article = convert_to_pdf(first_url)

for i in range(25):
    current_article = next_article
    next_article = convert_to_pdf(current_article)