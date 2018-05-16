#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 16:26:59 2018

@author: shrey
"""
from bs4 import BeautifulSoup
from requests import get
import csv


def spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.amazon.com/gp/bestsellers/books/ref=zg_bs_pg_1?ie=UTF8&pg=' + \
            str(page)
        code = get(url)
        soup = BeautifulSoup(code.text, "html.parser")
        count = 0
        for link in soup.findAll("div", class_="a-section a-spacing-none p13n-asin"):
            if(count < 20):
                book = []

                Name = link.find(
                    "div", class_="p13n-sc-truncate p13n-sc-line-clamp-1")
                if Name is None:
                    book.append("Not available")
                else:
                    book.append(Name.get_text().strip())
                url = link.find("a", class_="a-link-normal")
                if url is None:
                    book.append("Not available")
                else:
                    url = "https://www.amazon.com" + url["href"]
                    book.append(url)
                Author = link.find("a", class_="a-size-small a-link-child")

                if Author is None:
                    Author = link.find(
                        "span", class_="a-size-small a-color-base")
                    if Author is None:
                        book.append("Not available")
                    else:
                        book.append(Author.get_text().strip())
                else:
                    book.append(Author.get_text().strip())

                Price = link.find("span", class_="p13n-sc-price")
                if Price is None:
                    book.append("Not available")
                elif Price.get_text().strip() == "Prime":
                    book.append("Not available")
                else:
                    book.append(Price.get_text().strip())

                NoRatings = link.find("a", class_="a-size-small a-link-normal")
                if NoRatings is None:
                    book.append("Not available")
                else:
                    book.append(NoRatings.get_text().strip())

                Rating = link.find("span", class_="a-icon-alt")
                if Rating is None:
                    book.append("Not available")
                elif (Rating.get_text().strip() == "Prime"):
                    book.append("Not available")
                else:
                    book.append(Rating.get_text().strip())

                with open('./output/com_book.csv', 'a') as MyFile:
                    write = csv.writer(MyFile, delimiter=',',
                                       quoting=csv.QUOTE_MINIMAL)
                    write.writerow(book)

                count = count + 1
        page += 1


book = ["Name", "URL", "Author", "Price",
        "Number of Ratings", "Average Rating"]
with open('./output/com_book.csv', 'a') as MyFile:
    write = csv.writer(MyFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    write.writerow(book)
spider(5)
