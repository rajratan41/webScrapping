# if you want to scrap a website
# 1. Use the API
# 2. HTML Web Scraping using some tool like bs4 (Beautiful Soup)

# STEP 1 - Install all the requirements
# pip install requests
# pip install bs4
# pip install html5lib

# Step 2 - Get the HTML
import requests
from bs4 import BeautifulSoup
url = 'https://codewithharry.com/'

r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step 3: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# Step 4: HTML Tree Transversal


# Commonly used types of objects:
# 1. Tag -     print(type(title))
# 2. NavigableString -  print(type(title.string))
# 3. BeautifulSoup -  print(type(soup))
# 4. Comment
markup = "<p><!-- this is comment --></p>"
soup2 = BeautifulSoup(markup)
# print(soup2)
# print(soup2.p.string)
# print(type(soup2.p.string))
# exit()

# Get the Title of the HTML Page
title = soup.title

# Get all the Paragraphs from the Page
paras = soup.find_all('p')
# print(paras)

# Get all the Anchor Tags from the Page
anchors = soup.find_all('a')
# print(anchors)

# Get all the links on the Page:
for link in anchors:
    h = link.get('href')
    # print(h)

# Get all links without # and add specific link to it
# 1. get anchor tag
anchors = soup.find_all('a')
all_links = set()

# 2 get all the links
for link in anchors:
    if(link.get('href') != '#'):
        linkText = "https://codewithharry.com" + link.get('href')
        all_links.add(link)
        # print(linkText)

# Get the First Element in the HTML page
fpara = soup.find('p')
# print(fpara)

# Get classess of any element in the HTML Page
fpara = soup.find('p')['class']
# print(fpara)

# Find all the elements with class name text-sm [Finding Specific Class inside Element]
clas = soup.find_all("p", class_="text-sm")
# print(clas)

# Get the Text from the tags/soup
tex = soup.find('p').get_text()
# print(tex)

# Get text from whole HTML page
tex2 = soup.get_text()
# print(tex2)


# Get Specific div using it's Id
divId = soup.find(id="someId")
# print(divId)
# it will give that specific div with it's id someId if present

# Get Children of the div have id is someId

divId2 = soup.find(id="someId").children
# print(divId2)
# it will give that specific div with it's id someId if present

# Get Contents of the div have id is someId

divId3 = soup.find(id = "someId")

for ele in divId3.contents:
    # print(ele)
# print(divId3)
# it will give that specific div with it's id someId if present


# Diffrence between .contents and .children

# .contents - A tag's children are available as a list.  (sare elements save honge memory me), (slow hoga bare pages k liye bcz memory me store hoga)
# .children - A tag's children are available as a generator.  (memory me store nhi hoga but kvi bhi access kar sakte hain - iterate kr k for loop se), (fast hoga bare pages k liye)


# ####################################

# Get strings inside a specific div with id

divId4 = soup.find(id = "someId")

for item in divId4.strings:
    # print(item)

# Beautify string
for i in divId4.stripped_strings:
    # print(i)

# To print parent of divid4
# print(divId4.parent)

# iterate though parents
for it in divId4.parents:
    # print(item.name) - nav, body, html, [document]

# #########################
# .next_sibling, .previous_sibling - space ko v element samjhta hai

# print(divId.next_sibling)
# print(divId.next_sibling.next_sibling) 
#(.next_sibling kr k kitne v aage jaa skte hain)

# print(divId.previous_sibling.previous_sibling)

#####################################
# To get CSS selector
    # (# - id , . - class)
eleme = soup.select(".loginModal")
eleme1 = soup.select("#loginModal")



# Documentation of Beautiful Soup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/