from bs4 import BeautifulSoup

soup = BeautifulSoup("&#162;")
print soup.prettify()
