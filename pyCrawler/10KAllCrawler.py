# '''Python package to crawl the publicly available forms filed with the Securities and Exchange Commission (SEC)

#     under the new Electronic Data Gathering, Analysis and Retrieval System (EDGAR).

#     Copyright (C) 2013  Sreecharan Sankaranarayanan

#     This program is free software; you can redistribute it and/or modify

#     it under the terms of the GNU General Public License as published by

#     the Free Software Foundation; either version 2 of the License, or

#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,

#     but WITHOUT ANY WARRANTY; without even the implied warranty of

#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the

#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License along

#     with this program; if not, write to the Free Software Foundation, Inc.,

#     51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

#

#     Full License can be viewed at https://github.com/sreecharan93/FormCrawl/blob/master/LICENSE

#     Contact : sreecharan93@gmail.com											'''





#    https://www.sec.gov/cgi-bin/viewer?action=view&cik=1045810&accession_number=0001045810-16-000205&xbrl_type=v#

#    GITHUB : https://github.com/sreecharan93/FormCrawl/blob/master/10-K%20Crawler.py

#    SIC Code : https://www.sec.gov/info/edgar/siccodes.htm



from bs4 import BeautifulSoup

import re

import requests

import os

from nltk import pos_tag, ne_chunk

from nltk.tokenize import SpaceTokenizer



## Clean HTML Entity

from HTMLParser import HTMLParser



def cleanhtml(raw_html):

  h = HTMLParser()

  cleanr = re.compile('<.*?>')

  cleantext = re.sub(cleanr, '', raw_html)

#  s = BeautifulSoup(cleantext.encode('utf-8'))

#  return s.prettify()

  return cleantext

#  return h.unescape(cleantext)





# Procedure to retrieve the CIK codes with the entered SEC Code  ## 3674 / 3663 / 3571

# sec = input("Enter the SEC Code : ")

sec = 3674

count = 0 # Count for displaying 40 elements on the Company Search page

tddoc=[1] # Initialize to any non-empty list

companyList = []

while(len(tddoc)!=0):

	base_url = "http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&SIC="+str(sec)+"&owner=include&match=&start="+str(count)+"&count=40&hidefilings=0"

	r = requests.get(base_url)

	data = r.text.encode('utf-8')

	soup = BeautifulSoup(data)

	tddoc = soup.find_all("td")

	for i in range(0,len(tddoc)):

		companyList.append(tddoc[i].string)

		i+=2

	count+=40

# `companyList` now contains the list of companies corresponding to the entered SEC code.

# cikList = []

# cikList = ['0001038341','0001045810','0001649338','0001054374','0001101149','0001649338','0000320193'] #NVIDIA, BROADCOM, QCOM, Apple

cikList = ['0000066740','0000006281','0000002488','0000820313','0000023071','0001649338','0001054374',
'0001649338',
'0000772406',
'0000024741',
'0000029002',
'0001038272',
'0000050863',
'0000768545',
'0001096324',
'0001096325',
'0001294924',
'0000898293',
'0000887730',
'0001587523',
'0001099375',
'0001099372',
'0001099370',
'0000791907',
'0000743316',
'0000723125',
'0000067472',
'0001045810',
'0001097864',
'0001604778',
'0001119869',
'0000029669',
'0001000180',
'0001137789',
'0001494656',
'0000004127',
'0000817720',
'0000097476',
'0000715577',
'0001627223',
'0001587231',
'0001587413',
'0001587412',
'0001519061',
'0001116942',
'0000103730',
'0001487952',
'0000106040',
'0001168332',
'0001689431',
'0000827054']

#cikList = ['0001101149','0000320193'] # QCOM

#cikList = ['0001649338'] # BROADCOM

#cikList = ['0000320193'] # Apple





#for i in range(0,len(companyList),3):   ## by eliza

#    cikList.append(companyList[i])   ## by eliza





# List of CIK codes to be crawled has been extracted into `cikList`



# Below procedure creates the required folders if they don't already exist.

if not os.path.exists("./Crawled Data/"):

	os.makedirs("./Crawled Data/")

if not os.path.exists("./Crawled Data/"+str(sec)):

	os.makedirs("./Crawled Data/"+str(sec))

for j in range(len(cikList)):

	if not os.path.exists("./Crawled Data/"+str(sec)+"/"+str(cikList[j])):

		os.makedirs("./Crawled Data/"+str(sec)+"/"+str(cikList[j]))



for i in range(len(cikList)):

	# print cikList[i]

	base_url = "http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK="+str(cikList[i])+"&type=10-K&dateb=&owner=exclude&output=xml&count=100"

	r = requests.get(base_url)

	data = r.text

	soup = BeautifulSoup(data) # Initializing to crawl again

	linkList=[] # List of all links from the CIK page

	# If the link is .htm convert it to .html

	for link in soup.find_all('filinghref'):

		URL = link.string

		if link.string.split(".")[len(link.string.split("."))-1] == "htm":

			URL+="l"

    		linkList.append(URL)

	linkListFinal = linkList

	docList = [] # List of URL to the text documents

	docNameList = [] # List of document names



	for k in range(len(linkListFinal)):

		requiredURL = str(linkListFinal[k])[0:len(linkListFinal[k])-11]

		txtdoc = requiredURL+".txt"
		print(txtdoc)

		docname = txtdoc.split("/")[len(txtdoc.split("/"))-1]

		docList.append(txtdoc)

		docNameList.append(docname)

	# Save every text document into its respective folder

	for j in range(len(docList)):
        
		base_url = docList[j]

		r = requests.get(base_url)

		data = r.text.encode('utf-8')

		path = "./Crawled Data/"+str(sec)+"/"+str(cikList[i])+"/"+str(docNameList[j])

		filename = open(path,"a")

		filename.write(cleanhtml(data))



		# tokenizer = SpaceTokenizer()

		# toks = tokenizer.tokenize(data)

		# pos = pos_tag(toks.split())

		# #pos = pos_tag(toks)

		# chunked_nes = ne_chunk(pos)



	##  	nes = [' '.join(map(lambda x: x[0], ne.leaves())) for ne in chunked_nes if isinstance(ne, nltk.tree.Tree) ]

		# path = "d:/Crawled Data/"+str(sec)+"/"+str(cikList[i])+"/"+str(docNameList[j])+"_NER"

		# filename = open(path,"a")

		# filename.write(nes)
