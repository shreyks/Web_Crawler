# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import codecs
import sys
import csv
# from kitchen.text.converters import getwriter

UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)


# https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_2?_encoding=UTF8&pg=2
# https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_3?_encoding=UTF8&pg=3

amazon = "https://www.amazon.in/"

csvData = [["Name", "URL", "Author", "Price",
            "Number of Ratings", "Average Rating"]]


# myCSVFile = open ('example.csv', 'w')

for j in range(1, 6):
    url = "https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_1?ie=UTF8&pg=" + \
        str(j)
    page = requests.get(url)
    data = page.text

    soup = BeautifulSoup(data, "html.parser")

    # print soup.find_all ('div', class_="a-section a-spacing-none p13n-asin")[0]

    # soup2 = BeautifulSoup (str(soup.find_all('div', class_="p13n-sc-truncate p13n-sc-line-clamp-1")), "html.parser")

# soup2 = BeautifulSoup (str(soup.find_all('div', class_="a-section a-spacing-none p13n-asin")), "lxml")

    # print soup2.find_all ('div', class_="p13n-sc-truncate p13n-sc-line-clamp-1").get_text()

    # print "-------------------------"

    x = (j - 1) * 20 + 1
    for i in soup.find_all('div', class_="a-section a-spacing-none p13n-asin"):
        tempData = []
        # print "Book ", x, " :"
        soup2 = BeautifulSoup(str(i), "lxml")

        bookName = soup2.find(
            'div', class_="p13n-sc-truncate p13n-sc-line-clamp-1")
        if bookName is None:
            # print "Book Name ------ NA"
            tempData.append("Not Available")
        else:
            name = bookName.get_text().strip()
            # print "-----------", type(name)
            # print "Book Name ------ ", name
            tempData.append(name)

        m = soup2.find('a', class_="a-link-normal")
        n = m.get("href")
        # print "Book URL ------- ", amazon+n
        tempData.append(amazon + n)

        bookAuthor = soup2.find_all('div', class_="a-row a-size-small")
        if bookAuthor is None:
            # print "Author --------- NA"
            tempData.append("Not Available")
        else:
            # print "Author --------- ", bookAuthor[0].get_text().strip()
            tempData.append(bookAuthor[0].get_text().strip())
            # tempData.append (str(bookAuthor[0].get_text().strip()))

        bookPrice = soup2.find('span', class_="p13n-sc-price")
        if bookPrice is None:
            # print "Price ---------- NA"
            tempData.append("Not Available")
        else:
            # print "Price ---------- ", bookPrice.get_text().strip()
            tempData.append(bookPrice.get_text().strip())

        # print "Book Link ------ ", soup2.find_all ('a', class_="a-link-normal")[0].get_text().strip()

        numberOfRatings = soup2.find('a', class_="a-size-small a-link-normal")
        if numberOfRatings is None:
            # print "No. Of Ratings - NA"
            tempData.append("Not Available")
        else:
            # print "No. Of Ratings - ", numberOfRatings.get_text().strip()
            tempData.append(numberOfRatings.get_text().strip())

        bookRating = soup2.find('span', class_="a-icon-alt")
        if bookRating is None:
            # print "Rating --------- NA"
            tempData.append("Not Available")
        elif bookRating.get_text().strip() is "Prime":
            # print "Rating --------- NA"
            tempData.append("Not Available")
        else:
            # print "Rating --------- ", bookRating.get_text().strip()
            tempData.append(bookRating.get_text().strip())

        # print "Rating --------- ", soup2.find_all ('span', class_="a-icon-alt")[0].get_text().strip()

        csvData.append(tempData)

        # print "tempdata is ", tempData

        x += 1
        # print "----------------------------------------"
        # print csvData

        # with open ('example.csv', 'wb') as f:
        # 	writer = csv.writer(f)
        # 	for i in csvData:
        # 		i = [s.encode('utf-8') for s in i]
        # 		writer.writerows([i])

        # with open('example.csv', 'w') as myCSVFile:
        # 	writer = csv.writer(myCSVFile)
        # 	# writer.writerows(csvData)
        # 	for i in csvData:
        # 		if i: # and i != u'':
        # 			writer.writerow([i.encode("UTF-8")])

        # with myCSVFile:
        # 	writer = csv.writer (myCSVFile)
        # 	writer.writerows (csvData)

        if x == ((j - 1) * 20 + 1 + 20):
            break

with open('./output/in_book.csv', 'wb') as f:
    writer = csv.writer(f)
    for i in csvData:
        i = [s.encode('utf-8') for s in i]
        writer.writerows([i])

    # x = 1
    # for i in soup.find_all('div', class_="a-section a-spacing-none p13n-asin"):
    # 	if (x == 1):
    # 		# m = i.get ('href')
    # 		soup2 = BeautifulSoup (str(i), "lxml")
    # 		m = soup2.find ('a', class_="a-link-normal")
    # 		n = m.get ('href')
    # 		print "Book Link ------ ", amazon + n
    # 		# print "Book Name ------ ", soup2.find_all ('div', class_="p13n-sc-truncate p13n-sc-line-clamp-1").get_text().strip()
    # 		# print soup2
    # 		x += 1
    # 		print "-----------------------"

    # print i.get_text().strip()
    # print
    # x = 1
    # soup2 = BeautifulSoup (str(i), "lxml")
    # print soup2.find_all ('div', class_="p13n-sc-truncate p13n-sc-line-clamp-1")[0].get_text().strip()


# print "-----------------------------------------------------"

# x = 0
# for i in soup.find_all('div', class_="a-section a-spacing-none p13n-asin"):
# 	if (x==16 or x==17):
# 		print i
# 		print "_______"
# 	x += 1


# print soup2.find_all ('div', class_="p13n-sc-truncate p13n-sc-line-clamp-1")[0].get_text().strip

# for i in soup2.find_all ('div', class_="p13n-sc-truncate p13n-sc-line-clamp-1"):
# 	print i.get_text().strip()
