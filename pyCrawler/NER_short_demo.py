# -*- coding: utf-8 -*-

from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from itertools import groupby

st = StanfordNERTagger('/Users/Julius/Downloads/stanford-ner-2016-10-31/classifiers/english.all.3class.distsim.crf.ser.gz',
					   '/Users/Julius/Downloads/stanford-ner-2016-10-31/stanford-ner.jar',
					   encoding='utf-8')

text1 = "Historically, the Company's principal products were built using the Motorola\
68000  series  of  Complex Instruction Set Computing (CISC) microprocessors.\
However,  computer  manufacturers  are  beginning  to  move  from   a   CISC\
architecture  to  a  Reduced Instruction Set Computing (RISC)  architecture.\
Accordingly,  during 1994, the Company began a major product transition  and\
introduced  a  new  line  of  Macintosh  computers  based  on  the PowerPC \
(registered trademark) architecture,  a  new  RISC  microprocessor  jointly\
developed  by   Apple, International  Business Machines Corporation (IBM) \
and Motorola,  Inc.   The Company  believes  that these PowerPC based \
products will yield  significant improvements in price/performance and \
functionality compared with  its  CISC-based  products.  Further information\
regarding this product transition  may be found in Part II, Item 7 of this \
Annual Report on Form 10-K (the \"Form 10-K\")  under  the subheading \"Product\
Introductions and Transitions\"  included under  the  heading  \"Factors That \
May Affect Future Results  and  Financial Condition\", which information is \
hereby incorporated by reference."

text = "The decrease and increase in equipment and services revenues in fiscal 2015 and 2014 , respectively, were primarily due to a decrease and an increase in QCT revenues of $1.49 billion and $1.94 billion, respectively. The increase in equipment and services revenues in fiscal 2014 was partially offset by a decrease of $305 million as a result of the sale of our Omnitracs division during fiscal 2014. The increase in our licensing revenues in fiscal 2015 was primarily due to an increase in QTL revenues of $378 million. The decrease in our licensing revenues in fiscal 2014 was primarily due to a decrease in a nonreportable segment’s revenues of $32 million, partially offset by an increase in QTL revenues of $15 million. QCT and QTL segment revenues related to the products of Samsung Electronics and Hon Hai Precision Industry Co., Ltd/Foxconn, its affiliates and other suppliers to Apple Inc. comprised 45%, 49% and 43% of total consolidated revenues in fiscal 2015 , 2014 and 2013 , respectively. Revenues from customers in China, South Korea and Taiwan comprised 53% , 16% and 13% , respectively, of total consolidated revenues for fiscal 2015 , compared to 50% , 23% and 11% , respectively, for fiscal 2014 , and 49% , 20% and 11% , respectively, for fiscal 2013 . We report revenues from external customers by country based on the location to which our products or services are delivered, which for QCT is generally the country in which our customers manufacture their products, or for licensing revenues, the invoiced addresses of our licensees. As a result, the revenues by country presented herein are not necessarily indicative of either the country in which the devices containing our products and/or intellectual property are ultimately sold to consumers or the country in which the companies that sell the devices are headquartered. For example, China revenues would include revenues related to shipments of integrated circuits to a company that is headquartered in South Korea but that manufactures devices in China, which devices are then sold to consumers in Europe and/or the United States."

tokenized_text = word_tokenize(text)
classified_text = st.tag(tokenized_text)

sent_tokenize_list = sent_tokenize(text)

print "# Sentence Count", len(sent_tokenize_list)

OrgList = []
for idx, sent in enumerate(sent_tokenize_list):
	if idx % 10 == 0:
		print idx

	tokenized_text = word_tokenize(sent)
	classified_text = st.tag(tokenized_text)

	for tag, chunk in groupby(classified_text, lambda x:x[1]):
		if tag != "O":
			item = " ".join(w for w, t in chunk)
			if item not in OrgList:
				OrgList.append(item)

print "# Organization Count", len(OrgList)
print OrgList
